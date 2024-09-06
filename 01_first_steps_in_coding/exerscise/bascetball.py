year_fee = int(input())

shoes = year_fee - 0.4 * year_fee
clothes = shoes - 0.2 * shoes
ball = clothes / 4
accessories_price = ball / 5

total_price_per_year = year_fee + shoes + clothes + ball + accessories_price

print(total_price_per_year)
