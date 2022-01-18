# Todos os algoritmos recursivos devem obedecer a três leis importantes:

# 1) Um algoritmo recursivo deve ter um caso base : quando falamos de recursão, devemos sempre lembrar do caso base, pois sem ele nosso algoritmo ficará executando infinitamente. O caso base é a condição de parada do algoritmo recursivo, ele é o menor subproblema do problema, tornando-o possível de resolvê-lo de forma direta/trivial;

# ex: if < n return break;

# 2) Um algoritmo recursivo deve mudar o seu estado e se aproximar do caso base : após o início da execução de um algoritmo recursivo, a cada nova chamada a ele mesmo, o seu estado deve se aproximar cada vez mais do caso base. Por exemplo, vamos imaginar o seguinte: queremos criar um código que irá printar números a partir de 0 e terminar em 10. O caso base do algoritmo é 10 , pois é onde nossa função recursiva deve parar a execução. A primeira chamada a função terá o número 0 passado de parâmetro. A cada nova chamada à função, nosso estado deve incrementar o valor 1 ao valor do estado anterior, até chegar ao número 10. Logo, o valor do estado na primeira chamada será 0, na segunda chamada será 1, na terceira chamada será 2, e assim por diante até chegar ao valor do caso base;

# 3) Um algoritmo recursivo deve chamar a si mesmo, recursivamente : Essa lei é a própria definição de recursão.

# Entendendo recursividade e colocando em prática

# Antes de vermos como acontece a "mágica" da recursividade, vamos ver como costuma ser uma estrutura básica de uma função recursiva:

# Nome da função e parâmetro:
#     Condição de parada

#     Chamada de si mesma

# Declaramos uma função com um parâmetro. Dentro da função criada, definimos qual é a condição de parada da função. A condição de parada faz uma comparação entre o valor da condição com o parâmetro que a função está recebendo. Caso a condição não se satisfaça, a função é chamada novamente com um novo parâmetro. Caso contrário a execução para na condição de parada.
# Chega de teoria e vamos ver na prática como isso acontece. Para isso, vamos criar um arquivo python e escrever o código abaixo:

def countdown(n):  # nome da função e parâmetro
    if n == 0:  # condição de parada
        print('FIM!')
    else:
        print(n)
        countdown(n - 1)  # chamada de si mesma com um novo valor


countdown(5)

# No código acima temos uma função recursiva que chamamos de countdown . A ideia da função é fazer uma contagem regressiva de 5 até 0. Dito isso, primeira chamada que fazemos à função passamos o parâmetro inicial, no caso o número 5 . Nas outras vezes que a função for chamada é que vamos suprir a segunda lei da recursão , passando n - 1 , sendo n o número passado por parâmetro.
# Exemplo da execução do código:

# n = 5 -> não satisfaz a condição de parada / chama a função novamente: `countdown(5 - 1)`.  # primeira execução

# n = 4 -> não satisfaz a condição de parada / chama a função novamente: `countdown(4 - 1)`.  # segunda execução

# n = 3 -> não satisfaz a condição de parada / chama a função novamente: `countdown(3 - 1)`.  # terceira execução

# n = 2 -> não satisfaz a condição de parada / chama a função novamente: `countdown(2 - 1)`.  # quarta execução

# n = 1 -> não satisfaz a condição de parada / chama a função novamente: `countdown(1 - 1)`.  # quinta execução

# n = 0 -> satisfaz condição de parada / entra no if e printa "FIM!".                         # sexta execução

# Agora que entendemos melhor o código de uma função recursiva, vamos entender o que está acontecendo "por baixo dos panos". Para isso, precisamos, primeiro, entender alguns conceitos sobre pilha de execução:
# Toda vez que chamamos uma função em um programa, o sistema operacional reserva memória para as variáveis e parâmetros da função;
# Sempre quando uma função é executada, ela é guardada na pilha;
# Quando a função termina de ser executada, ela sai da pilha.
# Nota: Não se preocupe em entender, nesse momento, 100% dos conceitos de pilha, você irá ver esse conceito mais para frente. O importante aqui é que você entenda a parte conceitual do funcionamento da recursividade!

# Podemos perceber que cada vez que a função countdown é chamada, um novo dado é adicionado à uma pilha (canto direito do gif). É adicionado à pilha todos os valores executados, do 5 ao 1, até chegarmos no caso base 0 . Quando a execução acaba, os dados são retirados da pilha, um a um, de forma reversa (do 0 ao 5), até que a pilha esvazie e o processamento finalize.

# Vamos ver outro exemplo para fixarmos mais esse conceito. Dessa vez, vamos fazer um algoritmo recursivo para cálculo de fatorial. Vamos para o código!

def factorial_recursive(n):  # nome da função e parâmetro
    if n == 1:  # condição de parada
        return 1

    else:
        return n * factorial_recursive(n - 1)  # chamada de si mesma com um novo valor


factorial_recursive(5)

# Nessa função acontece, "por baixo dos panos", a mesma coisa que a função do exemplo anterior. Porém, explicando com outras palavras, internamente cada chamada recursiva à função adiciona um frame de pilha, até chegarmos ao caso base. Então, a pilha começa a se desenrolar à medida que cada chamada retorna seus resultados:

# Para praticar, vamos fazer um exercício:

# Exercício 3: Faça um algoritmo recursivo de soma. Esse algoritmo deve receber um número de parâmetro e deve somar todos os números antecessores a ele.

# Número passado por parâmetro à função: 4

# Execução: 4 + 3 + 2 + 1

# Resultado: 10

def algoritmo_soma(n):
  if n == 1:
    return n
  else:
    return n + algoritmo_soma(n - 1)