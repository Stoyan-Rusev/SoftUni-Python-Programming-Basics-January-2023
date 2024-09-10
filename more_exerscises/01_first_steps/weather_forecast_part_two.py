degrees = float(input())
weather = None

if 26.00 <= degrees <= 35.00:
    weather = "Hot"
elif 20.1 <= degrees <= 25.9:
    weather = "Warm"
elif 15.00 <= degrees <= 20.00:
    weather = "Mild"
elif 12.00 <= degrees <= 14.90:
    weather = "Cool"
elif 5.00 <= degrees <= 11.9:
    weather = "Cold"
else:
    weather = "unknown"

print(weather)



