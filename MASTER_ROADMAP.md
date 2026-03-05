# 🎮 SynEngine - Master Roadmap & Vision

**Synthesis Lab tarafından geliştirilen hibrit oyun motoru**

---

## 🎯 Vision Statement

SynEngine, **oyun geliştiricilerin hızlı prototip yapması ve üretken olması** için tasarlanmış bir oyun motorudur. Python'un kolaylığıyla C#'ın gücünü birleştirerek, **Godot (desktop), Phaser (web), ve custom runtimes** üzerinde çalışır.

### Hedef Kullanıcılar
- 🎓 Oyun geliştirme öğrencileri
- 👨‍💻 İndie oyun geliştiriciler
- 🎨 Game designers (kod bilmeyen)
- 📚 Eğitim kurumları

---

## 📊 4 Aşamalı Geliştirme Planı

### **Phase 1: SynScript Dili Olgunlaştırma** ✅ TAMAMLANDI

**Hedefi**: Oyun geliştirmeye özgü bir programlama dili oluşturmak

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

### **Phase 2: Godot Entegrasyonu** ⏳ SIRADET

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

### **Phase 3: Phaser (Web) Entegrasyonu** 🧊 PLANLAMADA

**Hedefi**: SynScript'i tarayıcıda çalıştırmak (WebAssembly)

#### 3.1 Brython Runtime Setup

```html
<!-- Web oyunu için SynScript -->
<script src="brython.js"></script>
<script src="synscript-runtime.js"></script>
<script type="text/python">
    from syn import *
    
    @export
    class PhaserGame(Game):
        def create(self):
            print("Phaser game created!")
</script>
```

**Strategi**:
- Brython (Python → JavaScript transpiler)
- Pyodide (WebAssembly Python runtime)
- Phaser.js JavaScript library

**Görevler**:
- [ ] Brython/Pyodide araştırması
- [ ] SynScript → JavaScript transpiler
- [ ] Phaser wrapper kütüphanesi
- [ ] Asset loaderı
- [ ] Performance optimization

**Tahmini**: 24 saat çalışma

#### 3.2 Build Pipeline

```bash
# SynScript → Web
synengine build --target=web --framework=phaser game.syn
# Çıkış: dist/index.html, game.js, assets/
```

**Görevler**:
- [ ] Build system (webpack/vite)
- [ ] Asset bundling
- [ ] Minification
- [ ] Source maps

**Tahmini**: 16 saat çalışma

**Phase 3 Toplam Tahmini**: 40 saat = 1 hafta

---

### **Phase 4: IDE & Ekosistem Tamamlama** 🧊 SONRASI

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

| Metrik | Şu Anki | Hedef |
|--------|---------|-------|
| **Kod Satırı (Python)** | 400 | 2000+ |
| **Kod Satırı (C#)** | 300 | 1500+ |
| **StdLib Fonksiyonları** | 40 | 100+ |
| **Desteklenen Platformlar** | 1 (Desktop) | 3 (Desktop, Web, Mobile) |
| **IDE Integration** | VS Code | VS Code + Godot |
| **Community Contributors** | 0 | 20+ |

---

## 🛠️ Technology Stack

### **Frontend (Editor)**
- VS Code Extension API
- TypeScript/JavaScript
- HTML5/CSS3

### **Backend (Transpiler)**
- C# + .NET 10.0
- ANTLR 4 (Parser)
- Python 3.14+

### **Runtime (Engine)**
- Godot 4.x (.NET sürümü)
- Phaser 3.x (Web)
- Python.NET (IPC bridge)

### **Tools**
- Git + GitHub
- Docker (cross-platform testing)
- CMake (build system)

---

## 💰 İnsan Gücü & Zaman Tahmini

### **Takım Yapısı Önerisi**
```
SynEngine Development Team
├── 1-2 Language Designer (ANTLR, Python)
├── 2-3 C#/.NET Developer (Godot integration)
├── 1-2 Frontend Developer (VS Code ext, UI)
├── 1 DevOps/QA Engineer
└── 1 Technical Writer
```

### **Zaman Tahmini**
- **Phase 1** (Dil): ✅ 1 gün = 29 saat
- **Phase 2** (Godot): ⏳ 1.5 hafta = 52 saat
- **Phase 3** (Web): 🧊 1 hafta = 40 saat
- **Phase 4** (IDE): 🧊 2-3 hafta = 80+ saat
- **Testing & Docs**: 🧊 1 hafta = 40 saat
- **Toplam**: ~9 hafta = 241+ saat

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

**Phase 1 Tamamlanmış**:
- [x] SynScript dili resmen tanımlandı
- [x] StdLib yazıldı (40+ fonksiyon)
- [x] Transpiler çalışıyor
- [x] VS Code desteği var

**Phase 2 Hedefleri**:
- [ ] Godot'da SynScript çalışıyor
- [ ] Export variables Editor'de görünüyor
- [ ] 5 example game var (Godot)
- [ ] Performance ✅ acceptable (<10ms transpile)

**Phase 3 Hedefleri**:
- [ ] Web oyunları SynScript'te yazılabiliyor
- [ ] Phaser framework fully wrapped
- [ ] 3 example game var (Web)
- [ ] Package size < 5MB

**Phase 4 Hedefleri**:
- [ ] 1000+ GitHub stars
- [ ] 100+ Discord members
- [ ] 50+ community games published
- [ ] LSP server stable ve production ready

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

- **SynScript Dili**: MIT License (Synthesis Lab)
- **Standart Kütüphane**: MIT License
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
