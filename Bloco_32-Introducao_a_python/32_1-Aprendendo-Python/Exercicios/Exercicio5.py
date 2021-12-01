# Exercício 5: Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Crie uma função que retorne dois valores em uma tupla contendo a quantidade de latas de tinta a serem compradas e o preço total a partir do tamanho de uma parede(em m²).

def pintura(area):
  preco = 80
  litro = area / 3
  latas = litro // 18
# se o modulo de litro por 18 retornar 0
  if litro % 18:
    # some 1 nas latas
    latas += 1
  # retorno a tupula com a quantidade de latas e o valor da compra
  return latas, latas * preco