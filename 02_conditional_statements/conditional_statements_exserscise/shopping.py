budget = float(input())
videocard_count = int(input())
processor_count = int(input())
ram_count = int(input())

VIDEOCARD_PRICE = 250
PROCESSOR_PRICE = 0.35 * (videocard_count * VIDEOCARD_PRICE)
RAM_PRICE = 0.10 * (videocard_count * VIDEOCARD_PRICE)

total_price = videocard_count * VIDEOCARD_PRICE \
    + processor_count * PROCESSOR_PRICE \
    + ram_count * RAM_PRICE

if videocard_count > processor_count:
    total_price *= 0.85

if budget >= total_price:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")
