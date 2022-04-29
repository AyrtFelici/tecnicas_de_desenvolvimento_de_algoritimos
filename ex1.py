#entrada
custof=float (input("digite o custo de fabrica R$"))
valord=float((custof*28)/100)
valori=float((custof*45)/100)
preco=float(custof+valord+valori)
print(f"o custo de fabrica{custof}")
print(f"o valor do distrito é:{valord}")
print(f"valor do imposto{valori}")
print(f"preço final é:{preco:.2f}")