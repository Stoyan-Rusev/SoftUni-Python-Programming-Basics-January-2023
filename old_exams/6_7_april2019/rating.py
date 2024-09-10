from sys import maxsize

movies_count = int(input())

highest_rating = -maxsize
lowest_rating = maxsize

movie_highest_rating = None
movie_lowest_rating = None

total_rating_sum = 0

for _ in range(movies_count):
    movie_name = input()
    rating = float(input())

    if rating > highest_rating:
        highest_rating = rating
        movie_highest_rating = movie_name

    if rating < lowest_rating:
        lowest_rating = rating
        movie_lowest_rating = movie_name

    total_rating_sum += rating

average_rating = total_rating_sum / movies_count

print(f"{movie_highest_rating} is with highest rating: {highest_rating:.1f}")
print(f"{movie_lowest_rating} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
