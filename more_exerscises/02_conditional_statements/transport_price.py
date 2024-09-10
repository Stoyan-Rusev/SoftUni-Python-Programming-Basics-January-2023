distance_km = int(input())
time_of_the_day = input()

taxi_price = 0
bus_price = 0.09 * distance_km
train_price = 0.06 * distance_km

if time_of_the_day == "day":
    taxi_price = (0.79 * distance_km) + 0.70

if time_of_the_day == "night":
    taxi_price = (0.90 * distance_km) + 0.70

if distance_km < 20:
    print(f"{taxi_price:.2f}")

if 20 <= distance_km < 100:
    print(f"{bus_price:.2f}")

if distance_km >= 100:
    print(f"{train_price:.2f}")




