age = int(input())
washer_price = float(input())
single_toy_price = int(input())

money = 0

for _ in range(age):
    if age % 2 == 0:
        money += 10
    else:
        money += single_toy_price


print(money)

