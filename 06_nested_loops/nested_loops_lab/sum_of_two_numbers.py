x1 = int(input())
x2 = int(input())
magic_number = int(input())

combination_counter = 0
break_condition = False

for num1 in range(x1, x2 + 1):
    for num2 in range(x1, x2 + 1):

        combination_counter += 1
        result = num1 + num2

        if result == magic_number:
            print(f"Combination N:{combination_counter} ({num1} + {num2} = {magic_number})")
            break_condition = True
            break

    if break_condition:
        break

if not break_condition:
    print(f"{combination_counter} combinations - neither equals {magic_number}")
