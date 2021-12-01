# Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.
def list(numbers):
  total = 0
  for number in numbers:
    total += number
  return total / len(numbers)