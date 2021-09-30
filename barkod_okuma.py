
import imutils
import cv2
import time
from pyzbar import pyzbar
from imutils.video import VideoStream


#vs = VideoStream(src=0).start()  # Webcam kullanılacaksa bu satırı açın alt satırı kapatın
vs = VideoStream(usePiCamera=True).start() # Raspberry Pi Kamera için
time.sleep(3.0)  # Kameranın açılması için süre ver

while True:
    frame = vs.read()        # Görüntüyü oku
    frame = imutils.resize(frame, width=600)
    barcodes = pyzbar.decode(frame)  # Görüntüdeki barkodu çözümle
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect  # Görüntüdeki bakodun sınırlarını belirle
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2) # Borkod sınırlarının etrafını mavi renk ile çiz
        barcodeData = barcode.data.decode("utf-8")  # Barkodu okunabilir yazı formatına dönüştür
        print (barcodeData)   # Okunan barkodu yazdır
        cv2.putText(frame, barcodeData, (x, y + 40),
        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)   # Barkodu resmin üzerine yerleştir
        cv2.imshow("Barkod Okuma", frame)  # Resmi görüntüle
        if cv2.waitKey(1) & 0xFF == ord('s'):  # cv2.imshow ile birlikte kullanılmalıdır
           break