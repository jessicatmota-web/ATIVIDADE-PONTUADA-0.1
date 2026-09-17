import os
os.system('cls')

morango = float(input("Quantos kg de morango: "))
maca = float(input("Quantos kg de maçã: "))

if morango <= 5:
    preco_morango = morango * 2.50
else:
    preco_morango = morango * 2.20

if maca <+ 5:
    preco_maca = maca * 1.80
else:
    preco_maca = maca * 1.50

total = preco_morango = preco_maca
total_kg = morango = maca

if total_kg >= 10 or total > 15:
    total = total * 0.90

print(f"Valor total a pagar: R$ {total:.2f}")
