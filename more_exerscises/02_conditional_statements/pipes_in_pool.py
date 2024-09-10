pool_volume = int(input())
pipe_one_debit = int(input())
pipe_two_debit = int(input())
hours = float(input())

pipe_one_water = pipe_one_debit * hours
pipe_two_water = pipe_two_debit * hours

total_water = pipe_one_water + pipe_two_water

water_in_percents = total_water / pool_volume * 100
pipe_one_percents = pipe_one_water / total_water * 100
pipe_two_percents = pipe_two_water / total_water * 100

if total_water <= pool_volume:
    print(f"The pool is {water_in_percents:.2f}% full. Pipe 1: {pipe_one_percents:.2f}%. Pipe 2: {pipe_two_percents:.2f}%.")
else:
    print(f"For {hours} hours the pool overflows with {total_water - pool_volume} liters.")

