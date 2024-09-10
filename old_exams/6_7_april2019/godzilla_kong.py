budget = float(input())
statists = int(input())
clothes_for_person_price = float(input())

DECOR = 0.1 * budget

if statists > 150:
    clothes_for_person_price *= 0.9

clothes_total = statists * clothes_for_person_price
total_cost = clothes_total + DECOR

if total_cost > budget:
    print("Not enough money!")
    print(f"Wingard needs {total_cost - budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget - total_cost:.2f} leva left.")
