t_shirt_price = float(input())
goal_price = float(input())

shorts_price = 0.75 * t_shirt_price
socks_price = 0.20 * shorts_price
buttons_price = 2 * (t_shirt_price + shorts_price)

clothes_price = t_shirt_price + shorts_price + socks_price + buttons_price
final_price = 0.85 * clothes_price

if final_price >= goal_price:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {final_price:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {goal_price - final_price:.2f} lv. more.")
