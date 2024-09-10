budget = float(input())
ticket_category = input()
ultras_count = int(input())

price_for_ticket = 0
transport_price = 0

if ticket_category == "VIP":
    price_for_ticket = 499.99
elif ticket_category == "Normal":
    price_for_ticket = 249.99

if 1 <= ultras_count <= 4:
    transport_price = budget * 0.75
elif 5 <= ultras_count <= 9:
    transport_price = budget * 0.60
elif 10 <= ultras_count <= 24:
    transport_price = budget * 0.50
elif 25 <= ultras_count <= 49:
    transport_price = budget * 0.40
elif ultras_count > 50:
    transport_price = budget * 0.25

total_cost = ultras_count * price_for_ticket + transport_price

if budget > total_cost:
    print(f"Yes! You have {budget - total_cost:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_cost - budget:.2f} leva.")




