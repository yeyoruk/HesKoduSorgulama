# HesKoduSorgulama
Python ile Karekod okuma ve HES kodu sorgusu

# Açıklama
Bu çalışma Python programlama dilinde oluşturulmuştur.
Raspberry Pi 3 Model B+ ve Pi Kamera ile test edilmiştir.
Çalışma 3 kısımdan oluşturulmuştur; 
 Birinci kısım kamera ile Karekod okuma,
 İkinci kısım e-devlet üzerinden HES kodu sorgulama,
 Üçüncü kısım ise birinci ve ikinci kısımların birleştirilmesiyle kamera ile algılanan HES karekodunun e-devlet üzerinden otomatik sorgusunu gerçekleştirmektedir.
 
# Birinci Kısım
karekod_okuma.py isimli dosya kullanılacak. Kamerada algılanan karekod bilgisi terminale yazdırılır ve aynı zamanda görüntü üzerine yerleştirilir.

# İkinci Kısım
Hes_sorgu.py isimli dosya kullanılacak. Bu program ile Chromium başlatılır ve öncelikle e-devlet sayfasından giriş yapılır. Terminal ekranından giriş için gerekli bilgiler kullanıcıdan istenir.
Başarılı bir şekilde e-devlet girişi yapılmışsa HES kodu sorgulama sayfasına gidilir ve kullanıcının Terminal ekranına girdiği Hes kodu sorgusu yapılarak risk durumu bilgisi ekrana yazdırılır. Sonrasında yeni bir sorgu için Hes kodu girilmesi beklenir ve döngü bu şekilde devam eder.
