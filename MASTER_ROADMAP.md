# 🎮 SynEngine - Master Roadmap & Vision

**Synthesis Lab tarafından geliştirilen hibrit oyun motoru**

---

## 🎯 Vision Statement

SynEngine, **oyun geliştiricilerin hızlı prototip yapması ve üretken olması** için tasarlanmış bir oyun motor ekosistemidir. **Unified SynScript dili** ile yazılan oyunlar, platform-spesifik derleyiciler aracılığıyla farklı motorlarda çalışır.

**Çift Sürüm Mimarisi**:
- 🏗️ **SynEngine Studio** (Amiral gemisi): Godot destekli, C#/C++ runtime, masaüstü
- 🚀 **SynEngine GO** (Spin-off): Cocos destekli, Java/Kotlin runtime, çapraz-platform

### Hedef Kullanıcılar
- 🎓 Oyun geliştirme öğrencileri ve öğretmenler
- 👨‍💻 Bağımsız oyun geliştiricileri
- 🎮 Mobil oyun geliştiricileri
- 🎨 Oyun tasarımcıları (düşük kod gerekliliği)
- 📚 Eğitim kurumları ve bootcamp'lar

---

## � SynScript Dil Stratejisi

### **Unified Syntax, Multiple Variants**

SynScript tek bir **base syntax** ile yazılır, ancak target motor'a göre farklı runtime'lara derlenir:

#### **Python Variant** (Studio - Godot)
```synscript
# Studio için: Python-benzeri, statik tiplemesi güçlü
var player_speed: float = 150.0
var health: int = 100

signal health_changed(old: int, new: int)

state Moving:
    fn on_enter():
        print("Player moving...")
    
    fn tick(delta: float):
        # Performance: @vector. kullan
        position = @vector.add(position, velocity * delta)
    
    fn on_exit():
        velocity = Vector2(0, 0)

# Python runtime compile -> Godot executes
```

**Özellikleri**:
- ✅ Python-like syntax (indentation, def-like)
- ✅ Strong type hints (`var x: Type`)
- ✅ State Machine 1st-class (built-in `state`)
- ✅ Signal/Slot (event system)
- ✅ @operator namespace (performance ops)
- ✅ **Runtime**: Python → C# → Godot

---

#### **JavaScript Variant** (GO - Cocos)
```synscript
// GO için: JavaScript-benzeri, dinamik tiplemesi esnek
let playerSpeed = 150.0;  // Type inference
let health = 100;

signal healthChanged(old, new);

state Moving {
    onEnter() {
        console.log("Player moving...");
    }
    
    tick(delta) {
        // Performance: @vector. kullan
        this.position = @vector.add(this.position, this.velocity.scale(delta));
    }
    
    onExit() {
        this.velocity = new Vector2(0, 0);
    }
}

// JavaScript emit -> TypeScript compile -> Cocos executes
```

**Özellikleri**:
- ✅ JavaScript-like syntax (semi-colon, let/const)
- ✅ Type hints optional (inference)
- ✅ State Machine 1st-class (blocks instead of indent)
- ✅ Signal/Slot (event system)
- ✅ @operator namespace (performance ops)
- ✅ **Runtime**: TypeScript → JavaScript → Cocos

---

### **Cross-Variant Features** (Both)
- ✅ Same base game concepts (State, Signal, Actor)
- ✅ Same standard library API
- ✅ Interchangeable syntax education (learn one, understand both)
- ✅ Code migration tools (Python ↔ JavaScript transpiler planned)

---

## �📊 3 Aşamalı Geliştirme Planı (Studio → GO)

> **Strateji**: Amiral gemisi sürümü (Studio) tam olgunlaştıktan sonra, GO sürümü spin-off olarak başlatılacaktır.

### **Phase 1: SynScript Dili Olgunlaştırma** ✅ TAMAMLANDI

**Hedefi**: Oyun geliştirmeye özgü bir programlama dili oluşturmak (Python Variant)

> **Not**: Phase 1'de Python variant oluşturuldu. Phase 3'te JavaScript variant eklenecektir.

| Görev | Durum | Tamamlama | Saatler |
|-------|-------|-----------|---------|
| ANTLR Gramer | ✅ | 100% | 4h |
| StdLib (4 modül) | ✅ | 100% | 8h |
| Transpiler | ✅ | 100% | 6h |
| Error Handling | ✅ | 100% | 4h |
| VS Code Extension | ✅ | 100% | 4h |
| Dokümantasyon | ✅ | 100% | 3h |

**Çıktılar**:
- ✅ ANTLR 4 Grammar (`SynScript.g4`)
- ✅ 40+ Standart Library fonksiyonu
- ✅ SynScript → Python Transpiler
- ✅ VS Code Syntax Highlighting
- ✅ 15+ Code Snippets

**Başlanılan**: 5 Mart 2026  
**Tamamlanan**: 5 Mart 2026  
**Süre**: 1 gün

---

### **Phase 2: Godot Entegrasyonu** ⏳ SIRADA

**Hedefi**: SynScript'i Godot motorunun üzerine kurmak

#### 2.1 Python.NET In-Memory Bridge

```csharp
// Hedef: Python kodu subprocess yerine bellek içinde çalışması
var pythonEngine = new GodotPythonBridge();
var scriptResult = pythonEngine.ExecuteInMemory(synscriptCode);
```

**Görevler**:
- [ ] Python.NET setup (Windows/Linux/Mac)
- [ ] Godot C# API wrapper
- [ ] GIL (Global Interpreter Lock) yönetimi
- [ ] Memory leak prevention
- [ ] Performance benchmarking

**Tahmini**: 24 saat çalışma

#### 2.2 SynActor - Node Wrapper

```synscript
class PlayerCharacter extends SynActor:
    @export
    var speed: float = 150.0
    
    @on_ready
    function _ready():
        print("Player loaded!")
    
    @process
    function _process(delta: float):
        self.position += Input.direction() * speed * delta
```

**Görevler**:
- [ ] SynActor base sınıfı
- [ ] Property binding (C# ↔ Python)
- [ ] Signal to decorator mapping
- [ ] Godot input system integration
- [ ] Node hierarchy support

**Tahmini**: 16 saat çalışma

#### 2.3 Inspector Integration

```plaintext
[Inspector Panel]
┌─ PlayerCharacter
│  ├─ speed: 150.0 [Exported]
│  ├─ health: 100 [Exported]
│  └─ max_health: 100 [Exported]
└─ Methods
   ├─ take_damage()
   └─ heal()
```

**Görevler**:
- [ ] Inspector drawer plugin
- [ ] Type conversion (Python ↔ C#)
- [ ] Hot reload desteği
- [ ] Debug visualization

**Tahmini**: 12 saat çalışma

**Phase 2 Toplam Tahmini**: 52 saat = 1.5 hafta

---

### **Phase 3: Cocos (Çapraz-Platform) Entegrasyonu - SynEngine GO** 🧊 PLANLAMADA

**Hedefi**: SynScript'i Cocos Engine üzerinde masaüstü, mobil ve web'de çalıştırmak

#### 3.1 Java/Kotlin Cocos Runtime

```kotlin
// SynEngine GO - Cocos Engine + Java/Kotlin
public class SynEngineGO {
    private val cocosEngine = CocosGame()
    private val synCompiler = SynScriptCompiler()
    
    fun compileAndRun(synScript: String) {
        val jsCode = synCompiler.transpileToJavaScript(synScript)
        cocosEngine.executeScript(jsCode)
    }
}
```

**Strategi**:
- Cocos Creator 3.x (official runtime)
- Java/Kotlin JVM wrapper
- SynScript → TypeScript/JavaScript transpiler
- Cross-platform deployment (Desktop, Mobile, Web)

**Görevler**:
- [ ] Cocos Creator C++ binding yapma
- [ ] SynScript → TypeScript transpiler
- [ ] JVM Cocos wrapper yazma
- [ ] Android NDK integration
- [ ] WebGL support setup

**Tahmini**: 36 saat çalışma

#### 3.2 Çapraz-Platform Build Pipeline

```bash
# Masaüstü (Windows/macOS/Linux)
synengine-go build --target=desktop game.syn

# Mobil (iOS/Android)
synengine-go build --target=mobile --os=android game.syn
synengine-go build --target=mobile --os=ios game.syn

# Web
synengine-go build --target=web game.syn
# Çıkış: dist/desktop/, dist/android/, dist/ios/, dist/web/
```

**Görevler**:
- [ ] Gradle build system integration
- [ ] Asset bundling (platform-specific)
- [ ] Code signing (iOS/Android)
- [ ] WebGL building
- [ ] Performance optimization per platform

**Tahmini**: 28 saat çalışma

#### 3.3 UI Framework (JavaFX + Mobile)

```kotlin
// Shared SynScript UI Components
@SynComponent
class GameButton : CocosNode {
    override fun onEngine(renderGame: CocosGame) {
        // Otomatik tema ve responsive tasarım
    }
}
```

**Tahmini**: 20 saat çalışma

**Phase 3 Toplam Tahmini**: 84 saat = 2.5 hafta

---

### **Phase 4: IDE & Ekosistem Tamamlama (Her İki Sürüm İçin)** 🧊 SONRASI

**Hedefi**: Profesyonel geliştirme deneyimi sağlamak

#### 4.1 Language Server Protocol (LSP)

```json
{
  "method": "textDocument/hover",
  "params": {
    "textDocument": "game.syn",
    "position": {"line": 5, "character": 10}
  },
  "result": "function calculate_damage(base: int) -> int"
}
```

**Görevler**:
- [ ] LSP server yazma (C#)
- [ ] Intellisense implementation
- [ ] Go-to-definition
- [ ] Find-references
- [ ] Rename refactoring

#### 4.2 Visual Scripter

```
┌─────────────────────────────────────────┐
│   Visual SynScript Editor               │
├─────────────────────────────────────────┤
│  [Variable] ──→ [If Statement] ──→ [Print] │
│                      ↓                   │
│                [Loop Block]              │
│                      ↓                   │
│              [Function Call]             │
└─────────────────────────────────────────┘
```

Drag-and-drop script editor oluşturmak

**Görevler**:
- [ ] Node-based editor UI
- [ ] Code-to-visual sync
- [ ] Visual-to-code transpile
- [ ] Template library

#### 4.3 Package Manager

```bash
syn install phaser-extensions
syn install godot-plugins
syn publish my-game-library
```

**Tahmini**: 40+ saatler

---

## 📈 Proje İstatistikleri

### SynEngine Studio (Godot + C#/C++)
| Metrik | Şu Anki | Phase 2 Hedef | Phase 4 Hedef |
|--------|---------|--------------|---------------|
| **Kod Satırı (Python)** | 550 | 3000+ | 5000+ |
| **Kod Satırı (C#/C++)** | 300 | 2000+ | 4000+ |
| **StdLib Fonksiyonları** | 40 | 80+ | 150+ |
| **Platformlar** | 1 (Desktop) | 3 (Win/Mac/Linux) | 3 (Win/Mac/Linux) |
| **IDE Integration** | VS Code | VS Code + Godot | VS Code + Godot + LSP |

### SynEngine GO (Cocos + Java/Kotlin)
| Metrik | Phase 3 Başlangıç | Phase 3 Hedef | Phase 4 Hedef |
|--------|------------------|---------------|---------------|
| **Kod Satırı (JavaScript)** | 0 | 2500+ | 5000+ |
| **Kod Satırı (Java/Kotlin)** | 0 | 1500+ | 3000+ |
| **StdLib Fonksiyonları** | - | 80+ | 150+ |
| **Platformlar** | - | 5 (Win/Mac/Linux/iOS/Android/Web) | 5+ (same + variations) |
| **IDE Integration** | - | Android Studio + VS Code | Android Studio + VS Code + Web IDE |

---

## 🛠️ Technology Stack

### **SynEngine Studio (Amiralgemisi)**

**Frontend (Editor)**:
- VS Code Extension API
- TypeScript/JavaScript
- Godot Editor integration
- Custom C#/C++ plugin SDK

**Backend (Transpiler - Python Variant)**:
- C# + .NET 10.0
- C++ (performans kritik kısımlar)
- ANTLR 4 (Parser)
- Python 3.8+ → C# → Python bridge

**Runtime (Engine)**:
- Godot 4.x Engine (.NET edition)
- Python.NET (C# ↔ Python IPC)
- Desktop platforms (Windows/macOS/Linux)

---

### **SynEngine GO (Spin-off)**

**Frontend (Editor)**:
- Android Studio SDK
- VS Code Extension API
- Browser-based Web IDE
- Multi-platform UI components (JavaFX)

**Backend (Transpiler - JavaScript Variant)**:
- Java 17+
- Kotlin 1.8+
- ANTLR 4 (Parser)
- SynScript → TypeScript/JavaScript transpiler

**Runtime (Engine)**:
- Cocos Creator 3.x
- JVM (Java/Kotlin runtime)
- WebGL support
- Android NDK (native performance)

**Deployment**:
- Desktop: Java executable
- Mobile: Android APK/iOS IPA
- Web: HTML5/WebGL

---

### **Shared Tools**
- Git + GitHub
- Gradle + Maven (Java build)
- Dotnet CLI (C# build)
- Docker (cross-platform testing)
- GitHub Actions CI/CD

---

## 💰 İnsan Gücü & Zaman Tahmini

### **Studio Takım Yapısı (Phase 1-2)**
```
SynEngine Studio Development Team
├── 1 Language Designer (ANTLR, Dual-syntax SynScript)
├── 2 C#/.NET Developer (Godot + Python.NET)
├── 1 C++ Developer (Performance critical)
├── 1-2 Frontend Developer (VS Code ext)
├── 1 DevOps Engineer
└── 1 Technical Writer
```

### **GO Takım Yapısı (Phase 3, Studio'dan sonra)**
```
SynEngine GO Development Team
├── 1 Java/Kotlin Developer (Cocos runtime)
├── 1 Android Developer (Mobile optimization)
├── 1 Web Developer (WebGL/TypeScript)
├── 1 Frontend Developer (Android Studio UI)
└── 1 QA Engineer (Cross-platform testing)
```

### **Zaman Tahmini**
**Studio (Amiral gemisi)**:
- Phase 1 (Dil): ✅ 1 gün = 29 saat
- Phase 2 (Godot): ⏳ 1.5 hafta = 52 saat
- Phase 4 (IDE/Ecosystem): 🧊 2.5 hafta = 100+ saat
- **Studio Toplam**: ~5 hafta = 181+ saat

**GO (Spin-off, Studio'dan sonra başlar)**:
- Phase 3 (Cocos): 🧊 2.5 hafta = 84 saat
- Phase 4 (IDE/Ecosystem): 🧊 2 hafta = 80+ saat
- Testing & Docs: 🧊 1 hafta = 40 saat
- **GO Toplam**: ~5.5 hafta = 204+ saat

**Genel Toplam**: ~10.5 hafta = 385+ saat (iki sürüm paralel geliştirme için 6-7 haftaya düşebilir)

---

## 🎓 Eğitim Hedefleri

### Yazabilecekleri Oyunlar
- ✅ 2D Platformer
- ✅ Top-Down RPG
- ✅ Puzzle Game
- ✅ Match-3 Oyunu
- ✅ Fighting Game
- ✅ Multiplayer Card Game

### Öğrenecekleri Konseptler
1. **Programming**: Variables, functions, OOP, functional programming
2. **Game Development**: Sprites, physics, collision, input, animations
3. **Architecture**: Design patterns, state machines, networking
4. **Tools**: Version control, debugging, performance profiling

---

## 🌍 Community & Monetization Vizyonu

### Phase 1-3 Tamamlandığında
- ✅ Open source yayınla (MIT license)
- ✅ GitHub Actions CI/CD
- ✅ Community contributions accept et
- ✅ Discord/Forum support

### Gelir Kaynakları (İsteğe Bağlı)
1. **Godot Asset Store**: Premium templates + games
2. **Udemy/Skillshare**: Video tutorials
3. **Patreon**: Monthly supporters
4. **Enterprise License**: Şirketler için özel destek

---

## ✅ Başarı Kriterleri

### **Phase 1 Tamamlanmış**:
- [x] SynScript dili resmen tanımlandı (Python variant)
- [x] StdLib yazıldı (4 modül, 40+ fonksiyon)
- [x] Transpiler çalışıyor (Regex → ANTLR)
- [x] VS Code desteği var (syntax, snippets, theme)
- [x] Dokümantasyon tam

### **Phase 2 Hedefleri (Studio - Godot)**:
- [ ] Godot'da SynScript (Python variant) çalışıyor
- [ ] Export variables Editor'de görünüyor
- [ ] 5+ örnek oyun var (Godot)
- [ ] Performance acceptable (<10ms transpile)
- [ ] Python.NET bridge stable
- [ ] Hot reload desteği

### **Phase 3 Hedefleri (GO - Cocos)**:
- [ ] Cocos'da SynScript (JavaScript variant) çalışıyor
- [ ] Masaüstü, mobil (iOS/Android), web'de deploy edebiliyor
- [ ] Android Studio integration
- [ ] 5+ örnek oyun var (iOS/Android/Web)
- [ ] Performance accepted (mobile 60fps)
- [ ] Asset management system

### **Phase 4 Hedefleri (Her İki Sürüm)**:
- [ ] 2000+ GitHub stars
- [ ] 300+ Discord members
- [ ] 100+ community games published (50+ Studio, 50+ GO)
- [ ] LSP server production-ready
- [ ] Official asset store açık
- [ ] Kurumsal destek (Godot/Cocos foundation)

---

## 🚀 Hızlı Başlangıç (Kullanıcı Için)

```bash
# 1. SynEngine'i yükle
npm install -g synengine
# veya
curl https://installer.synengine.io | bash

# 2. Yeni oyun projesi oluştur
synengine create my-game --godot

# 3. IDE'yi aç
synengine code my-game

# 4. Betiği yaz
# my-game/player.syn
@export
var speed = 150.0

function move(input: Vector2, delta: float):
    position += input * speed * delta

# 5. Çalıştır (Godot editöründe)
synengine run

# 6. Web'e yayınla
synengine build --target=web
synengine deploy --hosting=itch.io
```

---

## 🔐 Lisans & İP

- **SynScript Dili**: Apache-2.0 license (Synthesis Lab)
- **Standart Kütüphane**: Apache-2.0 license
- **Örnek Oyunlar**: CC-BY 4.0 (eğitim amaçlı)
- **Telif Hakları**: © 2026 Synthesis Lab

---

## 📞 İletişim & Destek

- **GitHub**: https://github.com/synthesis-lab/synengine
- **Discord**: https://discord.gg/synengine
- **Docs**: https://docs.synengine.io
- **Email**: team@synengine.io
- **Twitter**: @SynEngineDev

---

## 🎉 Kapanış

**SynEngine, oyun geliştirmeyi herkes için erişilebilir kılan bir vizyontur.**

Python'un basitliği ve C#'ın gücünü birleştirerek, şu anda Godot ve Phaser'da çalışacak, gelecekte tüm platformları destekleyecek bir ekosistem inşa ediyoruz.

**Bugün yola çıktık, yarın dünyayı değiştireceğiz. 🚀**

---

**Son Güncelleme**: 5 Mart 2026  
**Rapor Numarası**: SynEngine-2026-Q1-Master  
**Hazırlayan**: Synthesis Lab Engineering Team
