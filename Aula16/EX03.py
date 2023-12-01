def soma_multiplicacao(numero_str):
    soma = 0
    multi = 1
    for digito_str in numero_str:
        digito = int(digito_str)
        soma += digito
        multi *= digito
    return soma, multi
ra = input("Digite Seu ra completo: ")
try:
    soma, multi = soma_multiplicacao(ra)
    print(f"Soma = {soma} e Multiplicação = {multi}")
except ValueError:
    print("Por favor, digite um número válido no formato string.")