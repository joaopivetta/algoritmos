def qtd(cabeca , pe):
    y = 21
    cabeca = (y * 2) + 5
    pe = (y * 3) + 7

    resultado = cabeca / 2

    return resultado




x = int(input("Digite o número de cabeca: "))
y = int(input("Digite o número de pes: "))

total = qtd(x, y)

print(f"O total de patos é: {total} e o total de coelhos é {total}")

