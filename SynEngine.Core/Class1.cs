using System.Diagnostics;
using System.IO;
using System.Text.RegularExpressions;
using System.Collections.Generic;

namespace SynEngine.Core;

/// <summary>
/// SynScript hata sınıfı - daha iyi hata raporlama
/// </summary>
public class SynScriptError
{
    public int LineNumber { get; set; }
    public string? Message { get; set; }
    public string? ErrorType { get; set; } // "SyntaxError", "TypeError", etc.
    public string? Code { get; set; }
    
    public override string ToString()
    {
        return $"{ErrorType} at line {LineNumber}: {Message}\n  {Code}";
    }
}

/// <summary>
/// SynScript'ten Python'a transpiler
/// </summary>
public class SynScriptTranspiler
{
    private List<SynScriptError> _errors = new();
    private int _currentLine = 0;
    
    public List<SynScriptError> Errors => _errors;
    
    public string TranspileToPython(string synScriptCode)
    {
        _errors.Clear();
        _currentLine = 0;
        
        // Validasyon yapısal hatalar için
        ValidateSyntax(synScriptCode);
        
        if (_errors.Count > 0)
        {
            throw new Exception($"SynScript Syntax Errors:\n{string.Join("\n", _errors)}");
        }
        
        string pythonCode = synScriptCode;

        // @export dekoratörü -> Python comment + export flag
        pythonCode = Regex.Replace(pythonCode, @"@export\s*", "# __export__\n");

        // Diğer dekoratörler
        pythonCode = Regex.Replace(pythonCode, @"@on_ready\s*", "# __on_ready__\n");
        pythonCode = Regex.Replace(pythonCode, @"@process\s*", "# __process__\n");
        pythonCode = Regex.Replace(pythonCode, @"@signal\s*", "# __signal__\n");

        // v0.2.0 State Machine blocks
        // state Name: -> class Name(State):
        pythonCode = Regex.Replace(pythonCode, @"\bstate\s+([A-Za-z_][A-Za-z0-9_]*)\s*:", "class $1(State):");
        
        // fn on_enter/tick/on_exit -> def with proper indentation
        pythonCode = Regex.Replace(pythonCode, @"\bfn\s+on_enter\s*\(\)\s*:", "    def on_enter(self):");
        pythonCode = Regex.Replace(pythonCode, @"\bfn\s+tick\s*\(\s*delta\s*:\s*float\s*\)\s*:", "    def tick(self, delta: float):");
        pythonCode = Regex.Replace(pythonCode, @"\bfn\s+on_exit\s*\(\)\s*:", "    def on_exit(self):");
        
        // v0.2.0 Signal declarations
        // signal name(param: type) -> name = Signal()
        pythonCode = Regex.Replace(pythonCode, @"\bsignal\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\([^)]*\)", "$1 = Signal('$1')");
        
        // v0.2.0 Signal binding: source => target.method -> source.connect(target.method)
        pythonCode = Regex.Replace(pythonCode, @"([a-zA-Z_][a-zA-Z0-9_]*)\s*=>\s*([a-zA-Z_][a-zA-Z0-9_]*\.[a-zA-Z_][a-zA-Z0-9_]*)", "$1.connect($2)");
        
        // v0.2.0 @operator namespace
        // @vector.add(v1, v2) -> native_vector_add(v1, v2)
        pythonCode = Regex.Replace(pythonCode, @"@vector\.add\s*\(", "native_vector_add(");
        pythonCode = Regex.Replace(pythonCode, @"@vector\.subtract\s*\(", "native_vector_subtract(");
        pythonCode = Regex.Replace(pythonCode, @"@vector\.multiply\s*\(", "native_vector_multiply(");
        pythonCode = Regex.Replace(pythonCode, @"@vector\.normalize\s*\(", "native_vector_normalize(");
        pythonCode = Regex.Replace(pythonCode, @"@vector\.distance\s*\(", "native_vector_distance(");
        
        // @math operations
        pythonCode = Regex.Replace(pythonCode, @"@math\.sin\s*\(", "native_math_sin(");
        pythonCode = Regex.Replace(pythonCode, @"@math\.cos\s*\(", "native_math_cos(");
        pythonCode = Regex.Replace(pythonCode, @"@math\.sqrt\s*\(", "native_math_sqrt(");
        pythonCode = Regex.Replace(pythonCode, @"@math\.pow\s*\(", "native_math_pow(");

        // Tip annotations'ı Python stili'ne çevir
        // var x: int -> x: int
        pythonCode = Regex.Replace(pythonCode, @"\bvar\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*:\s*", "$1: ");
        // var x = 5 -> x = 5
        pythonCode = Regex.Replace(pythonCode, @"\bvar\s+", "");

        // function keyword'ünü def'e çevir
        pythonCode = Regex.Replace(pythonCode, @"\bfunction\s+", "def ");
        
        // Return tip annotationları ekle (-> type)
        pythonCode = Regex.Replace(pythonCode, @"def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(([^)]*)\)\s*->\s*([a-zA-Z0-9_]+)\s*:", "def $1($2) -> '$3':");

        // StdLib imports'ını ekle
        pythonCode = GenerateStdLibImports() + pythonCode;

        return pythonCode;
    }
    
    private void ValidateSyntax(string synScriptCode)
    {
        var lines = synScriptCode.Split('\n');
        var openBraces = 0;
        var openParens = 0;
        var openBrackets = 0;
        
        foreach (var line in lines)
        {
            _currentLine++;
            var trimmed = line.Trim();
            
            // Boş satırları ve yorumları atla
            if (string.IsNullOrEmpty(trimmed) || trimmed.StartsWith("#"))
                continue;
            
            // Parantez, bracket ve brace eşlemesini kontrol et
            foreach (var ch in trimmed)
            {
                if (ch == '(') openParens++;
                else if (ch == ')') openParens--;
                else if (ch == '[') openBrackets++;
                else if (ch == ']') openBrackets--;
                else if (ch == '{') openBraces++;
                else if (ch == '}') openBraces--;
            }
            
            // Hataları kontrol et
            if (openParens < 0) AddError("SyntaxError", "Unmatched closing parenthesis", trimmed);
            if (openBrackets < 0) AddError("SyntaxError", "Unmatched closing bracket", trimmed);
            if (openBraces < 0) AddError("SyntaxError", "Unmatched closing brace", trimmed);
        }
        
        // Son kontroller
        if (openParens != 0) AddError("SyntaxError", "Unclosed parenthesis", "");
        if (openBrackets != 0) AddError("SyntaxError", "Unclosed bracket", "");
        if (openBraces != 0) AddError("SyntaxError", "Unclosed brace", "");
    }
    
    private void AddError(string errorType, string message, string code)
    {
        _errors.Add(new SynScriptError
        {
            ErrorType = errorType,
            LineNumber = _currentLine,
            Message = message,
            Code = code
        });
    }
    
    private string GenerateStdLibImports()
    {
        return "# ===== SynScript StdLib Imports (v0.2.0) =====\n" +
               "from sys import path as _sys_path\n" +
               "from os import path as _os_path\n" +
               "_lib_path = _os_path.join(_os_path.dirname(__file__), '../../SynScript/StdLib')\n" +
               "if _lib_path not in _sys_path:\n" +
               "    _sys_path.insert(0, _lib_path)\n" +
               "\n" +
               "# v0.1 Modules\n" +
               "from synmath import SynMath\n" +
               "from syncolor import SynColor\n" +
               "from syntimer import SynTimer, DeltaTimer\n" +
               "from synvector import Vector2, Vector3\n" +
               "\n" +
               "# v0.2 State Machine & Event System\n" +
               "from synstate import State\n" +
               "from synsignal import Signal\n" +
               "from synactor import Actor\n" +
               "from syntyping import TypeInference\n" +
               "\n" +
               "class Input:\n" +
               "    @staticmethod\n" +
               "    def is_action_pressed(action: str) -> bool:\n" +
               "        return False\n" +
               "    \n" +
               "    @staticmethod\n" +
               "    def is_action_released(action: str) -> bool:\n" +
               "        return False\n" +
               "\n" +
               "# ===== End StdLib Imports (v0.2.0) =====\n\n";
    }
}

public class SynScriptEngine
{
    private readonly SynScriptTranspiler _transpiler = new();
    private string _projectRoot;
    
    public SynScriptEngine(string? projectRoot = null)
    {
        // Proje kök dizinini ayarla (StdLib bulmak için)
        _projectRoot = projectRoot ?? Directory.GetCurrentDirectory();
    }

    public string ExecuteFunction(string functionName, string? synScriptPath = null)
    {
        try
        {
            // SynScript dosyası yolu
            synScriptPath ??= Path.Combine(_projectRoot, "main.syn");
            
            if (!File.Exists(synScriptPath))
            {
                throw new FileNotFoundException($"SynScript file not found: {synScriptPath}");
            }
            
            // SynScript dosyasını oku
            string synScriptCode = File.ReadAllText(synScriptPath);

            // SynScript'i Python'a çevir
            Console.WriteLine("[SynEngine] Transpiling SynScript...");
            string pythonCode = _transpiler.TranspileToPython(synScriptCode);

            // Fonksiyon çağrısını ekle
            pythonCode += $"\ntry:\n    print({functionName}())\nexcept NameError as e:\n    print(f'Function not found: {functionName}')\nexcept Exception as e:\n    print(f'Error: {{e}}')";

            // Geçici Python dosyası oluştur
            string tempFile = Path.ChangeExtension(Path.GetTempFileName(), ".py");
            File.WriteAllText(tempFile, pythonCode);
            
            Console.WriteLine($"[SynEngine] Executing Python code from {tempFile}...");

            // Python kodu çalıştır
            var process = new Process
            {
                StartInfo = new ProcessStartInfo
                {
                    FileName = "/usr/bin/python3",
                    Arguments = tempFile,
                    RedirectStandardOutput = true,
                    RedirectStandardError = true,
                    UseShellExecute = false,
                    CreateNoWindow = true
                }
            };

            process.Start();
            string output = process.StandardOutput.ReadToEnd();
            string error = process.StandardError.ReadToEnd();
            process.WaitForExit();

            // Temp dosyayı sil
            File.Delete(tempFile);

            if (!string.IsNullOrEmpty(error))
            {
                throw new Exception($"Python Error:\n{error}");
            }
            
            if (process.ExitCode != 0)
            {
                throw new Exception($"Process exited with code {process.ExitCode}");
            }

            Console.WriteLine("[SynEngine] Execution completed successfully.");
            return output.Trim();
        }
        catch (Exception ex)
        {
            Console.WriteLine($"[SynEngine] ERROR: {ex.Message}");
            throw;
        }
    }
    
    public void ValidateSynScript(string synScriptPath)
    {
        try
        {
            string synScriptCode = File.ReadAllText(synScriptPath);
            _transpiler.TranspileToPython(synScriptCode);
            
            if (_transpiler.Errors.Count > 0)
            {
                Console.WriteLine("[SynEngine] Validation errors found:");
                foreach (var error in _transpiler.Errors)
                {
                    Console.WriteLine($"  {error}");
                }
            }
            else
            {
                Console.WriteLine("[SynEngine] Validation successful!");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"[SynEngine] Validation failed: {ex.Message}");
        }
    }
}

public class Class1
{
    public static void Main()
    {
        Console.WriteLine("╔═══════════════════════════════════════╗");
        Console.WriteLine("║    SynEngine v0.1 - Language Phase    ║");
        Console.WriteLine("╚═══════════════════════════════════════╝\n");
        
        try
        {
            // Proje kökü
            string projectRoot = Directory.GetCurrentDirectory();
            var engine = new SynScriptEngine(projectRoot);
            
            // Test 1: Basit test scripti
            Console.WriteLine("\n[Test 1] Running main.syn (Simple Test)");
            Console.WriteLine("─────────────────────────────────────");
            string result1 = engine.ExecuteFunction("test_synscript");
            Console.WriteLine($"Output: {result1}\n");
            
            // Test 2: Karakter kontrolcüsü örneği
            string characterScriptPath = Path.Combine(projectRoot, "../../SynScript/Examples/character_controller.syn");
            if (File.Exists(characterScriptPath))
            {
                Console.WriteLine("\n[Test 2] Running character_controller.syn (Advanced Test)");
                Console.WriteLine("─────────────────────────────────────");
                string result2 = engine.ExecuteFunction("test_character", characterScriptPath);
                Console.WriteLine($"Output: {result2}\n");
            }
            
            // Validation test
            Console.WriteLine("\n[Validation] Checking syntax...");
            Console.WriteLine("─────────────────────────────────────");
            engine.ValidateSynScript(Path.Combine(projectRoot, "main.syn"));
            
            Console.WriteLine("\n╔═══════════════════════════════════════╗");
            Console.WriteLine("║   All tests completed successfully!    ║");
            Console.WriteLine("╚═══════════════════════════════════════╝");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"\n[FATAL ERROR]: {ex.Message}");
            if (ex.InnerException != null)
            {
                Console.WriteLine($"[INNER ERROR]: {ex.InnerException.Message}");
            }
        }
    }
}
