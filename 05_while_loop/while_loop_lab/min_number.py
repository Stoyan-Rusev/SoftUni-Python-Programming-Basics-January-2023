from sys import maxsize

command = input()
min_number = maxsize

while command != 'Stop':
    num = int(command)

    if num < min_number:
        min_number = num

    command = input()

print(min_number)
