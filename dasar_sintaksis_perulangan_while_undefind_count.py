"""
Looping for read books
"""
book_count = 10
print("Mom said : read all your book until you understood")

understood_count = 0
print(f'All books already read and understood is {understood_count}')

read_count = 0

while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 9:
        print(f'the book {understood_count + 1}th not understood')

    else:
        understood_count = understood_count + 1
        print(f'book {understood_count} already read and understood')

print(f'so i have read and understood just {understood_count} books')

if understood_count == book_count:
    print('Mom i have read and understood all of books')
else:
    print(f'mom i can not read and understand all of books i just can read {understood_count} books')
