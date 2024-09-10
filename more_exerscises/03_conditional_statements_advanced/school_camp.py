season = input()
group_type = input()
students_count = int(input())
nights = int(input())

sport_type = None
price_for_person = 0

if group_type == "boys":
    if season == "Winter":
        price_for_person = 9.60
        sport_type = "Judo"
    elif season == "Spring":
        price_for_person = 7.20
        sport_type = "Tennis"
    elif season == "Summer":
        price_for_person = 15
        sport_type = "Football"

elif group_type == "girls":
    if season == "Winter":
        price_for_person = 9.60
        sport_type = "Gymnastics"
    elif season == "Spring":
        price_for_person = 7.20
        sport_type = "Athletics"
    elif season == "Summer":
        price_for_person = 15
        sport_type = "Volleyball"

elif group_type == "mixed":
    if season == "Winter":
        price_for_person = 10
        sport_type = "Ski"
    elif season == "Spring":
        price_for_person = 9.50
        sport_type = "Cycling"
    elif season == "Summer":
        price_for_person = 20
        sport_type = "Swimming"


final_price = price_for_person * nights * students_count


if students_count >= 50:
    final_price *= 0.50
elif students_count >= 20:
    final_price *= 0.85
elif students_count >= 10:
    final_price *= 0.95

print(f"{sport_type} {final_price:.2f} lv.")










