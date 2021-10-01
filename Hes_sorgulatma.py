
import time
import selenium
from  selenium import webdriver

global TC,sifre
global Hes_kod,sonuc

sonuc = ""  # herhangi bir ilk değer atıyoruz

TC  =  str(input("TC giriniz: \n"))  # e-devlet girişi için kullanıcıdan TC kimlik no istiyoruz
sifre  =  str(input("e-devlet sifrenizi giriniz: \n"))  # kullanıcıdan e-devlet şifresini istiyoruz

try:
    
    #Chromium başlatıyoruz
    browser = webdriver.Chrome(executable_path = '/usr/lib/chromium-browser/chromedriver')
    
    #e devlet giriş sayfasına git
    browser.get("https://giris.turkiye.gov.tr/Giris/gir")

    #tc no yazma
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="tridField"]').send_keys(TC)
    #şifreyi yaz
    browser.find_element_by_xpath('//*[@id="egpField"]').send_keys(sifre)
    
    try:
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="loginForm"]/div[2]/input[4]').click()  #Giriş düğmesi tıkla
        
    except:
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="loginForm"]/div[2]/input[4]').click()  #Giriş düğmesi tıkla
        
	
    while True:
               #HES kodu sorgulama sayfasına git
               browser.get("https://www.turkiye.gov.tr/saglik-bakanligi-hes-kodu-sorgulama")
               
               #Sorgulanacak Hes kodunu kullanıcıdan iste
               Hes_kod = str(input("HES kodu giriniz: \n"))
               Hes_kod= Hes_kod.upper() # Küçük harf girildiyse büyük harfe dönüştür
               
               time.sleep(1)
               browser.find_element_by_xpath('//*[@id="hes_kodu"]').send_keys(Hes_kod)  #Hes kodunu browserda ilgili alana gir
                                           
               try:
                          time.sleep(3)
                          browser.find_element_by_xpath('//*[@id="contentStart"]/div[3]/form/div/input[1]').click()  #Sorgula düğmesine tıkla
                          
               except:
                          time.sleep(3)
                          browser.find_element_by_xpath('//*[@id="contentStart"]/div[3]/form/div/input[1]').click()  #Sorgula düğmesine tıkla
               
               
               time.sleep(3)
               sonuc=browser.find_element_by_xpath('//*[@id="contentStart"]/div/dl/dd[4]').text   # Risk durumunu bildiren alanı bul ve sonuc değişkenine ata
               print(sonuc)  # Terminal ekranına sonucu yazdır
               

                               
except:
    print("internet yok")
    pass
