turns = int(input())

result = 0

from_zero_to_nine = 0
from_ten_to_nineteen = 0
from_twenty_to_twenty_nine = 0
from_thirty_to_thirty_nine = 0
from_forty_to_fifty = 0
invalid_number = 0

for i in range(1, turns + 1):
    number = int(input())

    if number < 0 or number > 50:
        result /= 2
        invalid_number += 1
    elif number <= 9:
        result += 0.2 * number
        from_zero_to_nine += 1
    elif number <= 19:
        result += 0.3 * number
        from_ten_to_nineteen += 1
    elif number <= 29:
        result += 0.4 * number
        from_twenty_to_twenty_nine += 1
    elif number <= 39:
        result += 50
        from_thirty_to_thirty_nine += 1
    else:
        result += 100
        from_forty_to_fifty += 1

total_amount_of_numbers = from_zero_to_nine + from_ten_to_nineteen + from_twenty_to_twenty_nine \
    + from_thirty_to_thirty_nine + from_forty_to_fifty + invalid_number

print(f"{result:.2f}")
print(f"From 0 to 9: {from_zero_to_nine / total_amount_of_numbers * 100:.2f}%")
print(f"From 10 to 19: {from_ten_to_nineteen / total_amount_of_numbers * 100:.2f}%")
print(f"From 20 to 29: {from_twenty_to_twenty_nine / total_amount_of_numbers * 100:.2f}%")
print(f"From 30 to 39: {from_thirty_to_thirty_nine / total_amount_of_numbers * 100:.2f}%")
print(f"From 40 to 50: {from_forty_to_fifty / total_amount_of_numbers * 100:.2f}%")
print(f"Invalid numbers: {invalid_number / total_amount_of_numbers * 100:.2f}%")

