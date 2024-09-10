voucher = int(input())

tickets_bought = 0
items_bought = 0

purchase_sum = 0

while True:
    purchase = input()
    if purchase == "End":
        break

    if len(purchase) > 8:
        purchase_sum = ord(purchase[0]) + ord((purchase[1]))
        voucher -= purchase_sum
        if voucher < 0:
            break
        tickets_bought += 1

    else:
        purchase_sum = ord(purchase[0])
        voucher -= purchase_sum
        if voucher < 0:
            break
        items_bought += 1

print(tickets_bought)
print(items_bought)
