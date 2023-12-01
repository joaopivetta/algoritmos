numero =int(input("Entre com um número: "))
exp = int(input("Entre com o valor do expoente final: "))

for i in range(1,exp + 1):
    numero = numero + (2 ** i)

    print(f"a soma dos numeros é: {numero:5.2f} ")