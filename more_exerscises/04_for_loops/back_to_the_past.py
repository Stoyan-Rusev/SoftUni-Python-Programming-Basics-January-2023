cash = float(input())
last_year_living = int(input())

age = 18
money_spent = 0

for year in range(1800, last_year_living + 1):
    if year % 2 == 0:
        money_spent += 12000
        age += 1
    else:
        money_spent += 12000 + 50 * age
        age += 1

if cash >= money_spent:
    print(f"Yes! He will live a carefree life and will have {cash - money_spent:.2f} dollars left.")
else:
    print(f"He will need {money_spent - cash:.2f} dollars to survive." )


