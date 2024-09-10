bottles_count = int(input())

i = 1
soap_ml = bottles_count * 750
dishes = 0
pots = 0

while soap_ml >= 0:
    items = input()

    if items == "End":
        print("Detergent was enough!")
        print(f"{dishes} dishes and {pots} pots were washed.")
        print(f"Leftover detergent {soap_ml} ml.")
        break

    items = int(items)

    if i % 3 == 0:
        soap_ml = soap_ml - items * 15
        pots += items
    else:
        soap_ml = soap_ml - items * 5
        dishes += items

    i += 1

else:
    print(f"Not enough detergent, {abs(soap_ml)} ml. more necessary!")
