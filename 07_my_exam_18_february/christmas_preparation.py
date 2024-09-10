present_paper_amount = int(input())
cloth_paper_amount = int(input())
glue_liters = float(input())
discount_percent = int(input()) / 100

PAPER_PRISE = 5.80
CLOTH_PRISE = 7.20
GLUE_PRISE = 1.20

total_prise = present_paper_amount * PAPER_PRISE + cloth_paper_amount * CLOTH_PRISE + glue_liters * GLUE_PRISE
final_prise = total_prise - (total_prise * discount_percent)

print(f"{final_prise:.3f}")
