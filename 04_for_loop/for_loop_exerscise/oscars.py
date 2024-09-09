actor_name = input()
starting_points = float(input())
number_of_judges = int(input())

actor_points = starting_points

for _ in range(number_of_judges):
    name_of_judge = input()
    points_from_judge = float(input())
    actor_points += len(name_of_judge) * points_from_judge / 2
    if actor_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {actor_points:.1f}!")
        break

else:
    print(f"Sorry, {actor_name} you need {1250.5 - actor_points:.1f} more!")
