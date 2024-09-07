budget = float(input())
extras = int(input())
clothes_price_for_an_extra = float(input())

decor = budget * 0.10

total_clothes_price = extras * clothes_price_for_an_extra
total_expenses = budget + total_clothes_price

if extras > 150:
    total_clothes_price *= 0.9

if total_expenses > budget:
    print("Not enough money!")
    print(f"Wingard needs {abs(budget - total_expenses):.2f} leva more.")

else :
    print("Action!" )
    print(f"Wingard starts filming with {(budget - total_expenses):.2f} leva left.")
