from math import floor

tournaments_count = int(input())
starting_points = int(input())

earned_points = 0
wins = 0

for _ in range(tournaments_count):

    stage_tournament = input()

    if stage_tournament == "W":
        earned_points += 2000
        wins += 1
    elif stage_tournament == "F":
        earned_points += 1200
    elif stage_tournament == "SF":
        earned_points += 720

total_points = starting_points + earned_points
points_average = earned_points / tournaments_count
percent_wins = wins / tournaments_count * 100

print(f"Final points: {total_points}")
print(f"Average points: {floor(points_average)}")
print(f"{percent_wins:.2f}%")
