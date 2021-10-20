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
Hes_sorgulatma.py isimli dosya kullanılacak. Bu program ile Chromium başlatılır ve öncelikle e-devlet sayfasından giriş yapılır. Terminal ekranından giriş için gerekli bilgiler kullanıcıdan istenir.
Başarılı bir şekilde e-devlet girişi yapılmışsa HES kodu sorgulama sayfasına gidilir ve kullanıcının Terminal ekranına girdiği Hes kodu sorgusu yapılarak risk durumu bilgisi ekrana yazdırılır. Sonrasında yeni bir sorgu için Hes kodu girilmesi beklenir ve döngü bu şekilde devam eder.

# Üçüncü Kısım
Hes_sorgu.py isimli dosya kullanılacak. Bu bölüm birinci ve ikinci kısımların kombinasyonundan oluşmaktadır. Program başlatıldığında terminal ekranından e-devlete giriş için kullanıcı bilgilerinin girilmesi istenir ve internet erişimi varsa giriş yapılır. Sonrasında döngü ile kameradan karekod okutulması beklenir, eğer karekod algılanmışsa bilgisi yazı formatına dönüştürülür ve yazı karakteri olarak Hes kodu çıkarılır. Web Browser ile e-devletten Hes kodu sorgusu gerçekleştirilerek Risk durumu hem terminale hemde resimde algılanan karekod üzerine yazdırılır.


# Youtube Eğitim Videoları
Bölüm 1: https://youtu.be/er_XNiuD6w0
Bölüm 2: https://youtu.be/fj0q__0H2-A
Bölüm 3: https://youtu.be/eoRyHBntPMA
