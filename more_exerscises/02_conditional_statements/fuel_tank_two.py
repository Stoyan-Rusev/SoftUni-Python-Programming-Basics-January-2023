GASOLINE = 2.22
DIESEL = 2.33
GAS = 0.93

fuel_type = input()
fuel_liters = float(input())
discount_card = input()

final_price = 0

if discount_card == "Yes":
    GASOLINE -= 0.18
    DIESEL -= 0.12
    GAS -= 0.08

if fuel_type == "Gasoline":
    final_price = fuel_liters * GASOLINE

elif fuel_type == "Diesel":
    final_price = fuel_liters * DIESEL

elif fuel_type == "Gas":
    final_price = fuel_liters * GAS

if 20 <= fuel_liters <= 25:
    final_price *= 0.92

elif fuel_liters > 25:
    final_price *= 0.90

print(f"{final_price:.2f} lv.")






