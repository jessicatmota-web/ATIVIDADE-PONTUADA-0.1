import os
os.system('cls')

operacao = input("Digite a operação (+, -, * ou /): ")
A = int(input("Digite o valor A: "))
B = int(input("Digite o valor B: "))

if operacao == "+":
    resultado = A + B
elif operacao == "_":
    resultado = A - B
elif operacao == "*":
    resultado = A * B
elif operacao == "/":
    if B != 0:
        resulado = A / B
    else:
        resultado = "Erro: não pode dividir por zero!"

else:
    resultado = "Operação ínvalida!"

print(f"Resultado: {A} {operacao} {B} = {resultado}")
