total_days = int(input())

doctors = 7
treated_patients = 0
untreated_patients = 0

for day in range(1, total_days + 1):
    patients_for_day = int(input())

    if day % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1

    if doctors >= patients_for_day:
        treated_patients += patients_for_day
    elif doctors < patients_for_day:
        treated_patients += doctors
        untreated_patients += patients_for_day - doctors

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
