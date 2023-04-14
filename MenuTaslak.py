Mail = None
KullaniciAdi = None
Sifre = None
#!!!!!!!NOT:Farklı fonksiyondaki Değişkenleri karşılaştırabilmek için fonksiyon dışına tanımlama yapıp fonksiyon içlerinde de global olarak tanımlama yaptım.


def Kayit_ol():
  global Mail, KullaniciAdi, Sifre
  print("\n***Kayit ol***\n")
  Ad = input("Adiniz: ")
  Soyad = input("Soyadiniz: ")
  KullaniciAdi = input("Kullanici adinizi giriniz: ")
  Mail = input("Mail adresinizi giriniz: ")
  Sifre = input("Sifreniz: ")
  while (len(Sifre) < 8):
    print("Sifreniz 8 karakterden buyuk olmalidir")
    Sifre = input("Sifreniz: ")
  print("Kaydiniz Tamamlanmistir. Ana menuye yonlendiriliyorsunuz...")


def Giris_yap():
  global Mail, KullaniciAdi, Sifre
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
          "1-Deprem Aninda Neler Yapmaliyiz?\n2-Ilk Yardim Nasil Yapilir?\n3-Cikis\nSeciminiz: "
        )
        menu2 = int(menu2)

        if menu2 == 1:
          print("Deprem aninda yapilacaklar...")
        elif menu2 == 2:
          print("Ilk yardim nasil yapilir...")
        elif menu2 == 3:
          print("Uygulamadan cikiliyor...")
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


print("\n*****DEPREM YARDIM UYGULAMASI*****\n")

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
