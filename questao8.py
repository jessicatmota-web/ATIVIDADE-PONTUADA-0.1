import os
os.system('cls')

cor = input("Digite a cor do CD (Verde, Azul, Amarelo ou Vermelho): ").strip().lower()

if cor == "verde":
    preco = 10.00
    print(f"CD Verde - Preço: R$ {preco:.2f}")
elif cor == "azul":
    preco = 20.00
    print(f"CD Azul - Preço: R$ {preco:.2f} ")
elif cor == "amarelo":
    preco = 30.00
    print(f"CD Amarelo - Preço: R$ {preco:>2f}")
elif cor == "vermelho":
    preco = 40.00
    print(f"CD Vermelho - Preço: R$ {preco:>2f}")
else:
    print("Cor inválida! Cores disponíveis: Verde, Azul, Amarelo, Vermelho.")
    