rent = int(input())

statues = rent - 0.3 * rent
catering = statues - 0.15 * statues
sound = catering / 2

total_cost = rent + statues + catering + sound

print(f"{total_cost:.2f}")
