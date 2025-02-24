pontos = 0

print("Telefonou para vítima?")
pergunta1 = int(input("1.Sim\n2.Não  \n" ))
if pergunta1 == 1:
    pontos += 1

print("Esteve no local do Crime?")
pergunta2 = int(input("1.Sim\n2.Não  \n" ))
if pergunta2 == 1:
    pontos += 1

print("Mora perto da vítima?")
pergunta3 = int(input("1.Sim\n2.Não  \n" ))
if pergunta3 == 1:
    pontos += 1

print("Devia para vítima?")
pergunta4 = int(input("1.Sim\n2.Não  \n" ))
if pergunta4 == 1:
    pontos += 1

print("Já trabalhou com a vítima?")
pergunta5 = int(input("1.Sim\n2.Não  \n" ))
if pergunta5 == 1:
    pontos += 1


if pontos == 2:
    print("Suspeito")
elif pontos == 3 or pontos == 4:
    print("Cúmplice")
elif pontos == 5:
    print("Assassino")
else: 
    print("Inocente")