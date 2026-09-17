import os
os.system('cls')

nome = input("Digite o nome: ")
sexo = input("Digite o sexo (F/M): ").upper()
estado_civil = input("Digite o estado civil: ").upper()

tempo_casada = 0
if sexo == "F" and estado_civil == "CASADA":
    tempo_casada = int(input("Digite o tempo de casada (em anos): "))

print("\n--- Dados ---")
print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")
if tempo_casada > 0:
    print(f"Tempo de casada: {tempo_casada} anos")