"""
Looping for read books
"""
book_count = 10
print('Mother said : "Read all your book"')

book_read = 0
print(f"count book already readed is {book_read}")
while book_read < book_count:
    book_read = book_read + 1
    print(f"book {book_read} already read")

print(f"now i have readed {book_read} books")
