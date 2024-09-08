type_flower = input()
pieces_flower = int(input())
budget = int(input())

final_price = 0

if type_flower == "Roses":
    if pieces_flower > 80:
        final_price = (pieces_flower * 5) * 0.9
    else:
        final_price = pieces_flower * 5

elif type_flower == "Dahlias":
    if pieces_flower > 90:
        final_price = (pieces_flower * 3.80) * 0.85
    else:
        final_price = pieces_flower * 3.80

elif type_flower == "Tulips":
    if pieces_flower > 80:
        final_price = (pieces_flower * 2.80) * 0.85
    else:
        final_price = pieces_flower * 2.80

elif type_flower == "Narcissus":
    if pieces_flower < 120:
        final_price = (pieces_flower * 3.00) * 1.15
    else:
        final_price = pieces_flower * 3.00

elif type_flower == "Gladiolus":
    if pieces_flower < 80:
        final_price = (pieces_flower * 2.50) * 1.20
    else:
        final_price = (pieces_flower * 2.50)

if budget >= final_price:
    print(f"Hey, you have a great garden with {pieces_flower} {type_flower} and {budget - final_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {final_price - budget:.2f} leva more.")

