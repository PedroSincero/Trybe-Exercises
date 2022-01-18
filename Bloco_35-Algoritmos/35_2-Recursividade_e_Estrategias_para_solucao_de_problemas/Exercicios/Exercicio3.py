# Exercício 3: Crie um algoritmo recursivo que encontre, em uma lista, o maior número inteiro.

listao = [2,1,3,4,5,6,17,8,9,10,11,12,13,14,15,16,7]

def lista_num(lista):
  if len(lista) == 1:
    return lista
  elif lista[0] > lista[1]:
    
    return lista_num(lista[1:])

lista = [1,2,3]


print(lista[2])