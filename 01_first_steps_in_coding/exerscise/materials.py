PACK_OF_PENS = 5.80
MARKERS_PACK = 7.20
DETERGENT_LITER = 1.20

packs_od_pens_quantity = int(input())
marker_packs_quantity = int(input())
detergent_liters = int(input())
percent_discount = int(input()) / 100

total_price_without_discount = packs_od_pens_quantity * PACK_OF_PENS \
    + marker_packs_quantity * MARKERS_PACK \
    + detergent_liters * DETERGENT_LITER \

total_price_with_discount = total_price_without_discount - percent_discount * total_price_without_discount

print(total_price_with_discount)





