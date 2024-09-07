from math import ceil

movie_name = input()
episode_length = int(input())
lunch_brake_length = int(input())

time_for_eating = lunch_brake_length / 8
time_for_rest = lunch_brake_length / 4
time_taken = time_for_rest + time_for_eating + episode_length
free_time_left = lunch_brake_length - time_taken

if free_time_left >= 0:
    print(f"You have enough time to watch {movie_name} and left with {ceil(free_time_left)} minutes free time.")

else:
    print(f"You don't have enough time to watch {movie_name}, you need {ceil(abs(free_time_left))} more minutes.")
