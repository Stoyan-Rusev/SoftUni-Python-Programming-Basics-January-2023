fruit = input()
day = input()
quantity_kg = float(input())

price = 0
correct_data = True

if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    if fruit == "banana":
        price = quantity_kg * 2.50
        print(f'{price:.2f}')
    elif fruit == "apple":
        price = quantity_kg * 1.20
        print(f'{price:.2f}')
    elif fruit == "orange":
        price = quantity_kg * 0.85
        print(f'{price:.2f}')
    elif fruit == "grapefruit":
        price = quantity_kg * 1.45
        print(f'{price:.2f}')
    elif fruit == "kiwi":
        price = quantity_kg * 2.70
        print(f'{price:.2f}')
    elif fruit == "pineapple":
        price = quantity_kg * 5.50
        print(f'{price:.2f}')
    elif fruit == "grapes":
        price = quantity_kg * 3.85
        print(f'{price:.2f}')
    else:
        correct_data = False
        if not correct_data:
            print('error')

elif day in ["Saturday", "Sunday"]:
    if fruit == "banana":
        price = quantity_kg * 2.70
        print(f'{price:.2f}')
    elif fruit == "apple":
        price = quantity_kg * 1.25
        print(f'{price:.2f}')
    elif fruit == "orange":
        price = quantity_kg * 0.90
        print(f'{price:.2f}')
    elif fruit == "grapefruit":
        price = quantity_kg * 1.60
        print(f'{price:.2f}')
    elif fruit == "kiwi":
        price = quantity_kg * 3.00
        print(f'{price:.2f}')
    elif fruit == "pineapple":
        price = quantity_kg * 5.60
        print(f'{price:.2f}')
    elif fruit == "grapes":
        price = quantity_kg * 4.20
        print(f'{price:.2f}')
    else:
        correct_data = False
        if not correct_data:
            print('error')

else:
    print('error')






