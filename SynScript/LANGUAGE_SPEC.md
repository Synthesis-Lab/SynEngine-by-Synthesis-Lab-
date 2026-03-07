<!--
Copyright © 2026 Synthesis Lab

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

# SynScript Language Specification v0.2.0

## 🎯 Özet
SynScript, oyun geliştirme için tasarlanmış **Hibrid Laboratuvar** ürünüdür. Python'un okunabilirliğini ve JavaScript'in asenkron gücünü oyun pratiğine katarak, **State Machine**, **Signal/Slot pattern** ve **Native Operator** desteği ile inşa edilmiş modern bir betik dilidir.

**Miraslar:**
- 🐍 **Python**: Temiz indentation, list comprehensions, okunabilir operatörler (and/or/not)
- 📜 **JavaScript**: Async/await, JSON esnekliği, event-driven mimarisi
- ✨ **SynScript**: Built-in State Machine, @native operators, Signal/Slot pattern, Actor isolation

---

## 📋 Temel Özeller

### 1. **Değişken Tanımlama (`var`)**
Python'daki basit atama yerine SynScript özel söz dizimi kullanır:

```synscript
# SynScript
var health = 100
var speed: float = 5.5
var player_name: string = "Hero"

# Transpile Edilen Python
health = 100
speed: float = 5.5
player_name: string = "Hero"
```

### 2. **Fonksiyon Tanımlama (`function`)**
```synscript
# SynScript
function calculate_damage(base_damage: int, multiplier: float) -> float:
    return base_damage * multiplier

# Transpile Edilen Python
def calculate_damage(base_damage: int, multiplier: float) -> float:
    return base_damage * multiplier
```

### 3. **Dekoratörler (Decorators)**
Oyun olaylarını simüle etmek için özel dekoratörler:

```synscript
@export              # Değişkeni Godot editöründe görünür kılar
@on_ready            # Node hazırlandığında çalışır
@on_process          # Her frame'de çalışır
@signal              # Sinyal fonksiyonları
```

### 4. **Standart Kütüphane (StdLib)**

#### **SynMath** - Matematiksel işlemler
```synscript
var pi = SynMath.PI
var result = SynMath.sin(angle)
var clamped = SynMath.clamp(value, 0, 100)
var distance = SynMath.distance(x1, y1, x2, y2)
```

#### **SynColor** - RGBA renk yönetimi
```synscript
var red = SynColor.RED()
var custom = SynColor(0.5, 0.8, 0.3, 1.0)
var hex = red.to_hex()  # "#FF0000FF"
var blended = red.blend(blue, 0.5)
```

#### **Vector2 & Vector3** - Vektör işlemleri
```synscript
var v1 = Vector2(3.0, 4.0)
var v2 = Vector2(1.0, 2.0)
var length = v1.length()  # 5.0
var distance = v1.distance_to(v2)
var normalized = v1.normalized()
var new_v = v1 + v2  # Vector2(4.0, 6.0)
```

#### **SynTimer & DeltaTimer** - Zaman yönetimi
```synscript
var timer = SynTimer(2.0, false)  # 2 saniye, tekrarlama yok
timer.start()
timer.tick(delta)
if timer.is_finished:
    print("Zaman doldu!")

var delta_timer = DeltaTimer(60)  # 60 FPS hedef
var dt = delta_timer.tick()  # Frame'den baştan çıkan zaman
```

### 5. **Kontrol Akışı**
```synscript
# if/elif/else
if player_health > 50:
    print("Belki iyisin")
elif player_health > 0:
    print("Napalı ama ayaktasın")
else:
    print("Öldün!")

# for döngüsü
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# while döngüsü
var count = 0
while count < 10:
    count = count + 1

# break ve continue
for i in range(10):
    if i == 3:
        break
    if i == 1:
        continue
```

### 6. **Açıklamalar (Comments)**
```synscript
# Bu tek satır açıklaması
# SynScript Python uyumlu komentler kullanır
```

---

## 📂 Dosya Yapısı

```
SynEngine-by-Synthesis-Lab-/
├── SynScript/                          # SynScript dili
│   ├── Grammar/
│   │   └── SynScript.g4                # ANTLR 4 Grameri
│   ├── StdLib/                         # Standart Kütüphane
│   │   ├── __init__.py
│   │   ├── synmath.py                  # Matematik işlemleri
│   │   ├── syncolor.py                 # Renk yönetimi
│   │   ├── syntimer.py                 # Zaman yönetimi
│   │   └── synvector.py                # Vektör işlemleri
│   └── Examples/
│       └── character_controller.syn    # Örnek karakter kontrolcüsü
├── SynEngine.Core/                     # C# Çalışma Zamanı
│   ├── Class1.cs                       # Transpiler + Engine
│   ├── main.syn                        # Test scripti
│   └── SynEngine.Core.csproj
└── README.md
```

---

## 🔄 Dönüştürüm (Transpilation) Örneği

### **Giriş (SynScript)**
```synscript
@export
var player_speed = 150.0

function update_position(delta: float) -> Vector2:
    var new_x = position.x + player_speed * delta
    return Vector2(new_x, position.y)
```

### **Çıkış (Python)**
```python
# __export__
player_speed = 150.0

def update_position(delta: float) -> Vector2:
    new_x = position.x + player_speed * delta
    return Vector2(new_x, position.y)
```

---

## ✅ Desteklenen Veri Tipleri

| SynScript | Python | Açıklama |
|-----------|--------|----------|
| `int` | `int` | Tam sayı |
| `float` | `float` | Ondalık sayı |
| `string` | `str` | Metin |
| `bool` | `bool` | Doğru/Yanlış |
| `Vector2` | `Vector2` (StdLib) | 2D Vektör |
| `Vector3` | `Vector3` (StdLib) | 3D Vektör |
| `Color` | `SynColor` (StdLib) | RGBA Renk |

---

## 🐛 Hata Yönetimi

Transpiler yapısal hataları algılar:
- **SyntaxError**: Eşleşmeyen parantez, bracket, brace
- **TypeError**: Tip uyumsuzluğu (gelecek sürüm)
- **NameError**: Tanımlanmamış değişken (Python runtime'dan)

```plaintext
[SynEngine] ERROR: SynScript Syntax Errors:
SyntaxError at line 5: Unmatched closing parenthesis
  print("Test"
```

---

## 🎮 State Machine Mimarisi (v0.2.0)

SynScript, State Machine'i **birinci sınıf dil yapısı** olarak sunar:

### **State Tanımı**

```synscript
state Angry:
    fn on_enter():
        print("DÜŞMAN KIZDI!")
        animation.play("angry_idle")
    
    fn tick(delta: float):
        var distance_to_player = position.distance_to(player.position)
        if distance_to_player < 50:
            attack_player()
        else:
            chase_player()
    
    fn on_exit():
        print("Düşman sakinleşti.")
        animation.stop()

state Calm:
    fn on_enter():
        animation.play("idle")
        patrol_timer.start()
    
    fn tick(delta: float):
        patrol()

state Dead:
    fn on_enter():
        animation.play("death")
        emit_signal("enemy_died", experience_reward)
    
    fn tick(delta: float):
        pass
```

### **State Döngüsü**

Her state şu yaşam döngüsünü izler:

```
[Other State] → on_exit() → [New State] → on_enter() → tick(delta) → tick(delta) → ...
```

### **State Geçişleri**

State'ler **Signal** aracılığıyla geçiş yapar (aşağıya bakın).

---

## ⚡ @Operator Namespace (v0.2.0)

Performans özellikleri için **yerli kesinlikle derlenmiş operasyonlar**:

```synscript
var v1 = Vector2(1, 2)
var v2 = Vector2(3, 4)

// Standart Phyton-stili (varsayılan, güvenli)
var sum = v1 + v2

// @Operator ile (hızlı, doğrudan C++ çağrısı)
var sum_fast = @vector.add(v1, v2)

// Diğer @operators
var distance = @vector.distance(v1, v2)
var normalized = @vector.normalize(v1)
var angle = @math.atan2(dy, dx)
var sin_fast = @math.sin(angle)
```

### **@Operator Kategorileri**

| Namespace | Operasyonlar | Kullanım |
|-----------|-------------|----------|
| `@vector` | add, subtract, multiply, normalize, distance, dot, cross | Vektör matematiği |
| `@math` | sin, cos, tan, sqrt, pow, clamp, lerp | Skalar matematiği |
| `@native` | custom_c_functions | C++ entegrasyonu |
| `@color` | blend, brighten, desaturate | Renk işlemleri |

---

## 📡 Signal/Slot Event System (v0.2.0)

Game event'leri için **deklaratif event binding**:

### **Signal Tanımı**

```synscript
signal health_changed(old_value: int, new_value: int)
signal died(killer: string)
signal reached_checkpoint(checkpoint_id: int)
```

### **Signal Emit (Tetikle)**

```synscript
fn take_damage(amount: int):
    var old_hp = health
    health -= amount
    
    # Signal tetikleme
    emit_signal("health_changed", old_hp, health)
    
    if health <= 0:
        emit_signal("died", "Enemy Attack")
```

### **Signal Binding (`=>` operatörü)**

```synscript
# UI'yı sağlıkla otomatik senkronize et
player.health_changed => health_bar.update_value

# Ses efekti oynat
player.died => audio_manager.play_death_sound

# Reboot tetikle
player.reached_checkpoint => restart_timer.start
```

### **Avantajları**

- ✅ Callback cehennemini önler (no nested callbacks)
- ✅ Deklaratif bağlantı (kod okunabilirliği)
- ✅ Dinamik bağlantı (runtime'da additive events)
- ✅ Type-safe (aktör kapsamında scope isolation)

---

## 🏛️ Actor Scope Isolation (v0.2.0)

Her oyun nesnesi (actor), kendi **izole ad alanında** (actor scope) yaşar:

```synscript
actor PlayerCharacter:
    # Oyuncu-özel değişkenler (diğer actor'lar okunamaz)
    var position: Vector2 = Vector2(0, 0)
    var health: int = 100
    var inventory = []

    # Oyuncu-özel state'ler
    state Running:
        fn tick(delta: float):
            move_by_input()
    
    state Jumping:
        fn tick(delta: float):
            apply_gravity(delta)
    
    # Mesaj geçişi ile iletişim
    signal jump_requested
    
    fn request_jump():
        emit_signal("jump_requested")

actor Enemy:
    var position: Vector2 = Vector2(100, 100)
    var target: Actor = null  # Reference geçişi

    state Hunting:
        fn tick(delta: float):
            if target:
                move_toward(target.position)

# Scope dışında erişim başarısız olur
print(player.position)      # ✅ Çalışır
print(enemy.position)       # ✅ Çalışır
print(inventory)            # ❌ HATA! (global scope yok)
```

### **Message Passing (Signal Aracılığıyla)**

```synscript
# Player durumunu diğer actor'lar bilmez, sadece signal alır
player.health_changed => ui.update_health_bar
player.died => game_manager.end_level
```

---

## ⏳ Async/Await Patterns (v0.2.0)

Bloke olmayan animasyonlar ve network işlemleri:

```synscript
# Bir animasyonun bitişini bekle
fn play_attack_animation():
    animation.play("sword_swing")
    await animation.finished()
    print("Animasyon bitti!")

# Zaman tabanlı gecikme
fn teleport_with_effect():
    emit_signal("teleport_requested")
    await timer.wait_seconds(1.0)
    position = target_position
    emit_signal("teleport_complete")

# Parallel await (çoklu operasyonları bekle)
fn load_level():
    var assets = await asset_loader.load_textures()
    var music = await audio_manager.load_music()
    # İkisi de bitene kadar devam etmez
    start_level()
```

### **Transpile Edilen Python**

```python
async def play_attack_animation():
    animation.play("sword_swing")
    await animation.finished()
    print("Animasyon bitti!")

async def teleport_with_effect():
    emit_signal("teleport_requested")
    await asyncio.sleep(1.0)
    position = target_position
    emit_signal("teleport_complete")
```

---

## 🚀 Çalışma Şekli

1. **Dosya Okuma**: `.syn` dosyası C# tarafından okunur
2. **Dönüştürüm**: `SynScriptTranspiler` SynScript → Python dönüştürür
   - State blocks → Python classes (State inheritance)
   - Signal declarations → Signal objects
   - Actor definitions → Actor class inheritance
   - @operators → Native function calls
   - async/await → asyncio syntax
3. **Validation**: Yapısal hatalar kontrol edilir
4. **Yürütme**: Python kodu `/usr/bin/python3` ile çalıştırılır
5. **Sonuç**: Çıktı C# tarafından alınır ve işlenir

---

## 📋 Yol Haritası (Roadmap)

| Aşama | Durum | Hedef |
|-------|-------|-------|
| **1. Dil Olgunlaştırma** | 🔧 DevAm Ediyor | ANTLR parser, StdLib expansion |
| **2. Godot Entegrasyonu** | ⏳ Sırada | Python.NET in-memory bridge |
| **3. Phaser (Web)** | 🧊 Beklemede | Brython/Pyodide + JS transpiler |
| **4. IDE Desteği** | 🧊 Beklemede | VS Code extension |

---

## 📝 Lisans
Apache License 2.0 - Synthesis Lab tarafından

---

## 👥 Katkıcılar
- **Synthesis Lab Team**: Tasarım ve geliştirme
- **v0.1.0**: Temel dil ve transpiler
- **v0.2.0**: State Machine, Signal/Slot, @operators, async/await
