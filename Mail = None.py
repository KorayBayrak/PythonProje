Mail = None
KullaniciAdi = None
Sifre = None
Ad = None
Soyad = None
#!!!!!!!NOT:Farklı fonksiyondaki Değişkenleri karşılaştırabilmek için fonksiyon dışına tanımlama yapıp fonksiyon içlerinde de global olarak tanımlama yaptım.
stok = {"Deprem Çadırı": 5, "Deprem Battaniyesi": 0, "Gıda Paketi": 7, "Giysi Paketi": 1}

def Kayit_ol():
  global Mail, KullaniciAdi, Sifre, Ad, Soyad
  print("\n***Kayit ol***\n")
  Ad = input("Adiniz: ")
  Soyad = input("Soyadiniz: ")
  KullaniciAdi = input("Kullanici adinizi giriniz: ")
  Mail = input("Mail adresinizi giriniz: ")
  Sifre = input("Sifreniz: ")
  while (len(Sifre) < 8):
    print("Sifreniz 8 karakterden uzun olmalidir")
    Sifre = input("Sifreniz: ")
  print("Kaydiniz Tamamlanmistir. Ana menuye yonlendiriliyorsunuz...")


def Giris_yap():
  global Mail, KullaniciAdi, Sifre,Ad ,Soyad
  print("\n***Uye Girisi***\n")

  Mail_giris = input("Mailinizi Giriniz: ")
  Sifre_giris = input("Sifrenizi Giriniz: ")
  while True:
    if (Mail_giris == Mail and Sifre_giris == Sifre):
      print("Giris Basarili.")
      print(f"Hoşgeldin {Ad} {Soyad}!")
      while True:
        print("\nMenuden Yapmak Istediginiz Islemi Seciniz: ")
        menu2 = input(
          "1-Deprem Yardim Toplama Merkezleri Adres Listesi\n2-Malzeme Yardimi Talep Et\n3-Malzeme yardimi yap\n4-Cikis\nSeciminiz: ")
        menu2 = int(menu2)

        if menu2 == 1:
            # Sözlük yapısı
            Adresler = {
                "Mugla": "Konacık Mahallesi Atatürk Bulvarı No:144",
                "Istanbul": "Yunus Emre Mahallesi Hüma Caddesi No:19",
                "Ankara": "Ostim OSB",
                "Izmir": "Gaziemir Fuar Merkezi",
                "Adana": "Yuzuncuyil 85197.Sokak"
            }
            print("*****Deprem Yardım Toplama Merkezleri Adres Listesi*****")
            for i in Adresler:
                print(i, "------->", Adresler[i])
        elif menu2 == 2:
            print("*****Malzeme Yardımı Talep Etme Sayfası*****")
            global stok
            for i in stok:
                print(i)
            print("1-Malzeme ihtiyacım var\n2-Ana Menüye Dön")
            secim1 = input("Seçiminiz: ")
            if secim1 == "1":
                secim2 = input("Menüden istediğiniz malzemeyi yazınız (Çadır/Battaniye/Gıda/Giysi): ")
                if secim2.lower() == "çadır":
                    if stok["Deprem Çadırı"] > 0:
                        print("*********\nTalebiniz oluşturuldu.\n*********")
                        stok_azalt(stok["Deprem Çadırı"])
                    else:
                        print("Ürün stoklarda yok.")
                elif secim2.lower() == "battaniye":
                    if stok["Deprem Battaniyesi"] > 0:
                        print("*********\nTalebiniz oluşturuldu.\n*********")
                        stok_azalt(stok["Deprem Battaniyesi"])
                    else:
                        print("Ürün stoklarda yok.")
                elif secim2.lower() == "gıda":
                    if stok["Gıda Paketi"] > 0:
                        print("*********\nTalebiniz oluşturuldu.\n*********")
                        stok_azalt(stok["Gıda Paketi"])
                    else:
                        print("Ürün stoklarda yok.")
                elif secim2.lower() == "giysi":
                    if stok["Giysi Paketi"] > 0:
                        print("*********\nTalebiniz oluşturuldu.\n*********")
                        stok_azalt(stok["Giysi Paketi"])
                    else:
                        print("Ürün stoklarda yok.")
            else:
                print("Geçersiz seçim.")
        elif menu2 == 3:
          print("*****Malzeme yardimi yapma Sayfasi*****")
          for i in stok:
                print(i)
          secim3=input("Yardımda bulunmak istediğiniz ürünü yazınız(Çadır/Battaniye/Gıda/Giysi): ")
          if secim3.lower() == "çadır":
            stok_arttır(stok["Deprem Çadırı"])
            print("Bağışınız için teşekkürler.")
          elif secim3.lower() == "battaniye":
            stok_arttır(stok["Deprem Battaniyesi"])
            print("Bağışınız için teşekkürler.")
          elif secim3.lower() == "gıda":
            stok_arttır(stok["Gıda Paketi"])
            print("Bağışınız için teşekkürler.")
          elif secim3.lower() == "giysi":
            stok_arttır(stok["Giysi Paketi"])
            print("Bağışınız için teşekkürler.")
          else:
                print("Geçersiz seçim.")
        elif menu2 == 4:
          print("Cikis Yapiliyor...")
          break
        else:
          print("Gecersiz secim. Lutfen tekrar deneyin.")
      break
    else:
      print("Giris basarisiz. Bilgilerinizi Kontrol ediniz...")
      Mail_giris = input("Mailinizi Giriniz: ")
      Sifre_giris = input("Sifrenizi Giriniz: ")


def Sifre_unuttum():
  global Mail, KullaniciAdi
  print("Sifrenizi ogrenmek icin bilgilerinizi giriniz.")
  Mail_unuttum = input("Mail: ")
  Kullanici_unuttum = input("Kullanici adi: ")
  while True:
    if (Mail_unuttum == Mail and Kullanici_unuttum == KullaniciAdi):
      print(
        "Giris bilgileriniz mailinize gönderilmistir. Ana menuye yonlendiriliyorsunuz..."
      )
      break
    else:
      print("Kayitli Hesap bulunamamistir. Ana menuye yonlendiriliyorsunuz...")
      break


def Yonetici_girisi():
  global Mail, KullaniciAdi, Sifre
  print("\n***Yonetici Giris Ekranı***\n")
  YoneticiAdi = input("Yonetici Kullanici Adi: ")
  YoneticiSifre = input("Yonetici Sifresi: ")
  while True:
    if (YoneticiAdi == "yonetici" and YoneticiSifre == "123456"):
      print("Giris Basarili. Yonetici Menusune Yonlendiriliyorsunuz...")
      break
    else:
      print("Giris basarisiz. Bilgilerinizi Kontrol ediniz...")
      YoneticiAdi = input("Yonetici Kullanici Adi: ")
      YoneticiSifre = input("Yonetici Sifresi: ")

def stok_arttır(ürün):
    global stok
    if ürün in stok:
      stok[ürün] += 1
            
def stok_azalt(ürün):
    global stok
    if ürün in stok:
        if stok[ürün] > 0:
            stok[ürün] -= 1
            if stok[ürün] < 0:
                stok[ürün] = 0
          
while True:
  print("\nMenuden Yapmak Istediginiz Islemi Seciniz: ")
  menu1 = input(
    "1-Sisteme Kayit Ol\n2-Sisteme Giris Yap\n3-Sifremi Unuttum\n4-Yonetici Girisi\n5-Cikis\nSeciminiz: "
  )
  menu1 = int(menu1)

  if menu1 == 1:
    Kayit_ol()
  elif menu1 == 2:
    Giris_yap()
  elif menu1 == 3:
    Sifre_unuttum()
  elif menu1 == 4:
    Yonetici_girisi()
  elif menu1 == 5:
    print("Uygulamadan cikiliyor...")
    break
  else:
    print("Gecersiz secim. Lutfen tekrar deneyin.")
