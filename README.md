# 🎮 SynEngine - Hibrit Oyun Motoru Ekosistemi

**Synthesis Lab tarafından geliştirilmekte olan çapraz-platform oyun motoru ailesi.**

> **Çift Sürüm Mimarisi**: 
> - 🏗️ **SynEngine Studio**: Godot destekli, C#/C++ runtime, masaüstü (Windows/macOS/Linux)
> - 🚀 **SynEngine GO**: Cocos destekli, Java/Kotlin runtime, çapraz-platform (Desktop + Mobil + Web)

---

## 📊 Proje Durumu

### SynEngine Studio (Amiralgemisi)
| Aşama | Durum | İlerleme | Açıklama |
|-------|-------|----------|----------|
| **Phase 1: SynScript v0.2.0** | ✅ TAMAMLANDI | 100% | Python variant, ANTLR gramer, StdLib |
| **Phase 2: Godot Entegrasyonu** | ⏳ SIRADA | 0% | Python.NET bridge, SynActor wrapper |
| **Phase 4: IDE & Ekosistem** | 🧊 SONRASI | 0% | LSP server, visual scripter, package manager |

### SynEngine GO (Spin-off, Studio'dan sonra başlar)
| Aşama | Durum | İlerleme | Açıklama |
|-------|-------|----------|----------|
| **Phase 3: Cocos Entegrasyonu** | 🧊 PLANLANIYOR | 0% | JavaScript variant, Java/Kotlin runtime |
| **Phase 4: IDE & Ekosistem** | 🧊 SONRASI | 0% | Mobile/Web support, Android Studio integration |

**Son Güncelleme**: 7 Mart 2026  
**Sürüm**: v0.2.0 - State Machine, Signal/Slot, @Operators (Python variant)

---

## 🎯 Vision

SynEngine, oyun geliştiricilerin **hızlı prototip yapması ve produktif olması** için tasarlanmış bir **çapraz-platform oyun motoru ekosistemidir**.

### SynEngine Studio - Amiralgemisi 🏗️
- 🎮 **Godot Engine** desteği
- 🐍 **Python-benzeri SynScript** (v0.2.0+)
- 💪 **C#/C++ runtime** (.NET 10.0 + native code)
- 🖥️ **Desktop platforms** (Windows/macOS/Linux)
- 📚 **Eğitim ve indie dev** odaklı

### SynEngine GO - Spin-off 🚀
- 🎮 **Cocos Engine** desteği
- 💻 **JavaScript-benzeri SynScript** (v0.3.0+)
- ☕ **Java/Kotlin runtime**
- 📱 **Çapraz-platform** (Desktop + iOS + Android + Web)
- 🌍 **Mobil ve web oyunları** odaklı

### Shared Features (Her İki Sürüm)
- 🎮 **State Machine First**: Oyun mantığı için built-in State deseni
- 📡 **Signal/Slot Events**: Deklaratif event binding (`=>` operatörü)
- ⚡ **@Operator Namespace**: Performans kritik işlemler için native operators  
- 🏛️ **Actor Scope Isolation**: Message-based architecture
- ⏳ **Async/Await Support**: Non-blocking game logic
- 📚 **Eğitim Dostu**: Başlangıçtan ileri seviyeye

---

## 🚀 Hızlı Başlangıç

### SynScript Dil Örneği (Python Variant - Studio)

```synscript
# SynScript - Oyun geliştiriciler için Hibrid dil (Python benzeri)

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

### Phase 1 v0.2.0 ✅ (TAMAMLANDI - Python Variant)

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
- ✅ **23+ Code snippets** (variable, function, state, signal, actor, @vector, vb.)
- ✅ Error handling ve detailed error messages
- ✅ Language configuration (brackets, indentation)
- ✅ **SynScript-Lab-Dark theme** (game dev optimized)
- ✅ **Advanced Linter** (6 analytical rules)
- ✅ **Syn-CLI** (validation, preview, reference lookup)

---

### Phase 2 ⏳ (SIRADA - SynEngine Studio)
**Hedef**: Godot Engine'de SynScript (Python variant) çalıştırmak

- ⏳ Python.NET in-memory bridge
- ⏳ SynActor sarmalayıcısı (Godot Node2D/Node3D)
- ⏳ Sinyal eşlemesi (SynScript Signal → Godot signals)
- ⏳ Inspector entegrasyonu (@export variables)
- ⏳ Hot reload desteği
- ⏳ Real-time preview
- ⏳ 5+ örnek oyun (character controller, RPG, platformer vb.)

---

### Phase 3 🧊 (PLANLANIYOR - SynEngine GO)
**Hedef**: Cocos Engine'de SynScript (JavaScript variant) çalıştırmak

#### 3.1 Language Variant (JavaScript benzeri syntax)
- 🧊 JavaScript-benzeri SynScript syntax
- 🧊 Type inference ve optional typing
- 🧊 Same game concepts (State, Signal, Actor)
- 🧊 SynScript → TypeScript transpiler

#### 3.2 Cross-Platform Runtime (Java/Kotlin)
- 🧊 Java/Kotlin Cocos wrapper
- 🧊 Android NDK integration
- 🧊 Desktop, Mobile (iOS/Android), Web support
- 🧊 Gradle build system

#### 3.3 Developer Tools
- 🧊 Android Studio integration
- 🧊 Web-based IDE
- 🧊 Build pipeline (desktop/mobile/web)
- 🧊 5+ örnek oyun (mobile-optimized)

---

### Phase 4 🧊 (SONRASI - Her İki Sürüm)
**Hedef**: Professional IDE ve ekosistem

- 🧊 Language Server Protocol (LSP)
- 🧊 Intellisense ve code completion
- 🧊 Visual/node-based scripter
- 🧊 Package manager (syn-pkg)
- 🧊 Asset store integration
- 🧊 Official documentation (TR + EN)
- 🧊 Community support (Discord, forums)
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

### Başlamak İçin İyi Konular
1. **StdLib Genişletmesi**: Yeni matematik/fizik fonksiyonları
2. **Örnek Oyunlar**: Kütüphanelerin kullanımını gösteren örnekler
3. **Belgelendirme**: Türkçe, İngilizce API referansları
4. **Testler**: Birim testleri yazma
5. **Performans**: Profilleme ve optimizasyon

### Geliştirme Ortamı Kurulumu

```bash
# Fork ve klonla
git clone https://github.com/YOUR_GITHUB/synengine
cd synengine

# Özellik dalı oluştur
git checkout -b feature/yeni-ozellik

# Değişiklikleri kaydet
git commit -am "Yeni özellik ekle"

# Gönder
git push origin feature/yeni-ozellik

# Pull request açın
```

**Katkı Rehberi**: [CONTRIBUTING.md](CONTRIBUTING.md) (Yakında)

---

## 📋 Bilinen Sorunlar

| Sorun | Durum | Çözüm |
|-------|-------|-------|
| Godot entegrasyonu henüz yapılmadı | 🔴 | Phase 2'de |
| ANTLR parser henüz derlenmiş değil | 🟡 | Sonraki sürüm |
| Web desteği henüz yoktur | 🔴 | Phase 3'te |
| LSP sunucusu henüz yoktur | 🔴 | Phase 4'te |

---

## 📊 İstatistikler

```
Phase 1 v0.2.0 Tamamlama İstatistikleri:
├── Toplam Kod Satırı: 1500+ (Python + C# + JS)
├── StdLib Fonksiyonları: 40+
├── Test Fonksiyonları: 7
├── VS Code Snippet'leri: 23+
├── Dokümantasyon Sayfaları: 8+
├── Linter Kuralları: 6
└── Theme Renk Grubu: 11+
```

---

## 🐛 Hata Bildir

Bir hata mı buldunuz? [GitHub Issues](https://github.com/synthesis-lab/synengine/issues) üzerinde bildir.

Lütfen aşağıdakini ekleyin:
- [ ] Hatanın açık açıklaması
- [ ] Sorunu tekrarlama adımları
- [ ] Beklenen vs gerçek davranış
- [ ] SynEngine sürümü
- [ ] Kullanılan sistem (Windows/Linux/macOS)

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

- **Godot Foundation** - Harika oyun motoru
- **Python Software Foundation** - Python'un tasarımı  
- **ANTLR Project** - Ayrıştırıcı üreteci
- **VS Code Community** - Mükemmel geliştirme ortamı
- **Synthesis Lab Ekibi** - SynEngine'in yaratıcıları

---

**SynEngine: Oyun Geliştirmeyi Herkese Açık Kılın 🚀**

Detaylı yol haritası için [MASTER_ROADMAP.md](MASTER_ROADMAP.md) dosyasına bakın.

**Son Güncelleme**: 7 Mart 2026 (v0.2.0 Sürümü)
