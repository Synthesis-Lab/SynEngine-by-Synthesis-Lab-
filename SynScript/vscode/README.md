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

# SynScript Language Support for VS Code

VS Code'da SynScript (.syn) dosyaları için tam dil desteği sağlayan extension.

## 🎨 Özellikler

✅ **Syntax Highlighting** - SynScript syntax'ı renkle vurgular
✅ **Code Snippets** - Hızlı kod yazımı için önceden tanımlanmış parçacıklar  
✅ **Language Configuration** - Otomatik girintilendirme, parantez eşleştirme
✅ **IntelliSense Hazırlanması** - Gelecek sürümde kod tamamlama

## 📦 Kurulum

### Manual Installation
1. Bu dizini VS Code extensions klasörüne kopyala:
   ```bash
   ~/.vscode/extensions/synscript-language-support-0.1.0/
   ```

2. VS Code'u yeniden başlat

### NPM Aracılığı (Ileride)
```bash
npm install -g synscript-language-support
```

## 🚀 Kullanım

1. `.syn` uzantılı dosya oluştur
2. VS Code otomatik olarak SynScript syntax'ını tanır
3. Code snippets'i kullan (`Ctrl+Space` veya `Cmd+Space`)

### Örnek Snippets

| Snippet | Komut |
|---------|-------|
| Variable | `var` + Tab |
| Function | `func` + Tab |
| If-Else | `ifelse` + Tab |
| For Loop | `for` + Tab |
| Vector2 | `vec2` + Tab |
| Timer | `timer` + Tab |

## 🎯 Desteklenen Söz Dizimi

- **Değişkenler**: `var`, `var x: type`, `var x = value`
- **Fonksiyonlar**: `function name() -> type:`
- **Dekoratörler**: `@export`, `@on_ready`, `@process`, `@signal`
- **Kontrol Akışı**: `if`, `elif`, `else`, `for`, `while`, `break`, `continue`, `return`
- **Tipler**: `int`, `float`, `string`, `bool`, `Vector2`, `Vector3`, `Color`
- **StdLib**: `SynMath`, `SynColor`, `SynTimer`, `DeltaTimer`, `Vector2`, `Vector3`, `Input`

## 🐛 Hatalar Bildir

GitHub Issues'den SynScript diline ilişkin hataları bildir:
https://github.com/synthesis-lab/synengine/issues

## 📝 Lisans
Apache License 2.0 - © 2026 Synthesis Lab

---

**Sürüm**: 0.1.0  
**Son Güncelleme**: 6 Mart 2026
