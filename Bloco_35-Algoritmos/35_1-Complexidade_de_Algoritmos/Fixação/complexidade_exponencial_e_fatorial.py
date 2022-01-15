# Essas complexidades caracterizam algoritmos que, para aumentos pequenos no tamanho da entrada, aumentam enormemente o seu tempo de execução. A relação do tempo de execução/espaço ocupado em cada caso é a seguinte:
# Exponencial: 2ⁿ ;
# Fatorial: n! .
# No caso exponencial, se n possui vinte elementos, o algoritmo faz um milhão de operações. Para o caso fatorial, os mesmos vinte elementos rendem 24 quatrilhões de operações (O número exato é: 2432902008176640000 operações 😨).
# Daí vem a pergunta: porque alguém iria escrever um algoritmo de complexidade fatorial?! A resposta é simples: quando não há outro algoritmo conhecido que resolve o problema. Quer conhecer um clássico? Eis o problema do caixeiro viajante ! Seu enunciado é: "Dada uma lista de cidades e a distância entre cada par de cidades, qual é a rota mais curta possível que visita todas as cidades exatamente uma vez e volta para a cidade de origem?"
# A única solução exata conhecida para este problema é a força bruta . Ou seja: você testa todas as possibilidades. Imagine que você tem três cidades: Belo Horizonte, São Paulo e Florianópolis. Temos as seguintes rotas possíveis, basta listá-las e escolher a mais curta:

# - Belo Horizonte > São Paulo > Florianópolis

# - Belo Horizonte > Florianópolis > São Paulo

# - Florianópolis > Belo Horizonte > São Paulo

# - Florianópolis > São Paulo > Belo Horizonte

# - São Paulo > Belo Horizonte > Florianópolis

# - São Paulo > Florianópolis > Belo Horizonte

# P = NP 

# O número de rotas para 3 cidades é 3! == 3 * 2 * 1 = 6 . Atualmente o Brasil tem 5570 municípios. Isso daria 5570 * 5569 * 5568 * ... . Quantos milhares de anos um computador precisaria para rodar esse algoritmo nesse caso? 😄
# Algoritmos que não tem solução conhecida em tempo polinomial, ou seja, que são fatoriais ou exponenciais , resolvíveis somente com força bruta, pertencem a uma categoria de problemas na computação chamada problemas NP Completos . Se quiser conhecer mais sobre essa categoria de problemas, explore nossos recursos adicionais!