salario = float(input("Digite seu salário atual: \n"))
percentual = float(input("Digite o percentual: \n"))
multiPercentual = percentual / 100
print(f"Seu novo salário com o aumento é: R$ {(salario + (salario * multiPercentual)):8.2f}")
