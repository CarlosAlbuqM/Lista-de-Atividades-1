perguntaTurno = str(input(("Qual turno você estuda, digite M para matutino, V para vespertino ou N para noturno: ")))


if perguntaTurno == 'M':
    print ("Bom dia")
elif perguntaTurno == "V":
    print("Boa tarde")
elif perguntaTurno == 'N':
    print("Boa noite")
else:   
    print("Valor inválido ")