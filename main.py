"""
semua sintaksis dasar bahasa pemrograman terdiri dari :
1. Sekuensial : langkah berurutan
2. Percabangan : langkah melompat jika kondisi terpenuhi
3. Perulangan : mengulang langkah yang sama berkali-kali sampai kondisi terpenuhi
"""

# Sekuensial
print('Ibu berkata : "Pergi ketoko"')
print('Budi menjawab : "Baik apa yang harus saya lakukan ditoko?"')
print('Ibu menjawab : "Beli 1 botol susu, dan jika ada telur beli 6"')
print("Maka budi berangkat ke toko")
print("Dan mulai berbelanja")

# percabangan
print('-' * 20)
print("Percabangan")
print('-' * 20)

susu_tersedia = 100
print(f"jumlah susu tersedia {susu_tersedia} botol")
telur_tersedia = 1000
print(f"jumlah telur tersedia {telur_tersedia} butir")
if susu_tersedia > 0:
    print("Budi cek uang yang dibawa sudah cukup")
    print("Budi membeli satu botol")
    if telur_tersedia > 0:
        print("Budi membeli 6 butir")
else:
    print("Budi tidak jadi membeli")


print("Budi kembali kerumah")
print("Dan menyampaikan hasilnya kepada ibu")
