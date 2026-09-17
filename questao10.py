import os
os.system('cls')

# Leitura dos dados de entrada
tipo_combustivel = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").strip().upper()
litros = float(input("Digite a quantidade de litros vendidos: "))

# Preços base por litro
PRECO_ALCOOL = 3.79
PRECO_GASOLINA = 6.59

valor_total = 0.0

if tipo_combustivel == 'A':
    if litros <= 25:
        desconto = 0.10  # 10%
    else:
        desconto = 0.20  # 20%
    
    preco_com_desconto = PRECO_ALCOOL * (1 - desconto)
    valor_total = litros * preco_com_desconto

elif tipo_combustivel == 'G':
    if litros <= 25:
        desconto = 0.15  # 15%
    else:
        desconto = 0.30  # 30%
    
    preco_com_desconto = PRECO_GASOLINA * (1 - desconto)
    valor_total = litros * preco_com_desconto

else:
    print("Tipo de combustível inválido!")

if valor_total > 0:
    print(f"Valor a ser pago pelo cliente: R$ {valor_total:.2f}")