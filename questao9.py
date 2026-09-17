import os
os.system('cls')

# Leitura dos dados de entrada
renda_mensal = float(input("Digite a renda mensal do solicitante (R$): "))
valor_emprestimo = float(input("Digite o valor total do empréstimo (R$): "))
num_prestacoes = int(input("Digite o número de prestações desejado: "))

# Cálculos
valor_prestacao = valor_emprestimo / num_prestacoes
limite_emprestimo = renda_mensal * 10
limite_prestacao = renda_mensal * 0.30

# Verificação das condições
if valor_emprestimo <= limite_emprestimo and valor_prestacao <= limite_prestacao:
    print("\nEmpréstimo CONCEDIDO.")
else:
    print("\nEmpréstimo NEGADO.")
    if valor_emprestimo > limite_emprestimo:
        print("- O valor total do empréstimo ultrapassa 10x a renda mensal.")
    if valor_prestacao > limite_prestacao:
        print("- O valor da prestação ultrapassa 30% da renda mensal.")