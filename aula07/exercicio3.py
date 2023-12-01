s_peso = 0
s_altura = 0
for i in range(1, 4):
    peso = float(input(f'Entre com o {i}o peso: '))
    altura = float(input(f"Entre com a {i}a altura"))
    s_peso = s_peso + peso
    s_altura = s_altura + altura
    imc = peso / (altura * altura)
    if i == 1:
        maior_imc = imc
        menor_imc = imc
    if imc > maior_imc:
        maior_imc = imc
    if imc < menor_imc:
        menor_imc = imc
media_peso = s_peso / 3
media_altura = s_altura / 3

print(f"Peso médio é {media_peso:5.2f}")
print(f"Altura Média é {media_altura:5.2f}")
print(f"O menor imc é {menor_imc:5.2f}")
print(f"O maior imc é {maior_imc:5.2f}")



