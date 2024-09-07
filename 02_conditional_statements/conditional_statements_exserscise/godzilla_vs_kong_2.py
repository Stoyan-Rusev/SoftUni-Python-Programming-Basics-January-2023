budget = float(input())
extras = int(input())
clothes_price_for_an_extra = float(input())

decor = budget * 0.10

if extras > 150:
    clothes_price_for_an_extra *= 0.9

total_expenses = decor + extras * clothes_price_for_an_extra

if total_expenses > budget:
    print("Not enough money!")
    print(f"Wingard needs {abs(budget - total_expenses):.2f} leva more.")

else :
    print("Action!" )
    print(f"Wingard starts filming with {(budget - total_expenses):.2f} leva left.")