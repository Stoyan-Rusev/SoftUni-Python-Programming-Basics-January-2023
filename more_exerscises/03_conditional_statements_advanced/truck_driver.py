season = input()
km_for_month = float(input())

money_for_km = 0

if km_for_month <= 5000:
    if season == "Spring" or season == "Autumn":
        money_for_km = 0.75
    elif season == "Summer":
        money_for_km = 0.90
    else:
        money_for_km = 1.05

elif 5000 < km_for_month <= 10000:
    if season == "Spring" or season == "Autumn":
        money_for_km = 0.95
    elif season == "Summer":
        money_for_km = 1.10
    else:
        money_for_km = 1.25

elif 10000 < km_for_month <= 20000:
    money_for_km = 1.45

salary = money_for_km * km_for_month
final_money = salary * 4 * 0.90

print(f"{final_money:.2f}")



