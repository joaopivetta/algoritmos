valorRoupa = float(input("Digite o valor da compra: "))

if valorRoupa <= 1000:
    print(f"O valor com 10% de desconto é R${valorRoupa * 0.9:5.2f}")
else:
    if valorRoupa <= 5000:
        print(f"O valor com 20% de desconto é R${valorRoupa * 0.8:5.2f}")
    else:
        print(f"O valor com 30% de desconto é R${valorRoupa * 0.7:5.2f}")