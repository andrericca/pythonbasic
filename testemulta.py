minutos = int(input("Digite o numero de minutos: "))
if minutos < 200:
	preco = 0.60
elif minutos < 400:
	preco = 0.40
elif minutos < 800:
	preco = 0.20
else:
	preco = 0.08

print ("O valor da conta é: R$%5.2f" %(preco*minutos))