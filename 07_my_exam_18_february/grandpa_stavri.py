days = int(input())

total_liters = 0
total_degrees = 0

for _ in range(days):
    current_liters = float(input())
    total_liters += current_liters

    current_rakia_degrees = float(input())
    total_degrees += (current_rakia_degrees * current_liters)

final_degrees = total_degrees / total_liters

print(f"Liter: {total_liters:.2f}")
print(f"Degrees: {final_degrees:.2f}")

if final_degrees < 38:
    print("Not good, you should baking!")
elif final_degrees < 42:
    print("Super!")
else:
    print("Dilution with distilled water!")
