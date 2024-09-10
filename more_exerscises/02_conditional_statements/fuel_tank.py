fuel_type = input()
fuel_in_tank = float(input())

ENOUGH_FUEL = 25

if fuel_in_tank < ENOUGH_FUEL:
    if fuel_type == "Diesel":
        print("Fill your tank with diesel!")
    elif fuel_type == "Gasoline":
        print("Fill your tank with gasoline!")
    elif fuel_type == "Gas":
        print("Fill your tank with gas!")

elif fuel_type != "Diesel" and fuel_type != "Gasoline" and fuel_type != "Gas":
    print("Invalid fuel!")

elif fuel_in_tank >= ENOUGH_FUEL:
    if fuel_type == "Gasoline":
        print("You have enough gasoline.")
    if fuel_type == "Gas":
        print("You have enough gas.")
    if fuel_type == "Diesel":
        print("You have enough diesel.")



