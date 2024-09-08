budget = int(input())
season = input()
fisherman_count = int(input())

price_for_boat = 0

if season == "Spring":
    price_for_boat = 3000
elif season == "Winter":
    price_for_boat = 2600
else:
    price_for_boat = 4200

if fisherman_count <= 6:
    price_for_boat *= 0.90
elif fisherman_count <= 11:
    price_for_boat *= 0.85
elif fisherman_count >= 12:
    price_for_boat *= 0.75

if season != "Autumn" and fisherman_count % 2 == 0:
    price_for_boat *= 0.95

if budget >= price_for_boat:
    print(f"Yes! You have {budget - price_for_boat:.2f} leva left.")
else:
    print(f"Not enough money! You need {price_for_boat - budget:.2f} leva.")


