airline = input()
adult_tickets_count = int(input())
children_tickets_count = int(input())
net_price_adult = float(input())
tax = float(input())

adult_ticket_price = net_price_adult + tax
children_ticket_price = 0.3 * net_price_adult + tax
money_made = 0.2 * (adult_ticket_price * adult_tickets_count + children_ticket_price * children_tickets_count)

print(f"The profit of your agency from {airline} tickets is {money_made:.2f} lv.")
