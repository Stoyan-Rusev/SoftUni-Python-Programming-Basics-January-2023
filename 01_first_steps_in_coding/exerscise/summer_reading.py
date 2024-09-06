book_pages = int(input())
pages_per_hour = int(input())
days_for_a_book = int(input())

hours_for_one_book = book_pages / pages_per_hour
hours_per_day = hours_for_one_book / days_for_a_book

print(int(hours_per_day))
