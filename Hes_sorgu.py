"""
@author: yeyoruk
@source code and info: https://github.com/yeyoruk/HesKoduSorgulama

>> python Hes_sorgu.py
"""

import imutils
import cv2
import time
from pyzbar import pyzbar
from imutils.video import VideoStream

import selenium
from  selenium import webdriver

global Hes_kod,sonuc

#vs = VideoStream(src=0).start()  # Webcam kullanılacaksa bu satırı açın alt satırı kapatın
vs = VideoStream(usePiCamera=True).start() # Raspberry Pi Kamera için
time.sleep(1)  # Kameranın açılması için süre ver

sonuc = ""  # herhangi bir ilk değer atıyoruz

TC  =  str(input("TC giriniz: \n"))  # e-devlet girişi için kullanıcıdan TC kimlik no istiyoruz
sifre  =  str(input("e-devlet sifrenizi giriniz: \n"))  # kullanıcıdan e-devlet şifresini istiyoruz

try:
    
    #Chromium başlatıyoruz
    browser = webdriver.Chrome(executable_path = '/usr/lib/chromium-browser/chromedriver')
    
    time.sleep(1)
    #e devlet giriş sayfasına git
    browser.get("https://giris.turkiye.gov.tr/Giris/gir")
    
    #tc no yazma
    time.sleep(5)
    browser.find_element_by_xpath('//*[@id="tridField"]').send_keys(TC)
    #şifreyi yaz
    browser.find_element_by_xpath('//*[@id="egpField"]').send_keys(sifre)
    
    try:
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="loginForm"]/div[2]/input[4]').click()  #Giriş düğmesi tıkla
        
    except:
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="loginForm"]/div[2]/input[4]').click()  #Giriş düğmesi tıkla
    
    time.sleep(5)
    #HES kodu sorgulama sayfasına git
    browser.get("https://www.turkiye.gov.tr/saglik-bakanligi-hes-kodu-sorgulama")
    
    while True:
          frame = vs.read()        # Görüntüyü oku
          frame = imutils.resize(frame, width=600)
          barcodes = pyzbar.decode(frame)  # Görüntüdeki kodu çözümle
          for barcode in barcodes:
              
              
              (x, y, w, h) = barcode.rect  # Görüntüdeki kodun sınırlarını belirle
              
              barcodeData = barcode.data.decode("utf-8")  # Kodu okunabilir yazı formatına dönüştür
              barcodeData = "{}".format(barcodeData[-10:])
              print (barcodeData)   # Okunan barkodu yazdır 
              Hes_kod= barcodeData.upper() # Küçük harf ise büyük harfe dönüştür
              
              cv2.imshow("HES Sorgu", frame)  # Karekod resmini görüntüle
              if cv2.waitKey(1) & 0xFF == ord('s'):  # cv2.imshow ile birlikte kullanılmalıdır
                 break
                 
              browser.find_element_by_xpath('//*[@id="hes_kodu"]').send_keys(Hes_kod)  #Hes kodunu browserda ilgili alana gir
              
              try:
                 time.sleep(3)
                 browser.find_element_by_xpath('//*[@id="contentStart"]/div[3]/form/div/input[1]').click()  #Sorgula düğmesine tıkla
                          
              except:
                 time.sleep(3)
                 browser.find_element_by_xpath('//*[@id="contentStart"]/div[3]/form/div/input[1]').click()  #Sorgula düğmesine tıkla
               
              
              time.sleep(5)
              sonuc=browser.find_element_by_xpath('//*[@id="contentStart"]/div/dl/dd[5]').text   # Risk durumunu bildiren alanı bul ve sonuc değişkenine ata
              print(sonuc)  # Terminal ekranına sonucu yazdır
              
              if sonuc == "Riskli":	  
                 sonuc="Riskli"
                 cv2.putText(frame, sonuc, (x+10, y+40),
                 cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                 cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
              else:
                 sonuc="Risksiz"
                 cv2.putText(frame, sonuc, (x+10, y+40),
                 cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                 cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                 
              
              cv2.imshow("HES Sorgu", frame)  # Resmi görüntüle
              if cv2.waitKey(1) & 0xFF == ord('s'):  # cv2.imshow ile birlikte kullanılmalıdır
                 break
              
              browser.get("https://www.turkiye.gov.tr/saglik-bakanligi-hes-kodu-sorgulama")
             
except:
    print("internet problemi")
    pass
