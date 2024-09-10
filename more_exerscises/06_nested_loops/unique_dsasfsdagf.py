first_num_max_range = input()
second_num_max_range = input()
third_num_max_range = input()

for num in range(222, 878 + 1):
    break_condition = False
    pin = ""

    for index, digit in enumerate(str(num)):

        if index == 0:
            if int(digit) % 2 != 0 or digit > first_num_max_range or int(digit) == 0:
                break_condition = True
                break
            else:
                pin += digit

        elif index == 1:
            if digit > second_num_max_range or int(digit) == 0:
                break_condition = True
                break
            else:
                pin += digit

        elif index == 2:
            if int(digit) % 2 != 0 or digit > third_num_max_range or int(digit) == 0:
                break_condition = True
                break
            else:
                pin += digit

    if break_condition:
        continue
    print(pin)
