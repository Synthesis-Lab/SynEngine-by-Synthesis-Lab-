# 👥 SynEngine Team Guide - Phase 1 Tamamlama 

## 🎉 Tebrikler! Phase 1 başarıyla tamamlandı.

Bu belge, ekibin **Phase 2 (Godot Entegrasyonu)** için hazırlanmasına yardımcı olur.

---

## 🎯 Mevcut Durum

### Neler Yapıldı? ✅

| Konu | Dosyalar | Durum |
|------|----------|-------|
| **SynScript Dili** | `SynScript/Grammar/SynScript.g4` | ✅ Completeş |
| **Standart Lib** | `SynScript/StdLib/*.py` | ✅ 40+ fonk. |
| **Transpiler** | `SynEngine.Core/Class1.cs` | ✅ Çalışıyor |
| **IDE Desteği** | `SynScript/vscode/` | ✅ Highlight + Snippets |
| **Dokümentasyon** | `PHASE1_COMPLETION_REPORT.md` | ✅ Detaylı |

### Ekip Rollerine Göre Önerileri

---

## 👨‍💻 Python Uzmanları (3 kişi önerilir)

### Şu An Yapabileceğiniz İşler

#### 1️⃣ StdLib Extensions (Kolay)
```python
# SynScript/StdLib/ içine yeni modüller ekle

# Örnek: synphysics.py
class SynRigidbody:
    def apply_force(self, force: Vector2):
        self.velocity += force / self.mass
    
    def check_collision(self, other) -> bool:
        return self.bounds.intersects(other.bounds)

# Örnek: synaudio.py
class SynAudioPlayer:
    def play_sound(self, sound_path: str, volume: float = 1.0):
        pass
    
    def play_music(self, music_path: str, loop: bool = True):
        pass
```

**Dosyalar**: 
- `SynScript/StdLib/synphysics.py` (yeni)
- `SynScript/StdLib/synaudio.py` (yeni)
- `SynScript/StdLib/__init__.py` (güncelle)

**Zaman**: 4-6 saat

#### 2️⃣ Unit Tests Yazma (Orta)
```python
# SynScript/StdLib/tests/test_synmath.py
import pytest
from synmath import SynMath

def test_clamp():
    assert SynMath.clamp(150, 0, 100) == 100
    assert SynMath.clamp(-5, 0, 100) == 0
    assert SynMath.clamp(50, 0, 100) == 50

def test_distance():
    dist = SynMath.distance(0, 0, 3, 4)
    assert abs(dist - 5.0) < 0.01  # 3-4-5 üçgeni

def test_lerp():
    result = SynMath.lerp(0, 10, 0.5)
    assert result == 5.0
```

**Dosyalar**:
- `SynScript/StdLib/tests/` (yeni klasör)
- `SynScript/StdLib/tests/test_*.py`

**Zaman**: 6-8 saat

#### 3️⃣ Örnek Oyunlar (Orta-Zor)
```synscript
# SynScript/Examples/
# - snake_game.syn (3 saat)
# - flappy_bird.syn (4 saat)
# - space_invaders.syn (6 saat)
```

**Zaman**: 3-6 saat per oyun

### Phase 2 İçin Hazırlık

1. **Python.NET Öğren**
   ```python
   # Python.NET ile C# kodu çağırmak nasıl yapılır
   import clr
   clr.AddReference("SynEngine.Core")
   from SynEngine.Core import SynScriptEngine
   ```
   
2. **Type Hints Derinlemesine**
   - Mevcut `synvector.py` ve `syncolor.py` incelensin
   - C# generics ile Python type hints entegrasyonunu planlayın

3. **Benchmark Tools**
   - Performance testeri yaz (transpile süresi, runtime)

---

## 🔧 C# Developers (2 kişi önerilir)

### Phase 2'ye Hazırlanma Listesi

#### 1️⃣ Python.NET Setup (Başla)
```csharp
// SynEngine.Core/PythonBridge.cs (PRE-PHASE 2)
using Python.Runtime;

public class GodotPythonBridge
{
    private IntPtr _pythonGIL;
    
    public void Initialize()
    {
        PythonEngine.Initialize();
        _pythonGIL = PythonEngine.AcquireLock();
    }
    
    public object ExecuteInMemory(string pythonCode)
    {
        // Subprocess yerine bellek içinde çalıştır
        using (Py.GIL())
        {
            return PyModule.FromString("synscript", pythonCode);
        }
    }
    
    public void Shutdown()
    {
        PythonEngine.ReleaseLock(_pythonGIL);
        PythonEngine.Shutdown();
    }
}
```

**Zaman**: 3-4 saat araştırma

#### 2️⃣ Godot C# API Wrapper (Başlangıç)
```csharp
// SynEngine.Godot/SynActor.cs (YENİ)
using Godot;

public partial class SynActor : Node2D
{
    // Godot Node özelliklerini Python tarafında expose et
    private Dictionary<string, object> _exportedProperties = new();
    
    public void SetExportedProperty(string name, object value)
    {
        _exportedProperties[name] = value;
    }
    
    public void CallSynScript(string methodName)
    {
        // Python fonksiyonunu çağır
    }
}
```

**Dosya**: `SynEngine.Godot/SynActor.cs` (yeni proje)

#### 3️⃣ Benchmarking Tools
```csharp
// SynEngine.Tools/PerformanceProfiler.cs
public class PerformanceProfiler
{
    public TimeSpan MeasureTranspilation(string synscriptPath)
    {
        var sw = Stopwatch.StartNew();
        // Transpile...
        sw.Stop();
        return sw.Elapsed;
    }
}
```

**Zaman**: 2-3 saat

### Öğrenme Kaynakları
- [Godot C# API](https://docs.godotengine.org/en/stable/tutorials/scripting/c_sharp/index.html)
- [Python.NET Documentation](https://pythonnet.github.io/)
- [LINQ & Generics](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/generics)

---

## 📱 Tüm Ekip

### Şu Hafta Yapılacak Görevler

| Görev | Sorumlu | Süresi | Deadline |
|-------|---------|--------|----------|
| StdLib physics module | Python Team | 6h | Tomorrow |
| Unit tests yazı | Python Team | 6h | This week |
| Python.NET araştırması | C# Team | 4h | Today |
| Godot API wrapper sketch | C# Team | 4h | This week |
| Documentation review | All | 2h | This week |

### Daily Standup Format

```
🔵 Python Team:
- Completed: X, Y, Z
- Blocked: [if any]
- Next: A, B, C

🔵 C# Team:
- Completed: X, Y, Z
- Blocked: [if any]
- Next: A, B, C
```

### Code Review Checklist

```python
# SynScript/StdLib/sunewmodule.py review
- [ ] Docstrings mevcut
- [ ] Type hints tam
- [ ] Unit tests yazılıyor
- [ ] Performance test geçiyor
- [ ] Python 3.8+ uyumlu
```

---

## 🎓 Hazırlanma Kaynakları

### Dış Kaynaklar
1. **Python.NET Getting Started**
   https://pythonnet.github.io/

2. **Godot 4 C# Scripting**
   https://docs.godotengine.org/en/stable/tutorials/scripting/c_sharp

3. **ANTLR 4 Parser Toolkit**
   https://www.antlr.org/

### İç Kaynaklar
- `SynScript/LANGUAGE_SPEC.md` - Dil tanımı
- `PHASE1_COMPLETION_REPORT.md` - Mevcut durum
- `MASTER_ROADMAP.md` - Detaylı plan

---

## 🔍 Kod Review Prosesi

Tüm PR'lar şunları içермeli:

```markdown
## PR Description
- [ ] Feature nedir?
- [ ] Neden gerekli?
- [ ] Test edilmiş mi?

## Checklist
- [ ] Code style (PEP8 for Python, Microsoft style for C#)
- [ ] Docstrings/Comments
- [ ] Tests (>80% coverage)
- [ ] No security issues
- [ ] Performance benchmarks (if applicable)

## Performance Impact
- Transpile time: ~5ms
- Memory usage: ~10MB
```

---

## 🚀 Phase 2 Timeline

```
Week 1: Setup & Prototyping
├── Python.NET environment setup
├── Godot C# scaffolding
└── Basic bridge POC

Week 2: Core Development
├── SynActor implementation
├── Property binding
└── Signal mapping

Week 3: Integration & Testing
├── End-to-end tests
├── Performance optimization
└── Example games

Week 4: Polish & Documentation
├── Code documentation
├── API documentation
└── Release preparation
```

---

## 📞 İletişim

### Meeting Schedule
- **Daily Standup**: 10:00 AM (15 min)
- **Code Review**: Tuesday 14:00 (30 min)
- **Technical Discussion**: Friday 15:00 (45 min)

### Channels
- **Discord**: `#synengine-dev`
- **GitHub**: Issues & Discussions
- **Email**: team@synengine.io

---

## ✅ Checklist for Next Phase

### Tamamlanmadan Önce
- [ ] Tüm Phase 1 görevlerini inceledim
- [ ] `LANGUAGE_SPEC.md` okudum
- [ ] StdLib modüllerine göz attım
- [ ] Kodlama standartlarını anladım

### Phase 2'ye Başlamak İçin
- [ ] Python.NET kurdum
- [ ] Godot 4 (.NET sürümü) kurdum
- [ ] Geliştirme ortamını setup ettim
- [ ] Testleri çalıştırabilirim

---

## 🎉 Başarı Sözcükleri

> "Phase 1, bir oyun motorsunun temelini attı. Phase 2 ile onu gerçek hayata söndüreceğiz." - Team Lead

Emeğiniz için teşekkürler! 🙏

---

**Sorular mı? GitHub Discussions'ta sorabilirsiniz!**

**UPDATED**: 5 March 2026  
**Next Review**: 12 March 2026
