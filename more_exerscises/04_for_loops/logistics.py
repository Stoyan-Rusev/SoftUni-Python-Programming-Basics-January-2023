cargo_count = int(input())

bus_tons = 0
truck_tons = 0
train_tons = 0

for number in range(1, cargo_count + 1):
    weight = int(input())

    if weight <= 3:
        bus_tons += weight
    elif weight <= 11:
        truck_tons += weight
    elif weight >= 12:
        train_tons += weight

total_tons = bus_tons + truck_tons + train_tons

bus_price = bus_tons * 200
truck_price = truck_tons * 175
train_price = train_tons * 120

total_price = bus_price + truck_price + train_price

print(f"{total_price / total_tons:.2f}")
print(f"{bus_tons / total_tons * 100:.2f}%")
print(f"{truck_tons / total_tons * 100:.2f}%")
print(f"{train_tons / total_tons * 100:.2f}%")
