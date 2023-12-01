def eh_primo(numero):

    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def contar_primos(n):

    count = 0
    for i in range(n + 1):
        if eh_primo(i):
            count += 1
    return count


Y = 21


limite = Y * 2 + 5


num_primos = [i for i in range(limite + 1) if eh_primo(i)]


soma_primos = sum(num_primos)


print("Lista de números primos até", limite, ":", num_primos)
print("Soma dos números primos:", soma_primos)