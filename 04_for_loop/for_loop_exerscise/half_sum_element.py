n = int(input())

sum_number = 0
max_number = float('-inf')

for _ in range(n):
    number = int(input())

    if number > max_number:
        max_number = number

    sum_number += number

if max_number == sum_number / 2:
    print(f"Yes\nSum = {max_number}")

else:
    print(f"No\nDiff = {abs(max_number - (sum_number - max_number))}")





