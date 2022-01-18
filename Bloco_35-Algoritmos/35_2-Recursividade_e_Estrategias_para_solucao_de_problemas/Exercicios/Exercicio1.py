# Exercício 1: Crie um algoritmo não recursivo para contar quantos números pares existem em uma sequência numérica (1 a n).
# Potencia = 0
def algoritmo(n):
  result = []
  for index in range(n):
    if index%2 == 0:
      result.append(n)
  return len(result)
  

print(algoritmo(4))