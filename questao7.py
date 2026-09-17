import os
os.system('cls')

nome_produto = input("Digite o nome do produto: ")
quantidade = int (input("Digite a quantidade adquirida: "))
preco_unitario = float(input("Digite o preço unitário: R$ "))

total = quantidade * preco_unitario
if quantidade <= 5:
    percentual_desconto = 2
elif quantidade <= 10:
    percentual_desconto = 3
else:
    percentual_desconto = 5

desconto =  total * (percentual_desconto / 100)
total_a_pagar = total - desconto

print("\n--- RESUMO DA COMPRA ---")
print(f"Produto: {nome_produto}")
print(f"Total sem desconto: R$ {total:.2f}")
print(f"Desconto ({percentual_desconto}%): R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total_a_pagar:.2f}")
