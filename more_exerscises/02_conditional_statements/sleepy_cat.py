rest_days = int(input())

NORM_FOR_PLAY = 30000
WORKING_DAY_PLAY = 63
REST_DAY_PLAY = 127

work_days = 365 - rest_days

total_play_minutes = (rest_days * REST_DAY_PLAY) + (work_days * WORKING_DAY_PLAY)

if total_play_minutes > NORM_FOR_PLAY:
    print("Tom will run away")
    print(f"{(total_play_minutes - NORM_FOR_PLAY) // 60} hours and {(total_play_minutes - NORM_FOR_PLAY) % 60} minutes more for play")

else:
    print("Tom sleeps well")
    print(f"{(NORM_FOR_PLAY - total_play_minutes) // 60} hours and {(NORM_FOR_PLAY - total_play_minutes) % 60} minutes less for play")




