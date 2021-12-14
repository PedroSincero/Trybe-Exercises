# Exercício 2: Defina uma classe Estatistica que calcule média, mediana e moda de uma lista de números.
# 🐦 Dica: Utilize métodos de classe.
from collections import Counter

class Estatistica():
  # n entendi direito o @classmethod, ver plantao
  @classmethod
  def media(self, num):
    return sum(num) / len(num)
  @classmethod
  def mediana(cls, numbers):
      numbers.sort()
      index = len(numbers) // 2
      if len(numbers) % 2 == 0:
          return (numbers[index - 1] + numbers[index]) / 2

      return numbers[index]

  @classmethod
  def moda(cls, numbers):
    # n entendi esta variavel, ver plantao, junto com o counter
      number, _ = Counter(numbers).most_common()[0]
      return number