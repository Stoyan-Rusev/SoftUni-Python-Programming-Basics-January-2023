juniors_count = int(input())
seniors_count = int(input())
track_type = input()

total_racers = juniors_count + seniors_count
juniors_tax = 0
seniors_tax = 0

if track_type == "trail":
    juniors_tax = 5.50
    seniors_tax = 7

elif track_type == "cross-country":
    juniors_tax = 8
    seniors_tax = 9.5
    if total_racers >= 50:
        juniors_tax *= 0.75
        seniors_tax *= 0.75

elif track_type == "downhill":
    juniors_tax = 12.25
    seniors_tax = 13.75

elif track_type == "road":
    juniors_tax = 20
    seniors_tax = 21.50

total_taxes = (juniors_tax * juniors_count + seniors_count * seniors_tax) * 0.95

print(f"{total_taxes:.2f}")


