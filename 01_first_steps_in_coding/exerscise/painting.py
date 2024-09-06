NYLON_SQUARE_METER = 1.50
PAINT_LITER = 14.50
THINNER_LITER = 5
BAGS = 0.40

nylon_price = (int(input()) + 2) * NYLON_SQUARE_METER
paint_price = (int(input()) + 10 / 100) * PAINT_LITER
thinner_price = int(input()) * THINNER_LITER

price_for_all_materials = nylon_price + paint_price + thinner_price + BAGS

hours_of_work = int(input())

money_for_workers = 30 / 100 * price_for_all_materials

total_price = price_for_all_materials + money_for_workers


