from sys import maxsize

max_number = -maxsize

while True:
    current_number = input()

    if current_number == "Stop":
        break

    current_number = int(current_number)

    if current_number > max_number:
        max_number = current_number

print(max_number)
