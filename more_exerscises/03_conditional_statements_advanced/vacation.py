budget = float(input())
season = input()

place_to_stay = None
location = None
price = 0

if budget <= 1000:
    place_to_stay = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = 0.65 * budget
    elif season == "Winter":
        location = "Morocco"
        price = 0.45 * budget


elif 1000 < budget <= 3000:
    place_to_stay = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = 0.80 * budget
    elif season == "Winter":
        location = "Morocco"
        price = 0.60 * budget

else:
    place_to_stay = "Hotel"
    if season == "Summer":
        location = "Alaska"
    elif season == "Winter":
        location = "Morocco"
    price = 0.90 * budget

print(f"{location} - {place_to_stay} - {price:.2f}")

