lista = []

for i in range(0, 5):
    lista.append(int(input(f"Digite o número {i+1}: ")))

    maior = max(lista)
    pos = lista.index(max(lista))

print(f"O maior é: {maior}, e a sua posição é: {pos}")