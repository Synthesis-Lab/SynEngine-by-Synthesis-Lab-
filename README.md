# 🎮 SynEngine - The Hybrid Game Engine

**Synthesis Lab tarafından geliştirilmekte olan bir oyun motoru.**

> **Godot ile desteklenen, C# ile yazılan, SynScript (Python-like) dilinde betiklenen oyun motoru.**

---

## 📊 Proje Durumu

| Aşama | Durum | İlerleme |
|-------|-------|----------|
| **Phase 1: SynScript Dili** | ✅ TAMAMLANDI | 100% |
| **Phase 2: Godot Entegrasyonu** | ⏳ SIRADET | 0% |
| **Phase 3: Phaser (Web)** | 🧊 PLANLAMADA | 0% |
| **Phase 4: IDE & Ekosistem** | 🧊 PLANLAMADA | 0% |

**Son Güncelleme**: 5 Mart 2026

---

## 🎯 Vision

SynEngine, oyun geliştiricilerin **hızlı prototip yapması ve produktif olması** için tasarlanmış bir oyun motorudur. 

- 🐍 **Python'un Kolaylığı**: SynScript dili Python-friendly
- 💪 **C#'ın Gücü**: .NET 10.0 ile high-performance
- 🎮 **Godot Desteği**: Desktop oyunları için
- 🌐 **Phaser Desteği**: Web oyunları için
- 📚 **Eğitim Dostu**: Başlangıçtan ileri seviyeye

---

## 🚀 Hızlı Başlangıç

### Phase 1 (SynScript Dili) Özellikleri

```synscript
# SynScript - Oyun geliştiriciler için Python-like dil

@export
var player_health = 100

@export
var player_speed = 150.0

function take_damage(damage: int):
    player_health -= damage
    if player_health <= 0:
        print("Player died!")

function move(direction: Vector2, delta: float):
    position = position + direction * player_speed * delta
```

### Standart Kütüphane

```synscript
# Matematik
var result = SynMath.sin(angle)
var clamped = SynMath.clamp(value, 0, 100)

# Renkler
var red = SynColor.RED()
var custom = SynColor(0.5, 0.8, 0.3)

# Vektörler
var v1 = Vector2(3.0, 4.0)
var distance = v1.distance_to(Vector2(0, 0))

# Timerlar
var timer = SynTimer(2.0, false)
```

---

## 📂 Proje Yapısı

```
SynEngine-by-Synthesis-Lab-/
│
├── 📖 Documentation
│   ├── README.md                    # Bu dosya
│   ├── MASTER_ROADMAP.md            # Detaylı yol haritası
│   ├── PHASE1_COMPLETION_REPORT.md  # Phase 1 raporu
│   └── LICENSE                      # MIT License
│
├── 🔤 SynScript/ (Dil & Kütüphane)
│   ├── Grammar/
│   │   └── SynScript.g4             # ANTLR 4 Grameri
│   ├── StdLib/                      # Standart Kütüphane
│   │   ├── synmath.py               # Matematik (15+ fonk.)
│   │   ├── syncolor.py              # Renk yönetimi
│   │   ├── synvector.py             # 2D/3D vektörler
│   │   └── syntimer.py              # Zaman yönetimi
│   ├── Examples/
│   │   └── character_controller.syn # Örnek oyuncı kontrolcüsü
│   ├── LANGUAGE_SPEC.md             # Dil spesifikasyonu
│   └── vscode/                      # VS Code Plugin
│       ├── package.json
│       ├── language-configuration.json
│       ├── syntaxes/
│       │   └── synscript.tmLanguage.json
│       ├── snippets/
│       │   └── synscript.json
│       └── README.md
│
├── ⚙️ SynEngine.Core/ (C# .NET Runtime)
│   ├── Class1.cs                    # Transpiler + Engine
│   ├── main.syn                     # Test scripti
│   ├── SynEngine.Core.csproj        # Project file
│   └── bin/                         # Compiled binaries
│
└── 🔗 Templates/ (Coming Soon)
    ├── godot-starter/
    ├── phaser-starter/
    └── plugin-template/
```

---

## 🔧 Kurulum & Setup

### Gereksinimler
- .NET 10.0 SDK
- Python 3.8+
- VS Code (opsiyonel, dil desteği için)
- Git

### Windows

```powershell
# Repository'yi klon et
git clone https://github.com/synthesis-lab/synengine
cd synengine

# .NET projesini build et
cd SynEngine.Core
dotnet build
dotnet run
```

### Linux / macOS

```bash
# Repository'yi klon et
git clone https://github.com/synthesis-lab/synengine
cd synengine

# .NET projesini build et
cd SynEngine.Core
dotnet build
dotnet run
```

### VS Code Extension Kurulumu

1. `SynScript/vscode/` klasörünü kopyala:
   ```bash
   cp -r SynScript/vscode ~/.vscode/extensions/synscript-0.1.0/
   ```

2. VS Code'u yeniden başlat

3. `.syn` dosyası oluştur ve test et

---

## 📚 Dokümantasyon

| Belge | İçerik |
|-------|--------|
| [LANGUAGE_SPEC.md](SynScript/LANGUAGE_SPEC.md) | Tam SynScript dil referansı |
| [MASTER_ROADMAP.md](MASTER_ROADMAP.md) | Detaylı geliştirme planı (Phase 1-4) |
| [PHASE1_COMPLETION_REPORT.md](PHASE1_COMPLETION_REPORT.md) | Phase 1 tamamlama raporu |
| [VS Code Extension README](SynScript/vscode/README.md) | IDE kurulum ve kullanım |

---

## 💡 Özellikler

### Phase 1 ✅ (TAMAMLANDI)
- ✅ SynScript dili (gramer, transpiler)
- ✅ Standart kütüphane (40+ fonksiyon)
- ✅ Error handling
- ✅ VS Code syntax highlighting
- ✅ 15+ Code snippets

### Phase 2 ⏳ (SIRADET)
- ⏳ Godot entegrasyonu
- ⏳ Python.NET in-memory bridge
- ⏳ SynActor wrapper
- ⏳ Signal mapping
- ⏳ Inspector integration

### Phase 3 🧊 (PLANLAMADA)
- 🧊 Phaser (Web) entegrasyonu
- 🧊 Brython/Pyodide runtime
- 🧊 JavaScript transpiler
- 🧊 Web asset management

### Phase 4 🧊 (PLANLAMADA)
- 🧊 Language Server Protocol (LSP)
- 🧊 Visual script editor
- 🧊 Package manager
- 🧊 Community marketplace

---

## 🎮 Örnek Kod

### Basit Oyuncu Kontrolcüsü

```synscript
# player.syn - SynScript örneği

@export
var speed: float = 150.0

@export
var jump_force: float = 300.0

var velocity = Vector2(0, 0)

@process
function _process(delta: float):
    # Input alma
    var direction = Input.get_vector("left", "right", "up", "down")
    
    # Hareket
    velocity.x = direction.x * speed
    
    # Yerçekimi
    velocity.y += 600 * delta  # gravity
    
    # Pozisyon güncelle
    position = position + velocity * delta
    
    # Zıplama
    if Input.is_action_pressed("jump"):
        velocity.y = -jump_force

@signal
function on_hit(damage: int):
    print(f"Oyuncu {damage} hasar aldı!")
```

---

## 🧪 Test & Validation

```bash
# Syntax validation
dotnet run validate script.syn

# Execute test function
dotnet run execute script.syn test_function

# Full test suite
dotnet test SynEngine.Core.Tests/
```

---

## 🤝 Katkıda Bulunma

### İyi Başlangıç Konuları
1. **StdLib Genişletmesi**: Yeni matematik/physics fonksiyonları
2. **Örnek Oyunlar**: Kütüphanelerin kullanımı gösteren örnekler
3. **Dokümentasyon**: Türkçe, İngilizce API dökümanları
4. **Tests**: Unit test yazma
5. **Performance**: Profiling ve optimizasyon

### Development Setup

```bash
# Fork ve clone et
git clone https://github.com/YOUR_GITHUB/synengine
cd synengine

# Feature branch oluştur
git checkout -b feature/your-feature

# Değişiklikleri commit et
git commit -am "Add new feature"

# Push et
git push origin feature/your-feature

# Pull request aç
```

**Kontribüsyon Rehberi**: [CONTRIBUTING.md](CONTRIBUTING.md) (Yakında)

---

## 📋 Bilinen Sorunlar

| Sorun | Durum | Fix |
|-------|-------|-----|
| Godot entegrasyonu yok | 🔴 | Phase 2 başlangıcında |
| ANTLR parser derlenmiş durumda değil | 🟡 | İleri sürüm |
| Web desteği eksik | 🔴 | Phase 3 |
| LSP server yok | 🔴 | Phase 4 |

---

## 📊 İstatistikler

```
Phase 1 Tamamlama İstatistikleri:
├── Toplam Kod Satırı: 700+ (Python + C#)
├── StdLib Fonksiyonları: 40+
├── Test Fonksiyonları: 7
├── Geliştirme Süresi: 1 gün
├── VS Code Snippets: 15+
└── Dokümantasyon Sayfaları: 5+
```

---

## 🐛 Hata Bildir

Hata mı buldum? [GitHub Issues](https://github.com/synthesis-lab/synengine/issues) üzerine bildir.

Lütfen içer:
- [ ] Hata açıklaması
- [ ] Tekrar adımları
- [ ] Beklenen vs gerçek davranış
- [ ] SynEngine sürümü

---

## 📝 Lisans

SynEngine MIT License ile lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bak.

```
MIT License (c) 2026 Synthesis Lab
```

---

## 🎯 Roadmap Özeti

```
2026 Q1: Phase 1 ✅ DONE - SynScript dili + StdLib
2026 Q2: Phase 2 ⏳ TODO - Godot entegrasyonu
2026 Q3: Phase 3 🧊 PLAN - Web (Phaser) desteği
2026 Q4: Phase 4 🧊 PLAN - IDE & Ekosistem
```

---

## 💬 Topluluk

- **Discord**: https://discord.gg/synengine
- **GitHub Discussions**: https://github.com/synthesis-lab/synengine/discussions
- **Twitter**: [@SynEngineDev](https://twitter.com/SynEngineDev)
- **Email**: team@synengine.io

---

## 🙏 Teşekkürler

- **Godot Foundation** - Harika oyun motoru
- **Python Software Foundation** - Python dilinin harika tasarımı  
- **ANTLR Project** - Parser generator
- **Synthesis Lab Team** - SynEngine'in kurucuları

---

**SynEngine: Oyun Geliştirmeyi Herkes İçin Erişilebilir Kıl 🚀**

Detaylı yol haritası için [MASTER_ROADMAP.md](MASTER_ROADMAP.md) bak.

**UPDATED**: 5 March 2026
