budget = float(input())
season = input()

place_to_stay = None
destination = None
money_spent = 0

if season == "summer":
    place_to_stay = "Camp"
else:
    place_to_stay = "Hotel"

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        money_spent = budget * 0.3
    elif season == "winter":
        money_spent = budget * 0.7

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        money_spent = budget * 0.4
    elif season == "winter":
        money_spent = budget * 0.8

else:
    destination = "Europe"
    money_spent = budget * 0.9

if destination == "Europe":
    place_to_stay = "Hotel"

print(f"Somewhere in {destination}")
print(f"{place_to_stay} - {money_spent:.2f}")

