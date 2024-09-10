from math import ceil
from math import floor

days = int(input())
food_she_left = int(input())

dog_food_kg = float(input())
cat_food_kg = float(input())
turtle_food_kg = float(input()) / 1000

food_needed_for_all_days = (dog_food_kg + cat_food_kg + turtle_food_kg) * days

if food_she_left >= food_needed_for_all_days:
    print(f"{floor(food_she_left - food_needed_for_all_days)} kilos of food left.")

else:
    print(f"{ceil(food_needed_for_all_days - food_she_left)} more kilos of food are needed.")


