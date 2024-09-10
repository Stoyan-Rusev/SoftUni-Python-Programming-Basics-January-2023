total_floors = int(input())
rooms_per_floor = int(input())

room_name = ""

for floor in range(total_floors, 0, -1):
    for rooms in range(0, rooms_per_floor):
        if floor == total_floors:
            room_name = f"L{floor}{rooms}"
        elif floor % 2 == 0:
            room_name = f"O{floor}{rooms}"
        elif floor % 2 != 0:
            room_name = f"A{floor}{rooms}"

        print(room_name, end=" ")
    print()
