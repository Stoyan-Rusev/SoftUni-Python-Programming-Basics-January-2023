GOAL = 10_000
steps_walked = 0

while steps_walked < GOAL:
    steps = input()

    if steps == "Going home":
        steps = int(input())
        steps_walked += steps

        if steps_walked < GOAL:
            print(f"{GOAL - steps_walked} more steps to reach goal.")
            break
        else:
            print("Goal reached! Good job!")
            print(f"{steps_walked - GOAL} steps over the goal!")
            break

    steps_walked += int(steps)

else:
    print("Goal reached! Good job!")
    print(f"{steps_walked - GOAL} steps over the goal!")
