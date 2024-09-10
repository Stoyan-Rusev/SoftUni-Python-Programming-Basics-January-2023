player = input()
goals = int(input())

record_name = player
record_goals = goals

while goals < 10:

    if goals > record_goals:
        record_goals = goals
        record_name = player

    if player == "END":
        print(f"{record_name} is the best player!")

        if record_goals < 3:
            print(f"He has scored {record_goals} goals.")
            break
        else:
            print(f"He has scored {record_goals} goals and made a hat-trick !!!")
            break

    player = input()

    if player != "END":
        goals = int(input())

else:
    record_name = player
    record_goals = goals
    print(f"{record_name} is the best player!")
    print(f"He has scored {record_goals} goals and made a hat-trick !!!")
