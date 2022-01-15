# Troco

# Valor final - Quantidade de moedas
# moedas
# resultado


# 16 4
# 25 10 5 1
# S

# [33, 33, 32, 31, 30, 25, 20, 14, 7, 1], 35
# True


def troco(lista, valor):
  index = 0
  result = valor
  while valor != 0 or index < len(lista):
    for  moeda in lista[index:]:
      print((lista[index:]))
      if moeda <= valor:
        valor -= moeda
      if valor == 0:
        return True
    valor = result
    index += 1
    break
  return False

# print(troco([25, 10, 5, 1], 16))
print(troco([33, 33, 32, 31, 30, 25, 20, 14, 7, 1], 35))

[25,17,12,5,4,2] 35