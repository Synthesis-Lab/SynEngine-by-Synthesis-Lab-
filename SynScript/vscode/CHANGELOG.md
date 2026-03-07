# SynScript Language Support - Sürüm Geçmişi

## [0.3.0] - 7 Mart 2026

### ✨ Yeni Özellikler

- **🎨 Profesyonel Ikon Tasarımı (YENİ)**
  - Duck ikonunun kod emblemli yeni tasarımı
  - Sarı başlı ördek + mavi gövde + yeşil `</>` kodu
  - Renkli sparkles (cyan, yeşil) ile dekorasyon
  - VS Code Marketplace'te profesyonel görünüm
  - 128x128 pixel PNG format

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
  - v0.2.0 oyun semantiği (State, Signal, Actor)
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
- Debug Adapter Protocol (DAP) implementasyonu
- Icon SVG/PNG dönüştürme pipeline'ı
- Dark tema color palette optimizasyonu
- Daha iyi performance (Icon optimizasyonu)
- Optimize edilmiş syntax highlighting
- İyileştirilmiş linter hızı
- Debugger breakpoint engine
- Daha geniş IDE API entegrasyonu

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
