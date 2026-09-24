# Telegram Botu — GitHub Actions ile Ücretsiz 7/24 Çalıştırma

Bu yöntemde bilgisayarını açık tutmana gerek yok. GitHub, senin yerine
zamanlanmış şekilde mesajı otomatik gönderir. Tamamen ücretsiz, kredi
kartı istemez.

## 1. Yeni bir GitHub reposu oluştur

1. github.com'da oturum aç.
2. Sağ üstteki **+** işaretine tıkla → **New repository**.
3. Repo adı: `telegram-bot` (istediğin bir isim de olur).
4. **Private** seçili kalsın.
5. **Create repository** butonuna bas.

## 2. Dosyaları yükle

1. Repo sayfasında **"uploading an existing file"** linkine tıkla
   (veya **Add file → Upload files**).
2. Bu klasördeki **tüm dosya ve klasörleri** (özellikle `.github` klasörü dahil,
   içindeki `workflows` klasörüyle birlikte) sürükleyip bırak.
3. Alt kısımda **Commit changes** butonuna bas.

## 3. Gizli bilgileri (token, gruplar, mesaj) ekle

1. Repo sayfasında **Settings** sekmesine git.
2. Sol menüden **Secrets and variables → Actions**.
3. **New repository secret** butonuyla sırayla şu 3 secret'ı ekle:

   **BOT_TOKEN**
   ```
   8681526533:AAE8mtaA9jV43ij3_rW8Wi1C9Wd9dE_Qeuk
   ```

   **CHAT_ID** (7 grup, virgülle ayrılmış)
   ```
   -1004372817514,-1001756946689,-1001546286218,-1001835906030,-1001971380910,-1002277923588,-1003753999641
   ```

   **MESSAGE_TEXT**
   ```
   ‼️ DOLANDIRICILIK UYARISI ‼️

   <u>Önerdiğimiz sitelerin Telegram üzerinden herhangi bir destek hattı bulunmamaktadır.</u>

   'Site destek ekibiyim', 'Destek yetkilisiyim' vb. ifadelerle size özelden mesaj atan hesapların SAHTE VE DOLANDIRICI olduğunu unutmayın!

   ⚠️ GRUBUMUZDA MODERATÖRLERİMİZİN BİREBİR TAKLİDİNİ YAPAN SAHTE HESAPLAR BULUNMAKTADIR!

   Bu kişiler, ilk fırsatta size özelden mesaj atarak güveninizi kazanmaya ve sizi dolandırmaya çalışabilir.

   <u>🚫 Size özelden mesaj atan ve kendisini destek ekibi veya moderatör olarak tanıtan kişilere KESİNLİKLE İNANMAYIN!</u>

   🔒 ŞÜPHELİ HESAPLARA PARA, SMS, CASHBACK, ŞİFRE VEYA KİŞİSEL BİLGİLERİNİZİ GÖNDERMEYİN.

   ‼️ GÜVENLİĞİNİZ İÇİN ÖZEL MESAJLARA DİKKAT EDİN! ‼️
   ```
   (Bu kutuya olduğu gibi, satır satır yapıştır — GitHub'ın Secrets kutusu çok satırlı
   metni sorunsuz kabul eder, `.env` dosyasındaki gibi tırnak/kaçış karakteri sorunu
   burada hiç yaşanmaz.)

   Her biri için: Name kutusuna ismi yaz, Value kutusuna değeri yapıştır,
   **Add secret** butonuna bas.

## 4. Zamanlama zaten ayarlı

`.github/workflows/telegram-mesaj.yml` dosyasında zamanlama Türkiye saatiyle
**11:00 - 23:00 arası, saatte bir** olacak şekilde ayarlandı. Değiştirmek
istersen dosyayı GitHub üzerinde aç, kalem ikonuyla düzenle, içindeki
`cron` satırını değiştir (GitHub UTC kullanır, Türkiye UTC+3):
- 30 dakikada bir: `- cron: "*/30 8-20 * * *"`
- 2 saatte bir: `- cron: "0 8-20/2 * * *"`

## 5. Test et

1. Repo sayfasında **Actions** sekmesine git.
2. Sol tarafta **"Telegram Otomatik Mesaj"** iş akışına tıkla.
3. Sağ tarafta **Run workflow** butonuna bas → tekrar **Run workflow** de.
4. Birkaç saniye sonra 7 gruba da mesaj düşmesi lazım.

Bu şekilde manuel test ettikten sonra, GitHub belirlenen saatlerde
otomatik olarak çalışmaya devam edecek — bilgisayarın kapalı olsa bile.

## Notlar

- Mesaj metnini veya grupları değiştirmek istersen sadece ilgili secret'ı
  güncellemen yeterli, dosyalara dokunmana gerek yok.
- GitHub'ın zamanlanmış görevleri bazen birkaç dakika gecikmeli
  tetiklenebilir, bu normaldir.
- Bundan sonra bilgisayarındaki `python bot.py` yöntemine gerek kalmıyor,
  o pencereyi kapatabilirsin.
