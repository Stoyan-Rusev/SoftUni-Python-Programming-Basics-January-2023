chrysanthemum_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
holiday_or_not = input()

chrysanthemum_price = 0
roses_price = 0
tulips_price = 0

if season == "Summer" or season == "Spring":
    chrysanthemum_price = 2.00
    roses_price = 4.10
    tulips_price = 2.50
elif season == "Winter" or season == "Autumn":
    chrysanthemum_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15

bouquet = (chrysanthemum_count * chrysanthemum_price) + (roses_count * roses_price) + (tulips_count * tulips_price)

if holiday_or_not == "Y":
    bouquet *= 1.15

if chrysanthemum_count + roses_count + tulips_count > 20:
    bouquet *= 0.80

if season == "Spring" and tulips_count > 7:
    bouquet *= 0.95
elif season == "Winter" and roses_count >= 10:
    bouquet *= 0.90

bouquet += 2

print(f"{bouquet:.2f}")




