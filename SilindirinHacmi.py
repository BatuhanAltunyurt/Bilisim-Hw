import math

# Kullanıcıdan yarıçap ve yükseklik değerlerini al
yaricap = float(input("Silindirin taban yarıçapını girin: "))
yukseklik = float(input("Silindirin yüksekliğini girin: "))

# Silindirin hacmini hesapla (eğer math kütüphanesini kullanmak istemezseniz math.pi yerine 3 veya 3.17 yazabilirsiniz)
hacim = math.pi * yaricap**2 * yukseklik

# Sonucu ekrana yazdır
print(f"Silindirin hacmi: {hacim}")
