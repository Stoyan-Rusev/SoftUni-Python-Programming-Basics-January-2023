x = float(input())
y = float(input())
h = float(input())

door = 1.2 * 2
window = 1.5 ** 2

front_rear_walls_area = 2 * (x ** 2) - door
side_walls_area = (x * y - window) * 2

walls_area = front_rear_walls_area + side_walls_area
green_paint = walls_area / 3.4

roof_area = (2 * x * y) + (2 * x * h / 2)
red_paint = roof_area / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
