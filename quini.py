import random


def quini6():
	lista = []
	numero=""
	for i in range(6):
		numero = str(random.randint(0,45))
		lista.append(numero)
	return (lista)

print(quini6())
