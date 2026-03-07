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

# SynScript Language Support for VS Code (v0.3.2)

VS Code'da SynScript (.syn) dosyaları için tam dil desteği ve hata ayıklama sağlayan profesyonel uzantı.

## 🎨 Özellikler

✅ **Syntax Highlighting** - SynScript syntax'ı renkle vurgular (State, Signal, @operators dahil)
✅ **Professional Debugger** - DAP destekli breakpoint, stack trace, değişken denetimi (YENİ v0.3.2)
✅ **State Machine Support** - `state` keyword'ü ve yaşam döngüsü (`on_enter`, `tick`, `on_exit`)
✅ **Signal/Slot Pattern** - `signal` tanımları ve `=>` operatörü
✅ **@Operator Namespace** - `@vector`, `@math`, `@native` operasyonları
✅ **Code Snippets** - Hızlı kod yazımı için 20+ önceden tanımlanmış parçacık
✅ **Language Configuration** - Otomatik girintilendirme, parantez eşleştirme
✅ **Professional Icon** - Duck tasarımı kod emblemli (YENİ v0.3.2)
✅ **Dark & Light Themes** - VS Code Dark uyumlu temalar (Güncellenmiş v0.3.2)
✅ **Actor Support** - Actor scope isolation ve message passing
✅ **Async/Await Ready** - `async`/`await` keyword desteği (transpilation)

## 📦 Kurulum

### Manuel Kurulum
1. Bu dizini VS Code extensions klasörüne kopyala:
   ```bash
   ~/.vscode/extensions/synscript-language-support-0.3.2/
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

### Debugger Kullanımı (v0.3.2) - YENİ

#### Hızlı Başlat
1. **Run and Debug Sekmesi**: `Ctrl+Shift+D` tuşlarına bas
2. **Konfigürasyon Seç**: "SynScript: Mevcut Dosyayı Başlat" seç
3. **Hata Ayıklamayı Başlat**: ▶️ yeşil buton'a tıkla veya `F5` tuşuna bas

#### Breakpoint Ayarlama
1. Sat\u0131r numaras\u0131n\u0131n solundaki kenara t\u0131kla (kırmızı nokta görüntülenir)
2. Hata ayıklama devam ederken bu satırda durur

#### Koşullu Breakpoint (Conditional Breakpoint)
1. Sat\u0131r numaras\u0131n\u0131n üzerine sa\u011f t\u0131kla
2. "Add Conditional Breakpoint" seç
3. Ko\u015ful gir (örn: `count > 10`)
4. Koşul sağlandığında durur

#### Logpoint (Log Yaz)
1. Sat\u0131r numaras\u0131n\u0131n üzerine sa\u011f t\u0131kla
2. "Add Logpoint" seç
3. Log mesaj\u0131 gir (örn: `Counter: {count}`)
4. Çalıştırma durdulmadan console'a yazd\u0131r\u0131r

#### Adım Adım Çalıştırma
- **F10** veya **Step Over**: Bir sat\u0131r ilerle (fonksiyona girme)
- **F11** veya **Step In**: Fonksiyona gir ve çalıştır
- **Shift+F11** veya **Step Out**: Mevcut fonksiyondan çık
- **F5** veya **Continue**: Sonraki breakpoint'e kadar çalıştır

#### Değişkenleri İnceleme
1. Debug panelinde (sol) "Variables" bölümüne bak
2. Local, Global, Static değişkenleri göreceksin
3. Değerleri genişlet ve basit değerler göster

#### Watch Expression (İzle)
1. Debug panelinde "Watch" bölümüne git
2. + butonuna bas ve expression gir (örn: `myArray.length`)
3. Her debug adımında otomatik güncellenir

#### Debug Console
1. Debug panelinde "Debug Console" sekmesine git
2. JavaScript benzeri expression'lar yazabilirsin
3. Hata ayıklanacak program'ın bağlamında değerlendirilir

### Komutu Doğrudan Çalıştırma
- **Ctrl+Shift+P** → "SynScript: Dosyayı Çalıştır" veya "SynScript: Hata Ayıklamayı Başlat"
- Mevcut dosya otomatik olarak seçilir

### Örnek Parçacıklar (v0.3.2 ile)

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

## 🎯 v0.3.2 Desteklenen Söz Dizimi

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

**Sürüm**: 0.3.2  
**Son Güncelleme**: 7 Mart 2026  
**Yenilikler**: - **Tema Güncellemesi**
                - 🌙 SynScript Lab Modern Dark - Profesyonel koyu modern tema eklendi
                - ☀️ SynScript Lab Modern Light - Profesyonel açık modern tema eklendi
