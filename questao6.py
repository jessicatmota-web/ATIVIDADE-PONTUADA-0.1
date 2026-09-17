import os
os.system("cls")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print(f"\nMédia: {media:.1f}")

if media >= 6.0:
    print("Parabéns! Aluno APROVADO!")
elif media >= 4.1 and media <= 5.9:
    print("Aluno em RECUPERAÇÃO")
else:
    print("Aluno REPROVADO!")