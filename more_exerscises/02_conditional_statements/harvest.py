from math import floor
from math import ceil

field_area = int(input())
grape_for_square_meter = float(input())
wine_liters_needed = int(input())
workers = int(input())

grape_total = field_area * grape_for_square_meter
grape_for_wine = 0.4 * grape_total
wine = grape_for_wine / 2.5
wine_extra = wine - wine_liters_needed

if wine < wine_liters_needed:
    print(f"It will be a tough winter! More {floor(wine_liters_needed - wine)} liters wine needed.")

else:
    print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
    print(f"{ceil(wine_extra)} liters left -> {ceil(wine_extra / workers)} liters per person.")






