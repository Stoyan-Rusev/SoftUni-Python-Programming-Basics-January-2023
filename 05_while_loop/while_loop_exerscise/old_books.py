book_name = input()
current_book = input()

books_checked = 0

while current_book != book_name:
    if current_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {books_checked} books.")
        break

    current_book = input()
    books_checked += 1

if current_book == book_name:
    print(f"You checked {books_checked} books and found it.")
