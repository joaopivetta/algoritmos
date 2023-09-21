xAposento = float(input("Entre com a primeira medida do aposento: "))
yAposento = float(input("Entre com a segunda medida do aposento: "))
litrosTinta = float(input("Entre com a quantidade em litros da lata de tinta: "))

medidaAposento = (( xAposento * 2.8) + (yAposento * 2.8) * 2) - (2.1 *0.8)

qtdLatas = medidaAposento / 3

print(f"A quantidade de latas necessárias é {round(qtdLatas):2.0f}")