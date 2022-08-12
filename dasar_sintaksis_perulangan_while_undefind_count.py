"""
Looping for read books
"""
book_count = 10
print("Ibu berkata, baca smua buku !")
read_count = 0

understood_count = 0
print(f"jumlah buku yang sudah dibaca dan difahami {understood_count}")

while read_count < book_count * 2:
    read_count = read_count + 1

    if understood_count == 9:
        print(f"Buku ke {understood_count + 1} belum faham")
    else:
        understood_count = understood_count + 1
        print(f"Buku ke {understood_count} sudah dibaca dan difahami")

    print(f"Jumlah buku yang sudah dibaca dan difahami : {understood_count}")
    if understood_count == book_count:
        print("Budi sudah membaca dan memahami semua buku")
    else:
        print(f'"Bu, Budi hanya baru membaca {understood_count} buku"')