searched_book = input()
books_count = int(input())
counter = 0
is_book_found = False

while books_count > 0:
    current_book = input()
    books_count -= 1
    if current_book == searched_book:
        is_book_found = True
        break
    counter += 1

if is_book_found:
    print(f'You checked {counter} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {counter} books.')