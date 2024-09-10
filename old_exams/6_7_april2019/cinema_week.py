movie_name = input()
type = input()
tickets_count = int(input())

tickets_price = 0

if type == "normal":
    if movie_name == "A Star Is Born":
        tickets_price = 7.50
    elif movie_name == "Bohemian Rhapsody":
        tickets_price = 7.35
    elif movie_name == "Green Book":
        tickets_price = 8.15
    elif movie_name == "The Favourite":
        tickets_price = 8.75

elif type == "luxury":
    if movie_name == "A Star Is Born":
        tickets_price = 10.50
    elif movie_name == "Bohemian Rhapsody":
        tickets_price = 9.45
    elif movie_name == "Green Book":
        tickets_price = 10.25
    elif movie_name == "The Favourite":
        tickets_price = 11.55

else:
    if movie_name == "A Star Is Born":
        tickets_price = 13.50
    elif movie_name == "Bohemian Rhapsody":
        tickets_price = 12.75
    elif movie_name == "Green Book":
        tickets_price = 13.25
    elif movie_name == "The Favourite":
        tickets_price = 13.95

total_price = tickets_count * tickets_price

print(f"{movie_name} -> {total_price:.2f} lv.")
