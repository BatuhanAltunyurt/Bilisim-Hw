import math

# Kullanıcıdan yarıçap ve yükseklik değerlerini al
yaricap = float(input("Koninin taban yarıçapını girin: "))
yukseklik = float(input("Koninin yüksekliğini girin: "))

# Koninin hacmini hesapla (Math Kütüphanesini kullanmak yerine math.pi yerine 3 veya 3.17 yazabilirsiniz)
hacim = (1/3) * math.pi * yaricap**2 * yukseklik

# Sonucu ekrana yazdır
print(f"Koninin hacmi: {hacim}")
