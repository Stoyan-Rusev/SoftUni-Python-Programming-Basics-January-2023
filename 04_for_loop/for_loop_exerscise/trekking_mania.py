ngroups_count = int(input())

musala = 0
monblan = 0
kilimanaro = 0
k2 = 0
everest = 0

for _ in range(groups_count):
    people_in_group = int(input())

    if people_in_group <= 5:
        musala += people_in_group

    elif people_in_group <= 12:
        monblan += people_in_group

    elif people_in_group <= 25:
        kilimanaro += people_in_group

    elif people_in_group <= 40:
        k2 += people_in_group

    elif people_in_group > 40:
        everest += people_in_group

total_amount_of_people = musala + monblan + kilimanaro + k2 + everest

print(f"{musala / total_amount_of_people * 100:.2f}%")
print(f"{monblan / total_amount_of_people * 100:.2f}%")
print(f"{kilimanaro / total_amount_of_people * 100:.2f}%")
print(f"{k2 / total_amount_of_people * 100:.2f}%")
print(f"{everest / total_amount_of_people * 100:.2f}%")

