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

# SynScript Language Support for VS Code (v0.3.0)

VS Code'da SynScript (.syn) dosyaları için tam dil desteği ve hata ayıklama sağlayan profesyonel uzantı.

## 🎨 Özellikler

✅ **Syntax Highlighting** - SynScript syntax'ı renkle vurgular (State, Signal, @operators dahil)
✅ **Professional Debugger** - DAP destekli breakpoint, stack trace, değişken denetimi (YENİ v0.3.0)
✅ **State Machine Support** - `state` keyword'ü ve yaşam döngüsü (`on_enter`, `tick`, `on_exit`)
✅ **Signal/Slot Pattern** - `signal` tanımları ve `=>` operatörü
✅ **@Operator Namespace** - `@vector`, `@math`, `@native` operasyonları
✅ **Code Snippets** - Hızlı kod yazımı için 20+ önceden tanımlanmış parçacık
✅ **Language Configuration** - Otomatik girintilendirme, parantez eşleştirme
✅ **Professional Icon** - Duck tasarımı kod emblemli (YENİ v0.3.0)
✅ **Dark & Light Themes** - VS Code Dark uyumlu temalar (Güncellenmiş v0.3.0)
✅ **Actor Support** - Actor scope isolation ve message passing
✅ **Async/Await Ready** - `async`/`await` keyword desteği (transpilation)

## 📦 Kurulum

### Manuel Kurulum
1. Bu dizini VS Code extensions klasörüne kopyala:
   ```bash
   ~/.vscode/extensions/synscript-language-support-0.2.0/
   ```

2. VS Code'u yeniden başlat

### NPM Aracılığı (Ileride)
```bash
npm install -g synscript-language-support
```

## 🚀 Kullanım

### Temel Kullanım
1. `.syn` uzantılı dosya oluştur
2. VS Code otomatik olarak SynScript söz dizimini tanır
3. Code parçacıklarını kullan (`Ctrl+Space` veya `Cmd+Space`)

### Debugger Kullanımı (v0.3.0) - YENİ
1. **Breakpoint Ayarla**: Satır numarasının solundaki kenara tıkla
2. **Koşullu Breakpoint**: Sağ tıkla → "Add Conditional Breakpoint" → Koşul gir (örn: `count > 10`)
3. **Logpoint**: Sağ tıkla → "Add Logpoint" → Mesaj gir (örn: `Counter: {count}`)
4. **Debug Başlat**: `F5` veya "Run and Debug" panelinden
5. **Adım Adım Çalıştır**: `F10` (step over), `F11` (step in)
6. **Continue**: `F5` (sonraki breakpoint'e kadar)
7. **Değişkenleri İncele**: Debug paneldeki "Variables" bölümünde
8. **Expression Evaluate**: Debug console'de yazarak değerleri kontrol et

### Örnek Parçacıklar (v0.2.0 ile)

| Parça | Komut | Açıklama |
|---------|-------|----------|
| Variable | `var` + Tab | Değişken tanımla |
| Function | `func` + Tab | Fonksiyon tanımla |
| If-Else | `ifelse` + Tab | Koşullu blok |
| For Loop | `for` + Tab | Döngü |
| **State Block** | **`state` + Tab** | **State Machine (YENİ)** |
| **Signal** | **`signal` + Tab** | **Event isteyen tanımla (YENİ)** |
| **Signal Binding** | **`=>` + Tab** | **Signal bağlantısı (YENİ)** |
| **Actor** | **`actor` + Tab** | **Actor scope isolation (YENİ)** |
| **@Vector Operator** | **`@vector` + Tab** | **Vektor hızlanması (YENİ)** |
| **@Math Operator** | **`@math` + Tab** | **Matematik hızlanması (YENİ)** |
| Vector2 | `vec2` + Tab | 2D Vektör |
| Vector3 | `vec3` + Tab | 3D Vektör |
| Color | `color` + Tab | Renk |
| Timer | `timer` + Tab | Zamanlayıcı |
| Print | `print` + Tab | Konsol çıktısı |

## 🎯 v0.2.0 Desteklenen Söz Dizimi

| Kategori | Söz Dizimi |
|----------|-----------|
| **Değişkenler** | `var`, `var x: type`, `var x = value` |
| **Fonksiyonlar** | `function name() -> type:` |
| **State Machine** | `state Angry:` → `on_enter()`, `tick(delta)`, `on_exit()` |
| **Signal/Slot** | `signal event(params)` / `source => target` |
| **Dekoratörler** | `@export`, `@on_ready`, `@process`, `@signal` |
| **@Operators** | `@vector.*`, `@math.*`, `@native.*`, `@color.*` |
| **Async** | `async`, `await` (transpilation desteği) |
| **Kontrol Akışı** | `if`, `elif`, `else`, `for`, `while`, `break`, `continue`, `return` |
| **Tipler** | `int`, `float`, `string`, `bool`, `Vector2`, `Vector3`, `Color` |
| **StdLib** | `SynMath`, `SynColor`, `SynTimer`, `DeltaTimer`, `Vector2`, `Vector3`, `Input`, `State`, `Signal`, `Actor`, `TypeInference` |
| **Operatörler** | `+`, `-`, `*`, `/`, `%`, `**`, `==`, `!=`, `<`, `>`, `<=`, `>=`, `=>`, `and`, `or`, `not` |

## 🐛 Hatalar Bildir

GitHub Issues'den SynScript diline ilişkin hataları bildir:
https://github.com/synthesis-lab/synengine/issues

## 📝 Lisans
Apache License 2.0 - © 2026 Synthesis Lab

---

**Sürüm**: 0.3.0  
**Son Güncelleme**: 7 Mart 2026  
**Yenilikler**: 🐛 Professional Debugger (DAP), 🎨 Duck Icon, 🌙 Dark Theme v2 (VS Code Dark uyumlu)
