from math import ceil
from math import floor

MAGNOLIAS_PRICE = 3.25
HYACINTH_PRICE = 4.00
ROSES_PRICE = 3.50
CACTUS_PRICE = 8.00

magnolias_count = int(input())
hyacinth_count = int(input())
roses_count = int(input())
cactus_count = int(input())
gift_price = float(input())

total_price = magnolias_count * MAGNOLIAS_PRICE \
    + hyacinth_count * HYACINTH_PRICE \
    + roses_count * ROSES_PRICE \
    + cactus_count * CACTUS_PRICE

maria_money = 0.95 * total_price

if maria_money >= gift_price:
    print(f"She is left with {floor(maria_money - gift_price)} leva.")

else:
    print(f"She will have to borrow {ceil(gift_price - maria_money)} leva.")


