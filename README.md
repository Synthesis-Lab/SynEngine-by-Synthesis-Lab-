# 🎮 SynEngine - The Hybrid Game Engine

**Synthesis Lab tarafından geliştirilmekte olan bir oyun motoru.**

> **Godot ile desteklenen, C# ile yazılan, SynScript (Python-like) dilinde betiklenen oyun motoru.**

---

## 📊 Proje Durumu

| Aşama | Durum | İlerleme |
|-------|-------|----------|
| **Phase 1: SynScript v0.2.0** | ✅ TAMAMLANDI | 100% |
| **Phase 2: Godot Entegrasyonu** | ⏳ SIRADA | 0% |
| **Phase 3: Phaser (Web)** | 🧊 PLANLANIYOR | 0% |
| **Phase 4: IDE & Ekosistem** | 🧊 PLANLANIYOR | 0% |

**Son Güncelleme**: 6 Mart 2026  
**Sürüm**: v0.2.0 - State Machine, Signal/Slot, @Operators

---

## 🎯 Vision

SynEngine, oyun geliştiricilerin **hızlı prototip yapması ve produktif olması** için tasarlanmış bir oyun motorudur. 

- 🎮 **State Machine First**: Oyun mantığı için built-in State deseni
- 📡 **Signal/Slot Events**: Deklaratif event binding (`=>` operatörü)
- ⚡ **@Operator Namespace**: Performans kritik işlemler için native operators  
- 🐍 **Python'un Kolaylığı**: SynScript dili Python-friendly
- 💪 **C#'ın Gücü**: .NET 10.0 ile high-performance
- 🎮 **Godot Desteği**: Desktop oyunları için
- 🌐 **Phaser Desteği**: Web oyunları için
- 📚 **Eğitim Dostu**: Başlangıçtan ileri seviyeye

---

## 🚀 Hızlı Başlangıç

### Phase 1 v0.2.0 Özellikleri

```synscript
# SynScript - Oyun geliştiriciler için Hibrid dil

# ===== State Machine Pattern =====
@export
var current_state = "Idle"

state Idle:
    fn on_enter():
        animation.play("idle_animation")
    
    fn tick(delta: float):
        if input.is_pressed("attack"):
            change_state("Attacking")
    
    fn on_exit():
        animation.stop()

state Attacking:
    fn on_enter():
        animation.play("attack_animation")
        emit_signal("attack_started")
    
    fn tick(delta: float):
        if animation.is_finished():
            change_state("Idle")
    
    fn on_exit():
        emit_signal("attack_finished")

# ===== Signal/Slot Pattern =====
signal health_changed(old_health: int, new_health: int)
signal died

@export
var player_health = 100

@export
var player_speed = 150.0

# ===== Event Binding (Signal/Slot) =====
player.health_changed => ui.update_health_bar
player.died => game_manager.end_level

# ===== @Operator Namespace =====
function calculate_distance(v1: Vector2, v2: Vector2) -> float:
    # Standart (güvenli)
    var slow_distance = (v1 - v2).length()
    
    # Native (hızlı)
    var fast_distance = @vector.distance(v1, v2)
    
    return fast_distance

function take_damage(damage: int):
    var old_health = player_health
    player_health -= damage
    emit_signal("health_changed", old_health, player_health)
    
    if player_health <= 0:
        emit_signal("died")
```

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

## 🔧 Kurulum & Ayarı

### Gereksinimler
- .NET 10.0 SDK
- Python 3.8+
- VS Code (isteğe bağlı, dil desteği için)
- Git

### Windows

```powershell
# Depoyu klonla
git clone https://github.com/synthesis-lab/synengine
cd synengine

# .NET projesini derle
cd SynEngine.Core
dotnet build
dotnet run
```

### Linux / macOS

```bash
# Depoyu klonla
git clone https://github.com/synthesis-lab/synengine
cd synengine

# .NET projesini derle
cd SynEngine.Core
dotnet build
dotnet run
```

### VS Code Eklentisi Kurulumu

1. `SynScript/vscode/` klasörünü kopyala:
   ```bash
   cp -r SynScript/vscode ~/.vscode/extensions/synscript-0.2.0/
   ```

2. VS Code'u yeniden başlat

3. `.syn` dosyası oluştur ve sına

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

### Phase 1 v0.2.0 ✅ (TAMAMLANDI)

#### Core Language Features
- ✅ SynScript dili (ANTLR 4 gramer, transpiler)
- ✅ **🎮 State Machine Pattern** (built-in `state` keyword)
- ✅ **📡 Signal/Slot Event System** (`signal`, `=>` operatörü)
- ✅ **⚡ @Operator Namespace** (`@vector`, `@math`, `@native`, `@color`)
- ✅ **🏛️ Actor Scope Isolation** (message passing, security)
- ✅ **⏳ Async/Await Support** (JavaScript-style non-blocking)
- ✅ **Optional Typing** (static analysis + duck typing)

#### Standard Library Features
- ✅ SynMath: 15+ matematiksel fonksiyon (sin, cos, clamp, lerp, vb.)
- ✅ SynColor: RGBA renk sınıfı ve 8 statik renk
- ✅ SynVector: Vector2/Vector3 operatörleriyle
- ✅ SynTimer: Tek sefer ve tekrarlayan zamanlayıcılar
- ✅ **State** (v0.2): Oyun durumu yönetimi
- ✅ **Signal** (v0.2): Event tetikleme ve alma
- ✅ **Actor** (v0.2): Oyun nesnesi temel sınıfı
- ✅ **TypeInference** (v0.2): Dinamik/statik tip kontrolü

#### Developer Experience
- ✅ VS Code syntax highlighting
- ✅ **20+ Code snippets** (variable, function, state, signal, actor, @vector, vb.)
- ✅ Error handling ve detailed error messages
- ✅ Language configuration (brackets, indentation)
- ✅ **v0.2 Theme support** (Lab themed colors)
- ✅ **v0.2 Semantic highlighting** (State/Signal/Actor renklendirilmesi)

### Phase 2 ⏳ (SIRADA)
- ⏳ Godot entegrasyonu
- ⏳ Python.NET bellek içi köprüsü
- ⏳ SynActor sarmalayıcısı (Godot Node2D/Node3D)
- ⏳ Sinyal eşlemesi (SynScript Signal → Godot signals)
- ⏳ Inspector entegrasyonu
- ⏳ Real-time preview

### Phase 3 🧊 (PLANLANIYOR)
- 🧊 Phaser (Web) entegrasyonu
- 🧊 Brython/Pyodide çalışma ortamı
- 🧊 JavaScript transpiler
- 🧊 Web varlık yönetimi
- 🧊 Browser debugging

### Phase 4 🧊 (PLANLANIYOR)
- 🧊 Language Server Protocol (LSP)
- 🧊 Görsel betik editörü
- 🧊 Paket yöneticisi (SynPackage)
- 🧊 Topluluk pazarı
- 🧊 AI-assisted code generation

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
    # Girdi alma
    var direction = Input.get_vector("left", "right", "up", "down")
    
    # Hareket
    velocity.x = direction.x * speed
    
    # Yer çekimi
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

## 🧪 Test & Doğrulama

```bash
# Söz dizimi doğrulaması
dotnet run validate script.syn

# Test fonksiyonunu çalıştır
dotnet run execute script.syn test_function

# Tamamen test paketi
dotnet test SynEngine.Core.Tests/
```

---

## 🤝 Katkıda Bulunma

### İyi Başlangıç Konuları
1. **StdLib Genişletmesi**: Yeni matematik/fizik fonksiyonları
2. **Örnek Oyunlar**: Kütüphanelerin kullanımını gösteren örnekler
3. **Belgelendirme**: Türkçe, İngilizce API belgeleri
4. **Testler**: Birim testleri yazma
5. **Performans**: Profilleme ve iyileştirme

### Geliştirme Ayarı

```bash
# Fork ve klonla
git clone https://github.com/YOUR_GITHUB/synengine
cd synengine

# Özellik dalı oluştur
git checkout -b feature/your-feature

# Değişiklikleri teslim et
git commit -am "Add new feature"

# Gönder
git push origin feature/your-feature

# Pull request açın
```

**Katkı Rehberi**: [CONTRIBUTING.md](CONTRIBUTING.md) (Yakında)

---

## 📋 Bilinen Sorunlar

| Sorun | Durum | Çözüm |
|-------|-------|-------|
| Godot entegrasyonu yok | 🔴 | Phase 2 başlangıcında |
| ANTLR parser derlenmiş durumda değil | 🟡 | Sonraki sürüm |
| Web desteği eksik | 🔴 | Phase 3 |
| LSP sunucusu yok | 🔴 | Phase 4 |

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

Lütfen şunları ekleyin:
- [ ] Hatanın açıklaması
- [ ] Tekrarlama adımları
- [ ] Beklenen vs gerçek davranış
- [ ] SynEngine sürümü

---

## 📝 Lisans

SynEngine Apache License 2.0 ile lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

```
Apache License 2.0 © 2026 Synthesis Lab
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

- **Godot Foundation** - Üstün oyun motoru
- **Python Software Foundation** - Python dilinin mükemmel tasarımı  
- **ANTLR Project** - Ayrıştırıcı üreticisi
- **Synthesis Lab Ekibi** - SynEngine'in mimarları

---

**SynEngine: Oyun Geliştirmeyi Herkes İçin Erişilebilir Kılın 🚀**

Detaylı yol haritası için [MASTER_ROADMAP.md](MASTER_ROADMAP.md) bakın.

**SON GÜNCELLEME**: 6 Mart 2026
