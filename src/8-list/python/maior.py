'''
Maior elemento de uma lista

Escreva a função maior_elemento que recebe como parâmetro 
uma lista com números inteiros 
e devolve um número inteiro correspondente 
ao maior valor presente na lista recebida.
'''
minha_lista = [7,8,9,15,1,2]

def maior_elemento(lista):
	maior = lista[0]
	for x in range(1,len(lista)):
		if maior < lista[x] :
			maior = lista[x]
	return maior

print(maior_elemento(minha_lista))