valor1 = int(input("Digite um número: "))
valor2 = int(input("Digite outro número: "))

if valor1 > valor2:
    print("O", valor1, "é maior que o" , valor2)
elif valor1 < valor2:
    print ("O", valor2, "é maior que o", valor1)
else:
    print("Os números são iguais")