# SynScript Language Specification v0.1

## 🎯 Özet
SynScript, oyun geliştirme için tasarlanmış **Python-tabanlı** fakat **Python'dan bağımsız söz dizimi** (syntax) kullanmayan bir betik dilidir. C#/.NET tarafından transpile edilerek Python runtime'ında çalışır.

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

## 🚀 Çalışma Şekli

1. **Dosya Okuma**: `.syn` dosyası C# tarafından okunur
2. **Dönüştürüm**: `SynScriptTranspiler` SynScript → Python dönüştürür
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
MIT License - Synthesis Lab tarafından

---

## 👥 Katkıcılar
- **Synthesis Lab Team**: Tasarım ve geliştirme
