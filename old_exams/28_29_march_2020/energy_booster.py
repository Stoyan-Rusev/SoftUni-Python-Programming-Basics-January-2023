flavour = input()
pack_type = input()
ordered_packs = int(input())

final_cost = 0

if flavour == "Watermelon":
    if pack_type == "small":
        final_cost = ordered_packs * 56
    elif pack_type == "big":
        final_cost = ordered_packs * 28.70


elif flavour == "Mango":
    if pack_type == "small":
        final_cost = ordered_packs * 36.66
    elif pack_type == "big":
        final_cost = ordered_packs * 19.60

elif flavour == "Pineapple":
    if pack_type == "small":
        final_cost = ordered_packs * 42.10
    elif pack_type == "big":
        final_cost = ordered_packs * 24.80

elif flavour == "Raspberry":
    if pack_type == "small":
        final_cost = ordered_packs * 20
    elif pack_type == "big":
        final_cost = ordered_packs * 15.20

print(f"{final_cost:.2f} lv.")
