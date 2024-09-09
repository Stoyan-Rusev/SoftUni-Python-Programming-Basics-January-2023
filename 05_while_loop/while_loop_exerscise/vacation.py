vacation_price = float(input())
money = float(input())

money_left = money
days = 0
days_spending_money = 0

while True:
    command = input()
    capital = float(input())

    if command == "save":
        money_left += capital
        days_spending_money = 0

    elif command == "spend":
        if money_left <= capital:
            money_left = 0
            days_spending_money += 1
        else:
            money_left -= capital
            days_spending_money += 1

    days += 1

    if money_left >= vacation_price:
        print(f"You saved the money for {days} days.")
        break

    if days_spending_money == 5:
        print("You can't save the money.")
        print(f"{days}")
        break
