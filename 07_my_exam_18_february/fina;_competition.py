dancers = int(input())
points = float(input())
season = input()
country = input()

money_from_competition = 0
expenses = 0

if country == "Bulgaria":
    money_from_competition = dancers * points

    if season == "summer":
        expenses = 0.05 * money_from_competition
    else:
        expenses = 0.08 * money_from_competition

else:
    money_from_competition = (dancers * points) + (0.5 * dancers * points)

    if season == "summer":
        expenses = 0.10 * money_from_competition
    else:
        expenses = 0.15 * money_from_competition

money_after_expenses = money_from_competition - expenses
money_for_charity = money_after_expenses * 0.75

money_per_person = (money_after_expenses - money_for_charity) / dancers

print(f"Charity - {money_for_charity:.2f}")
print(f"Money per dancer - {money_per_person:.2f}")
