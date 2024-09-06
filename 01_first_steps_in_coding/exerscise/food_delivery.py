CHICKEN_MENU_PRICE = 10.35
FISH_MENU = 12.40
VEG_MENU = 8.15
DELIVERY = 2.50

chicken_menu_total = int(input()) * CHICKEN_MENU_PRICE
fish_menu_total = int(input()) * FISH_MENU
veg_menu_total = int(input()) * VEG_MENU
dessert = 0.2 * (chicken_menu_total + fish_menu_total + veg_menu_total)

total_price = chicken_menu_total + \
              fish_menu_total + \
              veg_menu_total + \
              dessert + \
              DELIVERY

print(total_price)
