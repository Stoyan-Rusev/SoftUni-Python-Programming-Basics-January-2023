skumriq_price_kg = float(input())
caca_price_kg = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

PALAMUD_PRICE = skumriq_price_kg + skumriq_price_kg * 0.6
SAFRID_PRICE = caca_price_kg + caca_price_kg * 0.8
MIDI_PRICE = 7.50

total = palamud_kg * PALAMUD_PRICE + safrid_kg * SAFRID_PRICE + midi_kg * MIDI_PRICE

print(f"{total:.2f}")

