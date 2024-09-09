free_space = int(input()) * int(input()) * int(input())

while free_space > 0:
    boxes = input()

    if boxes == "Done":
        print(f"{free_space} Cubic meters left.")
        break

    free_space -= int(boxes)

else:
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
