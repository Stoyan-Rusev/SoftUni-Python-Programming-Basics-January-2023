ticket_type = input()
rows = int(input())
columns = int(input())

income = 0
cinema_capacity = columns * rows

if ticket_type == "Premiere":
    income = cinema_capacity * 12

elif ticket_type == "Normal":
    income = cinema_capacity * 7.50

elif ticket_type == "Discount":
    income = cinema_capacity * 5

print(f'{income:.2f} leva')

