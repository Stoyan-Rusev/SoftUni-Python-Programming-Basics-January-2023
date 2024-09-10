while True:
    destination = input()

    if destination == "End":
        break

    min_budget = float(input())
    actual_budget = 0

    while min_budget > actual_budget:
        money_saved = float(input())
        actual_budget += money_saved
    else:
        print(f"Going to {destination}!")
