# Os arrays tem sempre o mesmo tamanho
def multiply_arrays(array1, array2):
    result = []
    for number1 in array1:
        for number2 in array2:
            result.append(number1 + number2)

    return result

# Seus tempos de execução para um par de arrays de 2000 e 4000 elementos são:

# def multiply_array(numbers):
  # ...

sum_array(array_com_dois_mil_numeros)
# O tempo de execução deste algoritmo foi 0.45s

sum_array(array_com_quatro_mil_numeros)
# Já esse teve tempo de execução de 1.8s, cerca de quatro vezes maior.

# Porque, dessa vez, quando dobramos o tamanho da entrada (de 2000 para 4000) nós quadruplicamos o tempo de execução? Ora, vejamos! Temos dois arrays do mesmo tamanho, que vamos chamar de n . Repare que temos dois loops aninhados um dentro do outro. Isso significa que, para cada número de array1 , todo o array2 será percorrido! Rode o exemplo abaixo para conferir:

def multiply_arrays(array1, array2):
    result = []
    number_of_iterations = 0

    for number1 in array1:
        print(f'Array 1: {number1}')
        for number2 in array2:
            print(f'Array 2: {number2}')
            result.append(number1 * number2)
            number_of_iterations += 1

    print(f'{number_of_iterations} iterações!')
    return result


meu_array = [1,2,3,4,5]

multiply_arrays(meu_array, meu_array)

# Repare como, para dois arrays de tamanho 5, temos 25 iterações! Varie os números e veja como, sempre o número de iterações é n vezes n , ou seja, n² ! Por isso, lá em cima, multiplicar por dois o tamanho da entrada, de 2000 para 4000, multiplicou por quatro o tempo de execução: para um algoritmo O(n²) , aumentar a entrada em n vezes, aumenta o tempo de execução em n² vezes!
# Para fixar um pouco, vamos fazer uns exercícios:

# Exercícios de Fixação
# Exercício 2: Para desembaraçar a sopa de letrinhas que a seção anterior criou, meça o tempo de execução do algoritmo acima e, mudando o tamanho das entradas, veja como, se você aumenta a entrada em n vezes, o tempo de execução aumenta em n² vezes!
meu_array = list(range(1, 1000))
time python3 meu_programa.py
# Exercício 3: Faça um algoritmo qualquer com três loops aninhados um dentro do outro. Entenda como ele terá uma complexidade de O(n³) !
# Se tiver dificuldades, nos procure!
def multiply_arrays(array1, array2, array3):
    result = []
    number_of_iterations = 0

    for number1 in array1:
        for number2 in array2:
            for number3 in array3:
                result.append(number1 * number2 * number3)
                number_of_iterations += 1

    print(f'{number_of_iterations} iterações!')
    return result


# Usar 1000 aqui vai ser muito lento!
meu_array = list(range(1, 200))
multiply_arrays(meu_array, meu_array, meu_array)