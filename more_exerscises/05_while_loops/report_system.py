expected_money = int(input())

money = 0
i = 1
card_money = 0
cash_money = 0
people_card = 0
people_cash = 0

while money < expected_money:
    product = input()

    if product == "End":
        print("Failed to collect required money for charity.")
        break

    product = int(product)

    # with card:
    if i % 2 == 0:
        if product < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            money += product
            card_money += product
            people_card += 1

    # cash
    else:
        if product > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            money += product
            cash_money += product
            people_cash += 1

    i += 1

else:
    print(f"Average CS: {cash_money / people_cash:.2f}")
    print(f"Average CC: {card_money / people_card:.2f}")
