length_of_aquarium = int(input())
width_of_aquarium = int(input())
height_of_aquarium = int(input())

volume_of_aquarium = length_of_aquarium * width_of_aquarium * height_of_aquarium * 0.001
occupied_space = float(input()) / 100 * volume_of_aquarium

total_volume = volume_of_aquarium - occupied_space

print(total_volume)
