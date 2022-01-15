def squared_array(numbers):
    array_of_squares = []
    for number in numbers:
            array_of_squares.append(number * number)

    return array_of_squares

# Para o algoritmo acima, aumentar a entrada em dez vezes aumenta em dez vezes o tempo de execução! A sua ordem de complexidade, portanto, é O(n) . Na maior parte das vezes em que falarmos de Ordem de Complexidade, estamos falando disso: do tempo que o algoritmo vai demorar para executar, ou complexidade de tempo . Há também uma outra complexidade: a complexidade de espaço , se referindo ao espaço em memória que o algoritmo ocupa.
# A ideia é a mesma: na medida em que a entrada aumenta, quanto o espaço em memória usado pelo algoritmo aumenta? No exemplo acima, o algoritmo povoa e retorna um array de tamanho n , sendo n o tamanho do array entrado, e o retorna. Assim sendo, sua complexidade de espaço é O(n) !

# 💡 Se falamos em Ordem de Complexidade sem especificar se é de tempo ou de memória, assuma que é de tempo!

# Mas e o outro exemplo, o do algoritmo sum_array() ?! Nesse caso, ele só precisa do espaço, em memória, de um número para executar. Para qualquer tamanho de entrada ele ocupa a mesma quantidade de espaço para executar. Assim sendo, sua complexidade de espaço é constante . Uma complexidade, seja de memória ou de tempo, ser constante, significa que o tamanho da entrada não influi no tempo de execução/memória ocupada de um algoritmo. A notação para esta complexidade é O(1)
# 💡 Quando calculamos a complexidade de espaço não levamos em consideração o espaço ocupado pela entrada! O tamanho da entrada não é algo que podemos, com nosso algoritmo, influenciar, então ele não entra em nossos cálculos.

# Exercícios de Fixação
# Exercício 1: Qual a Ordem de Complexidade (complexidade de tempo) do algoritmo abaixo? E a complexidade de espaço?

# Complexidade de Espaço: O(1)
# Complexidade de Tempo : O(n)
def multiply_array(numbers):
  # O, 1 result
    result = 0 
    # N
    for number in numbers:
            result *= number

    return result