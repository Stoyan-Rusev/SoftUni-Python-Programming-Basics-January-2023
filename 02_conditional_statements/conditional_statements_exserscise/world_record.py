from math import floor

world_record_seconds = float(input())
swimming_meters = float(input())
seconds_for_one_meter = float(input())

water_resistance_seconds_delay = floor(swimming_meters / 15) * 12.5

ivan_record_seconds = swimming_meters * seconds_for_one_meter + water_resistance_seconds_delay

if ivan_record_seconds < world_record_seconds:
    print(f" Yes, he succeeded! The new world record is {ivan_record_seconds:.2f} seconds.")

else:
    print(f"No, he failed! He was {ivan_record_seconds - world_record_seconds:.2f} seconds slower.")

