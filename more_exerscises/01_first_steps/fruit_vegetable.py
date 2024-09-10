fruit_price_kg = float(input())
vegetables_price_kg = float(input())
fruit_kg = float(input())
vegetables_kg = float(input())

final_price = (fruit_price_kg * fruit_kg) + (vegetables_price_kg * vegetables_kg)
final_price_euro = final_price / 1.94

print(f"{final_price_euro:.2f}")



