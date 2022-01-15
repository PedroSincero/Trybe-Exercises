# Calma! Apesar do termo potencialmente assustador, a complexidade logarítmica não exige cálculos matemáticos complicados para ser entendida. Dado pela notação O(log n) , um algoritmo logarítmico geralmente reduz pela metade o tamanho do input a cada iteração.
# O tempo de execução de um algoritmo é dito logarítmico porque log₂n (lê-se: "log de n na base 2") nos dá o número de iterações que uma entrada de tamanho n terá no algoritmo.
# No exemplo a seguir temos um algoritmo de busca binária. Dado um array de tamanho n ordenado em ordem crescente, encontre um número passado na entrada . É como procurar por um nome numa lista telefônica!

# Como você faz? Suponha que você quer procurar pelo nome Tintim .
# Voce irá escolher uma página do livro para abrir;
# Percebe que caiu no bloco de letra M ;
# Como M < T na ordem alfabética, então voce deve avançar alguns blocos;
# Escolhe uma página que está adiante;
# Percebe que caiu no bloco de letra V ;
# Como V > T , então voce deve voltar alguns blocos;
# Repita esse processo até encontrar o nome desejado.

# Se quiser rodar seus próprios testes, o algoritmo de busca binária é o abaixo:

# A estrutura deve estar ordenada para que a busca binária funcione
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binary_search_iterative(array, element):
    mid = 0
    start = 0
    end = len(array)
    step = 0

    while (start <= end):
        print("Subarray in step {}: {}".format(step, str(array[start: end + 1])))
        step = step + 1
        mid = (start + end) // 2

        if element == array[mid]:
            return mid

        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return - 1


print(binary_search_iterative(data, 2))

# Observe como, a cada iteração, o algoritmo de busca binária corta o problema pela metade: primeiro ele corta a lista em dois e pega o elemento do meio. Depois ele vai para o lado onde o elemento que procura está e corta este lado novamente pela metade. Quando cortamos a entrada pela metade, a cada iteração, temos um padrão que segue a função matemática de logaritmo na base dois! Assim, nosso algoritmo é O(log n) .
# Um logaritmo em base 2 representa o número de vezes que um valor deve ser dividido pela metade para obter 1.
# Dessa forma, sem precisarmos nos aprofundar na matemática, conseguimos calcular a ordem de complexidade de um algoritmo deste tipo! Quando a entrada é cortada pela metade a cada iteração temos um comportamento logarítmico!

# Para fixar um pouco, vamos fazer um exercício:
# Exercícios de Fixação
# Exercício 4: Imagine que você recebe dois arrays de tamanho igual, array1 e array2 . Para cada elemento do array1 , realize uma busca binária no array2 . Mostre que a ordem de complexidade do algoritmo resultante é O(n * log n) , ou O(n log n) .
# 💡 Não precisa implementar o código aqui!
