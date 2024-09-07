excursion_price = float(input())

puzzles_count = int(input())
talking_dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

PUZZLE_PRICE = 2.60
TALKING_DOLL_PRICE = 3.00
TEDDY_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2.00

total_price = (puzzles_count * PUZZLE_PRICE) + (talking_dolls_count * TALKING_DOLL_PRICE) \
    + (teddy_bears_count * TEDDY_BEAR_PRICE) + (minions_count * MINION_PRICE) \
    + (trucks_count * TRUCK_PRICE)

total_toys_count = puzzles_count + talking_dolls_count + teddy_bears_count + minions_count + trucks_count

money_left = total_price - total_price * 0.10 - excursion_price

if total_toys_count >= 50:
    total_price *= 0.75

if total_price - total_price * 0.10 >= excursion_price:
    print(f"Yes! {money_left} lv left.")
else:
    print(f"Not enough money! {abs(money_left)} lv needed.")
