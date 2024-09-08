days_to_stay = int(input())
room_type = input()
rating = input()

with_discount = 0
price_for_night = 0
nights_to_stay = days_to_stay - 1
final_price = 0

if room_type == "room for one person":
    price_for_night = 18.00
elif room_type == "apartment":
    price_for_night = 25.00
elif room_type == "president apartment":
    price_for_night = 35.00

final_price = price_for_night * nights_to_stay

if room_type == "apartment":
    if days_to_stay < 10:
        final_price *= 0.70
    elif days_to_stay <= 15:
        final_price *= 0.65
    elif days_to_stay > 15:
        final_price *= 0.50

elif room_type == "president apartment":
    if days_to_stay < 10:
        final_price *= 0.90
    elif days_to_stay <= 15:
        final_price *= 0.85
    elif days_to_stay > 15:
        final_price *= 0.80

if rating == "positive":
    with_discount = final_price + 0.25 * final_price
elif rating == "negative":
    with_discount = final_price - final_price * 0.1


print(f"{with_discount:.2f}")