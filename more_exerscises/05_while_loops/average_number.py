n = int(input())

total_sum = 0

for i in range(n):
    number = int(input())
    total_sum += number

print(f"{total_sum / n:.2f}")
