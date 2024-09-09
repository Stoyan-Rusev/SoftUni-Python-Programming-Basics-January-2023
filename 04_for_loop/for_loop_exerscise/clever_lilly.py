years = int(input())
washing_machine_price = float(input())
single_toy_price = int(input())

money_given = 10
taken_from_brother = 1
saved_money = 0

for age in range(1, years + 1):
    if age % 2 == 0:
        saved_money += money_given - taken_from_brother
        money_given += 10
    else:
        saved_money += single_toy_price

if saved_money >= washing_machine_price:
    print(f"Yes! {saved_money - washing_machine_price:.2f}")

else:
    print(f"No! {washing_machine_price - saved_money:.2f}")


