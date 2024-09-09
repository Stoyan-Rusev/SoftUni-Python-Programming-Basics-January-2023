n = int(input())

left_count = 0
right_count = 0

for num in range(1, 2 * n + 1):

    number = int(input())

    if num <= n:
        left_count += number
    else:
        right_count += number

if left_count == right_count:
    print(f"Yes, sum = {right_count}")
else:
    print(f"No, diff = {abs(right_count - left_count)}")

