import math

# Kullanıcıdan yarıçapı al
yaricap = float(input("Dairenin yarıçapını girin: "))

# Dairenin alanını hesapla (eğer math kütüphanesini kullanmak istemezseniz math.pi kısmını 3 veya 3.17 yazabilirsiniz) 
alan = math.pi * yaricap**2

# Dairenin çevresini hesapla
cevre = 2 * math.pi * yaricap

# Ekrana yazdır
print(f"Dairenin alanı: {alan}")
print(f"Dairenin çevresi: {cevre}")
