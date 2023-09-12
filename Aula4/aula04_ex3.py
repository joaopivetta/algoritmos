from math import sqrt, pow

x1 = int(input("entre com o valor de x1: "))
y1 = int(input("entre com o valor de y1: "))
x2 = int(input("Entre com o valor de x2: "))
y2 = int(input("Entre com o valor de y2: "))
dx = x2 - x1
dy = y2 - y1
dist = sqrt(pow(dx, 2) + pow(dy, 2))
print("a distância entre os pontos é: ", dist)
