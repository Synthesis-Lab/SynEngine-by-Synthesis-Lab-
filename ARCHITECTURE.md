# 🏗️ SynEngine Mimarisi - Studio vs GO

**Synthesis Lab tarafından geliştirilen çift-motor mimarisi**

---

## 📋 Genel Bakış

SynEngine iki farklı **sürüm** olarak tasarlanmıştır:

1. **SynEngine Studio** (Amiralgemisi): Godot destekli, masaüstü oyunları
2. **SynEngine GO** (Spin-off): Cocos destekli, çapraz-platform oyunları

Her sürüm:
- ✅ **Aynı temel oyun kavramları** (State, Signal, Actor, @operators)
- ✅ **Aynı standard library API** (SynMath, SynColor, SynVector, SynTimer vb.)
- ❌ **Farklı dil varyantları** (Python vs JavaScript-benzeri söz dizimi)
- ❌ **Farklı runtime** (C# .NET vs Java/Kotlin)
- ❌ **Farklı hedef platformlar** (Masaüstü vs Masaüstü+Mobil+Web)

---

## 🏗️ Mimari Katmanlar

```
┌─────────────────────────────────────────────────────────────────┐
│                 SynScript (Birleştirilmiş Kavramlar)            │
├─────────────────────────────────────────────────────────────────┤
│  Katman 0: Temel Kavramlar (State, Signal, Actor, @operators)   │
│  Katman 1: Dil Söz Dizimi (Python variant vs JS variant)        │
│  Katman 2: Tip Sistemi (Python duck vs JS inference)            │
├─────────────────────────────────────────────────────────────────┤
│             SynEngine Studio            │    SynEngine GO        │
├─────────────────────────────────┼───────┼───────────────────────┤
│  Derleyici: Python              │       │ Derleyici: JS         │
│  Runtime: C#/.NET               │       │ Runtime: Java/Kotlin  │
│  Motor: Godot                   │       │ Motor: Cocos          │
│  Platformlar: Win/Mac/Linux     │       │ Platformlar: Tüm      │
└─────────────────────────────────┴───────┴───────────────────────┘
```

---

## 🎯 SynEngine Studio (Amiralgemisi)

### Mimarisi

```
┌──────────────────────────────────────────────────────────┐
│              SynScript (.syn dosyası)                     │
│     Python-benzeri söz dizimi (girinti-tabanlı)          │
└───────────────────────┬──────────────────────────────────┘
                        │
                        ▼
            ┌───────────────────────┐
            │   ANTLR 4 Ayrıştırıcısı│
            │  (SynScript.g4)       │
            │  Gramer → AST         │
            └───────────┬───────────┘
                        │
                        ▼
            ┌───────────────────────┐
            │  Derleyici (C#)       │
            │  Regex-tabanlı kurallar  │
            │  AST → Python kodu    │
            └───────────┬───────────┘
                        │
                        ▼
            ┌───────────────────────┐
            │  Python Kodu          │
            │  + Godot import'ları  │
            │  + StdLib (8 modül)   │
            └───────────┬───────────┘
                        │
                        ▼
            ┌───────────────────────┐
            │  Python.NET Köprüsü   │
            │  (Bellek İçi Çalışma) │
            │  C# ←→ Python IPC     │
            └───────────┬───────────┘
                        │
                        ▼
            ┌───────────────────────┐
            │   Godot Motoru        │
            │   (4.x C# API ile)    │
            │   Node2D/Node3D       │
            └───────────┬───────────┘
                        │
                        ▼
            ┌───────────────────────┐
            │   Masaüstü Oyunu!     │
            │ Win/macOS/Linux       │
            └───────────────────────┘
```

### Teknoloji Yığını

| Katman | Teknoloji | Amaç |
|--------|-----------|------|
| **Dil** | SynScript (Python variant) | Oyun betikleme |
| **Gramer** | ANTLR 4 | Resmi söz dizimi spesifikasyonu |
| **Derleyici** | C# + Regex | SynScript → Python |
| **Köprü** | Python.NET | C# ↔ Python iletişimi |
| **Runtime** | Python 3.8+ | Betik çalışması |
| **Motor** | Godot 4.x (.NET sürümü) | Oyun framework'ü |
| **IDE Desteği** | VS Code Extension + LSP | Geliştirici araçları |
| **Platformlar** | Windows, macOS, Linux | Masaüstü ihracı |

### Geliştirme Zaman Çizelgesi

- **Phase 1** ✅ (1 gün): Dil & StdLib tasarımı
- **Phase 2** ⏳ (1.5 hafta): Godot entegrasyonu
- **Phase 4** 🧊 (2.5 hafta): IDE & ekosistem cilası

**Hedef Kullanıcılar**:
- 🎓 Oyun geliştirme öğrencileri (Godot'ta öğren)
- 👨‍💻 İndie geliştiriciler (masaüstü odaklı)
- 📚 Eğitim kurumları (betik kursu)

---

## 🚀 SynEngine GO (Spin-off)

### Mimarisi

```
┌──────────────────────────────────────────────────────────┐
│              SynScript (.syn dosyası)                     │
│  JavaScript-benzeri söz dizimi (noktalı virgül, let/const)│
└───────────────────────┬──────────────────────────────────┘
                        │
                        ▼
            ┌───────────────────────┐
            │   ANTLR 4 Ayrıştırıcısı│
            │  (SynScript.g4)       │
            │  Gramer → AST         │
            └───────────┬───────────┘
                        │
                        ▼
            ┌───────────────────────┐
            │  Derleyici (Java)     │
            │  AST-tabanlı kurallar │
            │  AST → TypeScript     │
            └───────────┬───────────┘
                        │
                        ▼
            ┌───────────────────────┐
            │  TypeScript Kodu      │
            │  + Cocos import'ları  │
            │  + StdLib (JS variant)│
            └───────────┬───────────┘
                        │
                        ▼
            ┌───────────────────────┐
            │  TypeScript Derleyici │
            │  → JavaScript         │
            │  (ES2020+)            │
            └───────────┬───────────┘
                        │
                        ▼
         ┌──────────────┴──────────────┐
         │                             │
         ▼                             ▼
    ┌─────────────┐            ┌──────────────┐
    │ Masaüstü JVM│            │ Mobil Web    │
    │  (Electron) │            │ (HTML5/GL)   │
    └──────┬──────┘            └──────┬───────┘
           │                         │
           ▼                         ▼
    ┌──────────────────────────────────────────┐
    │  Cocos Creator 3.x Motoru                │
    │  (Evrensel runtime)                      │
    └──────────────────────████────────────────┘
           ▼                    ▼              ▼
      Masaüstü Oyunu      Mobil Oyunu      Web Oyunu
     Win/Mac/Linux       iOS/Android      Tarayıcı
```

### Teknoloji Yığını

| Katman | Teknoloji | Amaç |
|--------|-----------|------|
| **Dil** | SynScript (JS variant) | Oyun betikleme |
| **Gramer** | ANTLR 4 | Resmi söz dizimi spesifikasyonu |
| **Derleyici** | Java/Kotlin + AST | SynScript → TypeScript |
| **Dil Hedefi** | TypeScript + JavaScript | Cocos ekosistemi |
| **Derleyici** | TypeScript Derleyici | TS → JS derleme |
| **Motor** | Cocos Creator 3.x | Çapraz-platform framework |
| **Platformlar** | Windows, macOS, Linux (Ön) | Electron ile masaüstü |
|  | iOS, Android | Mobil native |
|  | Web | HTML5/WebGL |
| **IDE Desteği** | Android Studio + VS Code | Geliştirici araçları |

### Geliştirme Zaman Çizelgesi

- **Phase 3** 🧊 (2.5 hafta): Cocos entegrasyonu (Studio Phase 2'den sonra başlar)
- **Phase 4** 🧊 (2 hafta): IDE & ekosistem cilası

**Hedef Kullanıcılar**:
- 📱 Mobil oyun geliştiricileri
- 🌐 Web oyun geliştiricileri (Casual/İndie)
- 🌍 Çapraz-platform geliştiricileri
- 🎓 Oyun geliştirme bootcamp'ları (mobil odaklı)

---

## 🔄 Paylaşılan Bileşenler

Hem Studio hem de GO aynı **temel kavramsal temeli** paylaşır:

### 1. **Oyun Kavramları**

```synscript
// Her iki variant'da da aynı
state PlayerIdle:
    fn on_enter(): ...      // Godot: Python | GO: JavaScript
    fn tick(delta): ...
    fn on_exit(): ...

signal health_changed(old, new)
actor Player extends SynActor: ...
```

### 2. **Standart Kütüphane**

| Modül | Amaç | Studio (Python) | GO (JavaScript) |
|-------|------|-----------------|-----------------|
| **SynMath** | 15+ matematik fonksiyonu | synmath.py | synmath.ts |
| **SynColor** | Renk yönetimi | syncolor.py | syncolor.ts |
| **SynVector** | 2D/3D vektörler | synvector.py | synvector.ts |
| **SynTimer** | Zaman yardımcıları | syntimer.py | syntimer.ts |
| **State** | Durum makinesi temeli | synstate.py | synstate.ts |
| **Signal** | Olay sistemi | synsignal.py | synsignal.ts |
| **Actor** | Oyun nesnesi temeli | synactor.py | synactor.ts |
| **TypeInference** | Tip kontrolü | syntyping.py | syntyping.ts |

### 3. **@Operatör Ad Uzayı**

```synscript
// Her ikisinde de aynı API
@vector.add(v1, v2)
@vector.distance(v1, v2)
@math.sin(angle)
@math.clamp(value, min, max)
@color.blend(c1, c2, ratio)
```

---

## 🔀 Geçiş Yolu: Studio → GO

### Dil Söz Dizimi Geçişi (Python → JavaScript variant)

```python
# Studio (Python variant)
var player_speed: float = 150.0
state Moving:
    fn tick(delta: float):
        position += velocity * delta
```

```javascript
// GO (JavaScript variant)
let playerSpeed = 150.0;  // Tip çıkarımı
state Moving {
    tick(delta) {
        this.position += this.velocity.scale(delta);
    }
}
```

### Araç: Otomatik Derleyici (Phase 4'te Planlanmış)

```bash
# Studio betiğini GO betiğine dönüştür
synengine-convert studio-script.syn --target=go --output=go-script.syn

# Ya da tersini
synengine-convert go-script.syn --target=studio --output=studio-script.syn
```

---

## 🎓 Öğrenme Yolu

### Studio İçin (Masaüstü Oyun Geliştiricileri)

```
1. Python söz dizimini öğren (SynScript aracılığıyla)
   ↓
2. Oyun kavramlarını öğren (State, Signal, Actor)
   ↓
3. Godot motoru entegrasyonunu öğren
   ↓
4. 2D/3D masaüstü oyunları geliştir
```

### GO İçin (Mobil/Web Oyun Geliştiricileri)

```
1. JavaScript söz dizimini öğren (SynScript aracılığıyla)
   ↓
2. Oyun kavramlarını öğren (State, Signal, Actor)
   ↓
3. Cocos motoru entegrasyonunu öğren
   ↓
4. Mobil + web oyunlarını geliştir (çapraz-platform)
```

### Köprü: Studio'dan GO'ya

```
Studio'yu öğren (Python variant)
         ↓
Temel kavramları anla
         ↓
GO'ya geç (JavaScript variant)
         ↓
Kavramları yeniden kullan, farklı söz dizimi uygula
         ↓
Çapraz-platform oyunları geliştir
```

---

## 📊 Karşılaştırma Tablosu

| Yön | Studio | GO |
|-----|--------|-----|
| **Motor** | Godot 4.x | Cocos Creator 3.x |
| **Runtime** | C#/.NET 10.0 | Java/Kotlin + JavaScript |
| **Dil** | Python variant | JavaScript variant |
| **Platformlar** | Masaüstü (Win/Mac/Linux) | Masaüstü + Mobil + Web |
| **Hedef Kullanıcılar** | Masaüstü indie geliştiriciler | Mobil/web indie geliştiriciler |
| **Öğrenme Eğrisi** | Daha kolay (Python-benzeri) | Orta (JS-benzeri) |
| **Performans** | Yüksek (native kod) | Çapraz-platform (optimize) |
| **Ekosistem** | Godot asset mağazası | Cocos asset mağazası |
| **IDE** | VS Code + Godot | Android Studio + VS Code + Web IDE |
| **Olgunluk** | v0.2.0 hazır | v0.3.0 planlanmış |

---

## 🚀 Yol Haritası

### Studio (Amiralgemisi)

```
Phase 1 ✅ → Phase 2 ⏳ → Phase 4 🧊 → Olgun 🎉
(1 gün)    (1.5 hafta)   (2.5 hafta)
```

### GO (Spin-off, Studio Phase 2'den sonra başlar)

```
                       Phase 3 🧊 → Phase 4 🧊 → Olgun 🎉
                       (2.5 hafta)  (2 hafta)
```

**Zaman Çizelgesi**: Tam ekosistem için ~10-11 hafta

---

## 🎯 Başarı Metrikleri

### Studio Başarı Kriterleri
- ✅ Godot entegrasyonu kararlı
- ✅ 5+ örnek oyun yayımlandı
- ✅ 500+ GitHub yıldız
- ✅ 50+ topluluk oyunu

### GO Başarı Kriterleri
- ✅ Çapraz-platform dağıtımı çalışıyor
- ✅ 5+ mobil oyun yayımlandı
- ✅ 300+ ek GitHub yıldız (800+ toplam)
- ✅ 50+ topluluk oyunu (mobil/web)

### Ekosistem Başarısı
- ✅ 2000+ toplam GitHub yıldız
- ✅ 300+ Discord topluluk üyesi
- ✅ 100+ toplam topluluk oyunu
- ✅ Resmi asset mağazası 20+ ürün ile
- ✅ 10+ içerik yaratıcısı (YouTube/Twitch)

---

## 🔗 İlgili Belgeler

- [MASTER_ROADMAP.md](MASTER_ROADMAP.md) - Detaylı zaman çizelgesi ve hedefler
- [LANGUAGE_SPEC.md](SynScript/LANGUAGE_SPEC.md) - Dil spesifikasyonu (Python variant)
- [README.md](README.md) - Proje genel bakışı ve hızlı başlangıç
- [PHASE1_COMPLETION_REPORT.md](PHASE1_COMPLETION_REPORT.md) - Phase 1 detayları

---

**Son Güncelleme**: 7 Mart 2026  
**SynEngine Sürümü**: v0.2.0 (Studio - Python variant)  
**Durum**: Phase 1 Tamamlandı, Phase 2 Devam Ediyor
