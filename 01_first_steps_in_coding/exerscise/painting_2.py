nylon = int(input())
paint = int(input())
thinner = int(input())
hours_working = int(input())

NYLON_SQUARE_METER = 1.50
PAINT_LITER = 14.50
THINNER_LITER = 5
BAGS = 0.40

nylon = nylon + 2
paint = paint + paint * 10 / 100

material_price = nylon * NYLON_SQUARE_METER \
                 + paint * PAINT_LITER \
                 + thinner * THINNER_LITER\
                 + BAGS

work_price = hours_working * (30 / 100 * material_price)

total = material_price + work_price

print(total)
