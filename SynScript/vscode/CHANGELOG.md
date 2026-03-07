# SynScript Language Support - Sürüm Geçmişi
## [0.3.1] - 7 Mart 2026

### ✨ Yeni Özellikler

- **🐛 Hata Düzeltme**
  - 'package.json' dosyasındaki hatalar düzeltildi

## [0.3.0] - 7 Mart 2026

### ✨ Yeni Özellikler

- **🎨 Profesyonel İkon Tasarımı (YENİ)**
  - Duck ikonunun kod emblemli yeni tasarımı
  - Sarı başlı ördek + mavi gövde + yeşil `</>` kodu
  - Renkli sparkles (cyan, yeşil) ile dekorasyon
  - VS Code Marketplace'te profesyonel görünüm
  - 2048x2048 pixel PNG format

- **🐛 Debug Adapter Protocol (DAP) Desteği (YENİ)**
  - Tam SynScript debugger entegrasyonu
  - Breakpoint ayarlama ve koşullu breakpoints
  - Stack trace ve çağrı yığınını inceleme
  - Değişken denetimi ve canlı değerlendirme
  - Step in/over/out işlemleri
  - Logpoint desteği (code çalıştırmadan log yazdır)
  - Hover expression evaluation
  - Thread yönetimi
  - Console.log() alternatifi olarak breakpoint messages

- **▶️ Run and Debug UI Entegrasyonu (YENİ v0.3.0)**
  - VS Code "Çalıştırma ve Hata Ayıklama" sekmesy ile tam entegrasyon
  - `extension.js` - Tüm debug commands'ını handle eden ana extension dosyası
  - Komutlar:
    - `synscript.debug.start` - Hata ayıklamayı başlat (F5 uyumlu)
    - `synscript.run.file` - Dosyayı çalıştır
    - `synscript.debug.stop` - Debugger'ı durdur
  - Activation Events: onDebug, onLanguage, onCommand, workspaceContains
  - Launch configuration templates:
    - "SynScript: Program Başlat" (${workspaceFolder}/program.syn)
    - "SynScript: Mevcut Dosyayı Başlat" (${file} - EN ÇOK KULLANILAN)
    - "SynScript: Argümanlarla Başlat" (proje with CLI args)
  - Debug Adapter Factory - Node.js runtime ile debugger adapter'ı başlat
  - Extension info mesajı - Aktivasyon'da kullanıcıya bilgi ver

- **🌙 Dark Tema İyileştirmeleri**
  - VS Code Dark (#1e1e1e) uyumlu arka plan
  - Profesyonel renk paletine geçiş
  - Daha iyi kontrast ve okunabilirlik
  - Oyun dev semantik renk güncellemeleri:
    - Keywords: #569cd6 (Mavi)
    - Functions: #dcdcaa (Sarı)
    - Comments: #6a9955 (Yeşil)
    - State: #d4a9ff (Mor)
    - Signal: #4dd0e1 (Turkuaz)
  - Tüm UI elemanları (editor, sidebar, terminal) uyumlu

- **Birçok Tema Desteği**
  - 🌙 SynScript Lab Dark - VS Code Dark uyumlu profesyonel tema
  - ☀️ SynScript Lab Light - Aydınlık tema game dev için
  - Her iki tema da oyun geliştirme semantiğine optimize

- **Geliştirilmiş Sözdizimi Vurgulaması**
  - v0.3.0 oyun semantiği (State, Signal, Actor)
  - @Operator namespaces (@vector, @math, @color)
  - Async/await desteği
  - İyileştirilmiş type annotations

- **Kod Parçaları (23 Adet)**
  - State machine tanımı
  - Signal/Slot event binding
  - Actor yaratma ve yönetme
  - @Operator kullanım örnekleri
  - Async/await patterns

- **Linter Framework**
  - Statik kod analizi
  - Hata tespiti ve uyarılar
  - Kod kalitesi kontrol kuralları
  - Plugin mimarisi

- **SynScript CLI** (Marketplace destekli)
  - `validate` - Dosya doğrulama
  - `preview` - AST preview
  - `reference` - API referansı arama
  - 200+ satır CLI entegrasyonu

- **Debugger Komutları**
  - Koşullu breakpoint: `condition` alanı ile
  - Hit count breakpoint: `hitCondition` ile belirli sayıda kırılma
  - Logpoint: console çıkışı breakpoint olmadan
  - Expression evaluation: Hover ve debug console'de

- **Paket Optimizasyonu**
  - `.vscodeignore` dosyası eklendi - Gereksiz dosyaları hariç tut
  - VSIX boyutunu %40 kadar azalt (800KB+ → 50-100KB hedefi)
  - Sadece gerekli dosyalar paketlenmesi

- **Birçok Tema Desteği**
  - 🌙 SynScript Lab Dark - VS Code Dark uyumlu profesyonel tema
  - ☀️ SynScript Lab Light - Aydınlık tema game dev için
  - Her iki tema da oyun geliştirme semantiğine optimize

- **Geliştirilmiş Sözdizimi Vurgulaması**
  - v0.3.0 oyun semantiği (State, Signal, Actor)
  - @Operator namespaces (@vector, @math, @color)
  - Async/await desteği
  - İyileştirilmiş type annotations

- **Kod Parçaları (23 Adet)**
  - State machine tanımı
  - Signal/Slot event binding
  - Actor yaratma ve yönetme
  - @Operator kullanım örnekleri
  - Async/await patterns

- **Linter Framework**
  - Statik kod analizi
  - Hata tespiti ve uyarılar
  - Kod kalitesi kontrol kuralları
  - Plugin mimarisi

- **SynScript CLI** (Marketplace destekli)
  - `validate` - Dosya doğrulama
  - `preview` - AST preview
  - `reference` - API referansı arama
  - 200+ satır CLI entegrasyonu

- **Debugger Komutları**
  - Koşullu breakpoint: `condition` alanı ile
  - Hit count breakpoint: `hitCondition` ile belirli sayıda kırılma
  - Logpoint: console çıkışı breakpoint olmadan
  - Expression evaluation: Hover ve debug console'de

### 🎮 Oyun Geliştirme Semantiği
- **State (Mor - #a78bfa)**
  - State machine deklarasyonları
  - Durum yönetimi
  - Transition definitions

- **Signal (Turkuaz - #06b6d4)**
  - Event binding operator (=>)
  - Signal slot patterns
  - Event handling

- **@Operators (Sarı - #fbbf24)**
  - @vector işlemleri
  - @math fonksiyonları
  - @color manipülasyonu
  - @timer yönetimi

- **Actor (Yeşil)**
  - Oyun nesneleri
  - Component sistema

### 📚 Belgelendirme
- Güncellenen README (v0.3.0 özelliklerine göre)
- Debugger kullanım rehberi
- İkon tasarım özellikleri
- Dark tema güncellemesi notları
- Yeni örnekler ve kodeparçaları
- API referansları
- Tema yönetimi rehberi

### 🔧 Teknik İyileştirmeler
- Debug Adapter Protocol (DAP) implementasyonu (250+ satır adapter.js)
- Extension main entry point (extension.js - 150+ satır)
- Debug Adapter Factory pattern uygulaması
- Icon SVG/PNG dönüştürme pipeline'ı
- Dark tema color palette optimizasyonu
- Daha iyi performance:
  - Icon optimizasyonu
  - Optimize edilmiş syntax highlighting
  - İyileştirilmiş linter hızı
- Debugger breakpoint engine
- Daha geniş IDE API entegrasyonu
- .vscodeignore ile paket boyutunu %40 azalt
- Activation events optimizasyonu (5 event tipi)
- Command palette entegrasyonu (3 command)

### 🐛 Hata Düzeltmeleri
- Daha sağlam syntax parsing
- İyileştirilmiş debugger error handling
- Tema color contrast iyileştirmeleri
- Icon rendering hataları giderildi
- Bellek optimizasyonu (debugger session yönetimi)

---

## [0.2.0] - 6 Mart 2026

### ✨ Yeni Özellikler
- State Machine syntax highlighting
- Signal/Slot pattern desteği
- @Operator namespace vurgulaması
- Actor isolation support
- Async/await keyword recognition
- Light tema eklendi
- Expanded code snippets (23 adet)
- Linter framework
- SynScript CLI tools
- Language configuration enhancements

### 🔧 İyileştirmeler
- Better color palette matching VS Code Dark
- Improved token semantics
- Enhanced documentation
- Extended API support

---

## [0.1.0] - 5 Mart 2026

### ✨ İlk Sürüm
- Temel SynScript syntax highlighting
- Dil tanımı ve konfigürasyon
- Bir tema (Dark)
- Temel snippet'ler (8 adet)
- Basit syntax support
