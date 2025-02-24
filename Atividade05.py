valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

if valor1 > valor2 and valor1 > valor3:
    print("O número", valor1 ," tem o maior valor.")
elif valor2 > valor1 and valor2 > valor3:
    print("O número", valor2 ,"tem o maior valor.")
elif valor3 > valor1 and valor3 > valor2:
    print("O número", valor3 ,"tem o maior valor.")
else:
    print("Os número são iguais.")