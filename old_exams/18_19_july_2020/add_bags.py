baggage_over_20kg_price = float(input())
kg_baggage = float(input())
days_to_departure = int(input())
num_luggage = int(input())

tax = 0

if kg_baggage < 10:
    tax = 0.2 * baggage_over_20kg_price
elif kg_baggage <= 20:
    tax = 0.5 * baggage_over_20kg_price
else:
    tax = baggage_over_20kg_price

if days_to_departure > 30:
    tax += 0.1 * tax
elif 7 <= days_to_departure <= 30:
    tax += 0.15 * tax
else:
    tax += 0.4 * tax

price_for_baggage = tax * num_luggage

print(f" The total price of bags is: {price_for_baggage:.2f} lv. ")
