x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

spot = None

if x == x1 and y1 <= y <= y2:
    spot = "Border"
elif x == x2 and y1 <= y <= y2:
    spot = "Border"
elif y == y1 and x1 <= x <= x2:
    spot = "Border"
elif y == y2 and x1 <= x <= x2:
    spot = "Border"
else:
    spot = "Inside / Outside"

print(spot)

