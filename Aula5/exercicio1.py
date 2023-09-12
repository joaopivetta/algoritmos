nome = input("Digite seu nome Completo: ")
idade = int(input("Digite sua idade: "))

print(f"{nome} tem {idade} anos!")

if idade >= 60:
    print("Você ja pode pagar 1/2")
else:
    print("Parabéns você ainda é jovem")

print("Acabou o programa!")