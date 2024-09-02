# while True:
#     sayi1 = input("Lütfen birinci sayiyi giriniz: ")
#     sayi2 = input("Lütfen ikinci sayiyi giriniz: ")
#     sayi3 = input("Lütfen üçüncü sayiyi giriniz: ")
#
#     if sayi1 > sayi2 and sayi1 > sayi3:
#         print("Girmiş olduğunuz sayılardan büyük olan sayı: " + sayi1)
#     elif sayi2 > sayi1 and sayi2 > sayi3:
#         print("Girmiş olduğunuz sayılardan büyük olan sayı: " + sayi2)
#     elif sayi3 > sayi1 and sayi3 > sayi2:
#         print("Girmiş olduğunuz sayılardan büyük olan sayı: " + sayi3)
#     else:
#         print("Girmiş olduğunuz sayi değerleri birbirine eşittir")


#
#
# *********************************************************************************************************************************************************************
# import math
# import numpy as np
#
#
# while True:
#     print("******************** Lütfen Alanını Hesaplamak istediğiniz Çokgeni seçiniz ********************")
#
#     print("Üçgene ait alanı hesaplamak için Lütfen 1'e basınız")
#     print("Kareye ait çevre ve alanı hesaplamak için Lütfen 2'ye basınız")
#     print("Daireye ait çevre ve alanı hesaplamak için Lütfen 3'e basınız")
#     print("Yamuka ait çevre ve alanı hesaplamak için Lütfen 4'e basınız")
#     print("\n")
#     secilen = int(input("Lütfen İşlem yapmak istediğiniz çokgene ait değeri giriniz:"))
#
#
#     if secilen == 1:
#         print("ÜÇGEN adlı çokgen için işlem yapmaktasınız!\n")
#         taban = float(input("Lütfen üçgenin taban uzunluk değerini giriniz: "))
#         yukseklik = float(input("Lütfen üçgenin yükseklik değerini giriniz: "))
#         print("\n")
#         alan = taban*yukseklik/2
#         print("Girmiş olduğunuz değerlere ait üçgenin alanı: "+str(alan)+" birimkaredir.\n")
#         input("Ana menüye dönmek için lütfen enter tuşuna basınız")
#
#
#
#     elif secilen == 2:
#         print("KARE adlı çokgen için işlem yapmaktasınız'\n")
#         kenar = float(input("Lütfen KARE'ye ait bir kenar uzunluğu giriniz: "))
#         print("\n")
#         alan = kenar*kenar
#         cevre = kenar*4
#
#         print("Girmiş olduğunuz değerlere ait Karenin alanı: "+str(alan)+" birimkaredir.")
#         print("Girmiş olduğunuz değerlere ait Karenin çevresi: "+str(cevre)+" birimdir.\n")
#         input("Ana menüye dönmek için lütfen enter tuşuna basınız")
#
#
#     elif secilen == 3:
#         print("DAİRE adlı çokgen için işlem yapmaktasınız'\n")
#         cap = float(input("Lütfen DAİRE'ye ait çap uzunluğunu giriniz: "))
#         print("\n")
#         alan = cap * cap*math.pi
#         cevre = 2*math.pi*cap
#
#         print("Girmiş olduğunuz değerlere ait dairenin alanı: " + str(alan) + " birimkaredir.")
#         print("Girmiş olduğunuz değerlere ait dairenin çevresi: " + str(cevre) + " birimdir.\n")
#         input("Ana menüye dönmek için lütfen enter tuşuna basınız")
#
#     elif secilen == 4:
#         print("YAMUK adlı çokgen için işlem yapmaktasınız'\n")
#         usttaban = float(input("Lütfen YAMUK'a a ait üst taban uzunluğunu giriniz: "))
#         alttaban = float(input("Lütfen YAMUK'a a ait alt taban uzunluğunu giriniz: "))
#         yukseklik = float(input("Lütfen YAMUK'a a ait yükseklik değerini giriniz: "))
#         print("\n")
#         alan = (alttaban+usttaban)*yukseklik/2
#         yankenar=np.sqrt(yukseklik*yukseklik+(alttaban-usttaban/2)*(alttaban-usttaban/2))
#         cevre = yankenar*2+alttaban+usttaban
#
#         print("Girmiş olduğunuz değerlere ait dairenin alanı: " + str(alan) + " birimkaredir.")
#         print("Girmiş olduğunuz değerlere ait dairenin çevresi: " + str(cevre) + " birimdir.\n")
#         input("Ana menüye dönmek için lütfen enter tuşuna basınız")
#
#
#     else:
#         print("Girmiş olduğunuz hiçbir değer işlem için uygun değildir")
#         input("Ana menüye dönmek için lütfen enter tuşuna basınız")




# # GİRİLEN SAYIYA KADAR KARELERİNİ ALIP DAHA SONRA EKRANA YAZDIRAN KODU YAZIN
#
# print("GİRİLEN SAYIYA KADAR KARELERİNİ ALIP DAHA SONRA EKRANA YAZDIRMA İŞLEMİ")
#
# sayi1 = int(input("Lütfen bir sayı giriniz: "))
# x=1
# for x in range(1,sayi1+1):
#     cikti = x*x
#     print(cikti)
#


# Girilen SAYIYA KADAR 5'er 5'er yazdırma
#
# sayi1 = int(input("Lütfen bir sayı giriniz: "))
#
# for x in range(1, sayi1+1, 5):
#     print(x)
#
#
#
# DOĞUM TARİHİ GİRİLEN 3 KİŞİNİN YAŞINI HESAPLAYAN PROGRAMI



# from datetime import datetime
#
# # Şu anki tarih ve saati al
# now = datetime.now()
#
# for i in range(1, 4):  # 3 kişiyi almak için range(1, 4)
#     print(f"Lütfen {i}. kişinin doğum tarihi bilgilerini giriniz: ")
#     dogum_yili = int(input("Lütfen doğum yılınızı giriniz: "))
#     dogum_ayi = int(input("Lütfen doğum ayınızı giriniz: "))
#     dogum_gunu = int(input("Lütfen doğum gününüzü giriniz: "))
#
#     # Doğum tarihini datetime nesnesi olarak oluştur
#     dogum_tarihi = datetime(dogum_yili, dogum_ayi, dogum_gunu)
#
#     # Yaşı hesapla
#     yas = now.year - dogum_yili - ((now.month, now.day) < (dogum_ayi, dogum_gunu))
#
#     print(f"{i}. kişinin yaşı: {yas}")
#
# print("Tüm kişilerin yaş hesaplaması tamamlandı.")
#

#
# GİRİLEN 10 ADET SAYIDAN SADECE ÇİFT OLANLARIN KARASİNİ ALIP EKRANA YAZDIRAN PROGRAMI YAZINIZ
#

# print("GİRİLEN 10 ADET SAYIDAN SADECE ÇİFT OLANLARIN KARASİNİ ALIP EKRANA YAZDIRAN PROGRAMI")
#
# numbers = []
#
# n = int(input("Girmek istediğiniz eleman sayısını giriniz:  "))
#
# for i in range(n):
#     number=int(input(f"Lütfen {i+1}.sayi değerini giriniz:"))
#     numbers.append(number)
#
#
# print("Girmiş olduğunuz elemanların sırasıyla listesi: ",numbers)
#
# input("Girmiş olduğunuz çift sayıların karelerini görüntülemek için ENTER tuşuna basınız: ")
#
# for i in range(n):
#
#     if numbers[i]%2==0:
#         kare=numbers[i]*numbers[i]
#         print(f"girilen sayideğerlerinden {i+1}.sayi değeri çift ve karesi: "+str(kare))




#
# # GİRİLEN SAYIYA KADARKİ  ÇİFT OLANLARIN KARASİNİ ALIP EKRANA TOPLAMLARINI YAZDIRAN PROGRAM
# print("GİRİLEN SAYIYA KADARKİ  ÇİFT OLANLARIN KARASİNİ ALIP EKRANA TOPLAMLARINI YAZDIRAN PROGRAM")
#
# sayi=int(input("Lütfen bir sayı giriniz: "))
# toplam=0
# for i in range(1,sayi+1,1):
#     if i%2==0:
#         kare=i*i
#         toplam=kare+toplam
#         print(f"Girmiş olduğunuz sayilardan {i}.sayının karesi: {kare} ")
#
# print("Girmiş olduğunuz sayıya kadarki çift sayıların kareleri toplamı: "+str(toplam))
#
# sayi=15
# print(sayi)
#
# for i in range(3):
#
#     for i in range(2):
#         sayi=sayi+1
#         print(sayi)
#     sayi = sayi + 8
#     print(sayi)
#
#
# #
#
# sayi=15
# print(sayi)
#
# for i in range(3):
#     for i in range(2):
#         sayi=sayi+1
#         print(sayi)
#     for i in range(1):
#         sayi=sayi+8
#         print(sayi)
