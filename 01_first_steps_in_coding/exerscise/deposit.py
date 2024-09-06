deposit = float(input())
time_for_deposit = int(input())
year_interest_percent = float(input()) / 100

total_sum = deposit + (year_interest_percent * deposit / 12) * time_for_deposit

print(total_sum)
