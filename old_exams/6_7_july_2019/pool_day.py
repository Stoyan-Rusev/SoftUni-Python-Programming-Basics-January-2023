from math import ceil

people = int(input())
entry_tax = float(input())
price_for_a_seat = float(input())
price_for_umbrella = float(input())

umbrellas_count = ceil(people / 2)
seats_count = ceil(0.75 * people)

final_price = people * entry_tax + price_for_a_seat * seats_count + price_for_umbrella * umbrellas_count

print(f"{final_price:.2f} lv")
