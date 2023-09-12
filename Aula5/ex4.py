dia = int(input(" entre com um numero do dia da semana: "))

match dia:
    case 1:
        nome = "domingo"
    case 2:
        nome = "Segunda-Feira"
    case 3:
        nome = "terça-feira"
    case 4:
        nome = "Quarta-feira"
    case 5:
        nome = "Quinta-feira"
    case 6:
        nome = "Sexta-feira"
    case 7:
        nome = "Sábado"
    case _:
        nome = f"O valor {dia} é inválido"



print(nome)
