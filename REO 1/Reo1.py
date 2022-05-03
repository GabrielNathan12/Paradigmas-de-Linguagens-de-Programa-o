def pearson(X, Y):
	mediaX    = float(sum(X)) / len(X)
	mediaY    = float(sum(Y)) / len(Y)
	paraCima   = 0
	paraBaixoX = 0
	paraBaixoY = 0

	for valorX, valorY in zip(X, Y):
		paraCima = paraCima + ((valorX - mediaX) * (valorY - mediaY))
		paraBaixoX = paraBaixoX + ((valorX - mediaX) ** 2.0)
		paraBaixoY = paraBaixoY + ((valorY - mediaY) ** 2.0)

	total = paraCima / ((paraBaixoX * paraBaixoY) ** (1.0/2.0))

	return total


def main():
	import sys
	nome_arq = sys.argv[1:]
	arq = open(str(nome_arq[0]), 'r', encoding='utf8')
	l = arq.readlines()
	i = len(l)
	arq.close()
	

	if(i > 0):
		l = [valor.rstrip() for valor in l]
		l = [_str.split(',') for _str in l]

		X = []
		Y = []

		tamanho = 0
		palavra = False

		while(tamanho < 8 and palavra == False):
			try:
				l = list(map(float, l[tamanho]))
				X.append(l[0])
				Y.append(l[1])
			except:
				palavra = True

			tamanho += 1

		if(palavra == False):
			total = pearson(X, Y)

			print('%.18f' % total)
		else:
			print("Palavras no arquivo")

	else:
		print("Arquivo Vazio")

