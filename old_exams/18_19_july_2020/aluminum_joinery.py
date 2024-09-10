joinery_count = int(input())
type_joinery = input()
with_without_delivery = input()

price = 0
DELIVERY = 60

if type_joinery == "90X130":
    price = 110 * joinery_count

    if joinery_count > 60:
        price = 0.92 * price
    elif joinery_count > 30:
        price = 0.95 * price


elif type_joinery == "100X150":
    price = 140 * joinery_count

    if joinery_count > 80:
        price = 0.90 * price
    elif joinery_count > 40:
        price = 0.94 * price

elif type_joinery == "130X180":
    price = 190 * joinery_count

    if joinery_count > 50:
        price = 0.88 * price
    elif joinery_count > 20:
        price = 0.93 * price

elif type_joinery == "200X300":
    price = 250 * joinery_count

    if joinery_count > 50:
        price = 0.86 * price
    elif joinery_count > 25:
        price = 0.91 * price


if with_without_delivery == "With delivery":
    price += 60


if joinery_count > 99:
    price *= 0.96


if joinery_count < 10:
    print("Invalid order")
else:
    print(f"{price:.2f} BGN")
