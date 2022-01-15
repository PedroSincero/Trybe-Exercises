# # Beleza! Vamos resumir o que vimos até aqui:
# A Ordem de Complexidade diz o quanto o tempo de execução (ou espaço de memória ocupado) de um algoritmo cresce, na medida em que aumentamos o tamanho da sua entrada!
# Uma O(1) executa no mesmo tempo independente do tamanho da entrada. Como exemplo, lembre-se do acesso a um elemento do array , estudado na aula de ontem. Esse acesso é O(1) , pois leva o mesmo tempo, independente do tamanho do array;
# Uma O(n) significa que o algoritmo é linear : se aumentamos a entrada em 2 vezes , aumentamos o tempo de execução em 2 vezes ;
# Uma O(n²) significa que o algoritmo é quadrático : se aumentamos a entrada em 2 vezes , aumentamos o tempo de execução em 4 (2²) vezes ;
# Uma O(n³) significa que o algoritmo é cúbico : se aumentamos a entrada em 2 vezes , aumentamos o tempo de execução em 8 (2³) vezes .

# Falamos aqui de algoritmos O(n) , O(n²) e até de O(n³) , mas vamos mostrar o que eles significam de outra forma.

# Para se ter uma noção, pense assim: para um algoritmo linear, com n = 1000 temos mil operações. Quando o algoritmo é O(n²) um n = 1000 gera um milhão de operações . Essa mesma quantidade (um milhão) para O(n³) , se atinge com n = 100 . Está começando a entender como alguns algoritmos podem, rapidinho, ficar inviáveis de se executar?
# A seguir, vamos explorar outros tipos de complexidades de algoritmos!
# 💡 Lembre-se! Se você se embananar com essa quantidade de números, rode exemplos na sua máquina contando o número de iterações! É uma excelente forma de visualizar a complexidade acontecendo. E não deixe de falar com a gente no Slack se algum exemplo estiver te confundindo!