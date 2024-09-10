fuel_type = input()
fuel_in_tank = float(input())

if fuel_type == "Diesel":
    if fuel_in_tank < 25:
        print("Fill your tank with diesel!")
    else:
        print("You have enough diesel.")

elif fuel_type == "Gasoline":
    if fuel_in_tank < 25:
        print("Fill your tank with gasoline!")
    else:
        print("You have enough gasoline.")

elif fuel_type == "Gas":
    if fuel_in_tank < 25:
        print("Fill your tank with gas!")
    else:
        print("You have enough gas.")

else:
    print("Invalid fuel!")

