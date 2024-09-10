meters = 5364
day = 1

while meters < 8848:
    command = input()
    if command == "END":
        break
    elif command == "Yes":
        day += 1

    if day > 5:
        break

    current_meters_climbed = int(input())
    meters += current_meters_climbed

if meters >= 8848:
    print(f"Goal reached for {day} days!")
else:
    print("Failed!")
    print(f"{meters}")
