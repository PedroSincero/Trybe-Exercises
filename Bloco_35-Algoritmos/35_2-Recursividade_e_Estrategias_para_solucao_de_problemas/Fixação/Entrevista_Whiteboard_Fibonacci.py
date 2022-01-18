# Imagine que você vai fazer uma entrevista para uma empresa onde você sempre sonhou em trabalhar. Você vai fazer uma whiteboard interview, onde você tem um tempo limitado para resolver um problema de programação; Quem sabe faz ao vivo! Veja o problema:
# A sequência de fibonacci é uma sequência numérica em que, partindo dos dois primeiros números sendo 0 e 1, o próximo número será sempre a soma dos dois anteriores. Esta sequência é interessante pois aparece muito na matemática e na natureza de formas inusitadas. Veja os primeiros números:

# começo = [0, 1]
#  + 1 = 1 -> [0, 1, 1]
#  + 1 = 2 -> [0, 1, 1, 2]
#  + 2 = 3 -> [0, 1, 1, 2, 3]
#  + 2 = 5 -> [0, 1, 1, 2, 3, 5]

# e assim por diante: 8, 13, 21, 33, 54...
# Faça uma função que retorne o enésimo número da sequência de Fibonacci.
# Exercício de fixação

# Exercício 1: Fibonacci: Ligue o cronômetro, e faça a medição de quanto tempo você leva para resolver este problema. Se demorar mais de 10 minutos, pare! Seu tempo acabou.

def fibonacci_iter(n):
    sequence = [0, 1]
    if n >= 2:
        for x in range(2, n+1):
            next = sequence[-1] + sequence[-2]
            sequence.append(next)
    return sequence[n]

def fibonacci2(n):

  if n < 2:
    return n
  
  return fibonacci2(n-1) + fibonacci2(n-2)

# print(fibonacci2(10))
print(fibonacci_iter(10))