month = input()
days_count = int(input())

apartment_price = 0
studio_price = 0

if month == "May" or month == "October":
    studio_price = days_count * 50
    apartment_price = days_count * 65
    if 7 < days_count <= 14:
        studio_price *= 0.95
    elif days_count > 14:
        studio_price *= 0.70

elif month == "June" or month == "September":
    studio_price = days_count * 75.20
    apartment_price = days_count * 68.70
    if days_count > 14:
        studio_price *= 0.80

elif month == "July" or month == "August":
    studio_price = days_count * 76
    apartment_price = days_count * 77


if days_count > 14:
    apartment_price *= 0.90


print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")






