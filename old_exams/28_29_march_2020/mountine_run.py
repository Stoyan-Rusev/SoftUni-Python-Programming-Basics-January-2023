record_seconds = float(input())
distance_meters = float(input())
seconds_per_meter = float(input())

seconds_slowed = distance_meters // 50 * 30
time_without_slowing = distance_meters * seconds_per_meter
final_time = time_without_slowing + seconds_slowed

if final_time < record_seconds:
    print(f" Yes! The new record is {final_time:.2f} seconds.")
else:
    print(f"No! He was {final_time - record_seconds:.2f} seconds slower.")
