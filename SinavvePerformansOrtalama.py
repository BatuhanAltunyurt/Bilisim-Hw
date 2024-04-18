# Kullanıcıdan notları al
sinav1 = float(input("İlk sınav notunu girin: "))
sinav2 = float(input("İkinci sınav notunu girin: "))
performans1 = float(input("İlk performans notunu girin: "))
performans2 = float(input("İkinci performans notunu girin: "))

# Not ortalamasını hesapla
ortalama = (sinav1 + sinav2 + performans1 + performans2) / 4

# Sonucu ekrana yazdır
print(f"Öğrencinin not ortalaması: {ortalama}")
