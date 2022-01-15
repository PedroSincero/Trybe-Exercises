# Há um último conceito importante para aprendermos aqui antes de passarmos para a aula ao vivo e os exercícios! Vocês verão nos próximos dias e blocos do curso muitas vezes os termos "melhor caso", "pior caso" e "caso médio". Eles significam o seguinte: "A depender da minha entrada, o meu algoritmo pode executar em O(1) ou O(n) ". Por exemplo, pense na busca sequencial:

def linear_search(numbers, n):
    for index, number in enumerate(numbers):
        if(number == n): return index

    return -1

print(linear_search([1, 2, 3, 4, 5], 4))

# Dizemos que, para entradas muito grandes, esse algoritmo é O(n) . O que acontece, porém, caso tenhamos sorte e o número que procuramos seja o primeiro do array? Nesse caso, mesmo para uma entrada infinita, nossa complexidade será O(1) . Esse é o melhor caso desse algoritmo. De forma análoga, o pior caso é o número ser o último elemento do array, ou seja O(n) .
# E o caso médio? Bem, seria algo como O(n * 1/2) , por exemplo (ou seja, o número que procuramos está no meio da lista). Mas, para entradas muito grandes, aprendemos a desprezar os números menos relevantes da soma, então podemos simplificar e dizer que o caso médio é O(n) também.
# Diferentes algoritmos tem diferentes cenários de melhor caso, pior caso e caso médio! Você verá vários exemplo ao longo dos próximos blocos!