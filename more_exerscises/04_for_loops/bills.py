months = int(input())

electricity_total = 0
water_total = 0
internet_total = 0
other_bills_total = 0

for i in range(1, months + 1):
    electricity_bill = float(input())

    electricity_total += electricity_bill
    water_total += 20
    internet_total += 15
    other_bills_total += (electricity_bill + 20 + 15) + (electricity_bill + 20 + 15) * 0.2

average_bills_for_month = (electricity_total + water_total + internet_total + other_bills_total) / months

print(f"Electricity: {electricity_total:.2f} lv")
print(f"Water: {water_total:.2f} lv")
print(f"Internet: {internet_total:.2f} lv")
print(f"Other: {other_bills_total:.2f} lv")
print(f"Average: {average_bills_for_month:.2f} lv")
