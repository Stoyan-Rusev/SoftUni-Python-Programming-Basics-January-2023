bitcoins_amount = int(input())
chinese_money = float(input())
commission_percent = float(input()) / 100

leva_from_bitcoins = bitcoins_amount * 1168
dollars_from_chinese = chinese_money * 0.15
leva_from_dollars = dollars_from_chinese * 1.76

total_lv = leva_from_dollars + leva_from_bitcoins
tota_euro = total_lv / 1.95

money_left = tota_euro - tota_euro * commission_percent

print(f"{money_left:.2f}")
