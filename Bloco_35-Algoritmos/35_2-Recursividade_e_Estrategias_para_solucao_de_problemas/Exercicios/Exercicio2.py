# Exercício 2: Transforme o algoritmo criado acima em recursivo.

def algoritmo(n):
  if n == 1:
    return 0
  elif n%2 == 0:
    return 1 + algoritmo(n -1)
  else: 
    return algoritmo(n -1)
  

print(algoritmo(4))