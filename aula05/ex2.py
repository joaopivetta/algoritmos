nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
nota3 = float(input("Digite a sua terceira nota: "))

media = (nota1 + nota2 + nota3)/3
nota_exame = 0

if media < 3:
    resultado = "Reprovado"
else:
    if media < 7:
        resultado = "Exame"
        nota_exame = 12 - media
    else:
        resultado = "Aprovado"

print(f"media {media:5.2f} - {resultado}")
if nota_exame != 0:
    print(f"Tem que tirar no mínimo {nota_exame:5.2f}")
