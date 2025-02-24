nota1 = float(input("Digite a nota da primeira unidade: "))
nota2 = float(input("Digite a nota da segunda unidade: "))

media = (nota1 + nota2) / 2


if media >= 7 and media < 10:
    print("Aprovado.")
elif media < 7:
    print("Reprovado.")
elif media == 10:
    print ("Aprovado com Distinção.")