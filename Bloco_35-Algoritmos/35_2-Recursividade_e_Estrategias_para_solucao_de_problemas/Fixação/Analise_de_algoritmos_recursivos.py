# Para que consigamos realizar a análise de algoritmos recursivos, nós iremos fazer uso da Árvore de Recorrência ! Mas o que é isso?!

# Árvore de Recursão

# O método da árvore de recursão pode ser utilizado para estimar o custo de um algoritmo. É um meio de analisarmos seu custo, o que nos ajuda a decidir se tal solução recursiva vale a pena ou não. Podemos visualizar nível a nível da estrutura de um algoritmo recursivo por meio de uma árvore recursiva. No final, tem-se a estimativa de tempo do problema. Vamos ver na prática como isso acontece para termos um melhor entendimento.

def fibonacci(num):  # nome da função e parâmetro
    if (num <= 1):  # condição de parada
        return num
    else:
        return fibonacci(num - 2) + fibonacci(num - 1)  # chamada de si mesma com um novo valor

# Acima estamos fazendo um código recursivo para cálculo de fibonacci. Na imagem abaixo visualizamos a representação do algoritmo fibonacci recursivo, que acabamos de montar, convertido em uma estrutura que chamamos de árvore:

# 💡 Lembre-se! Se você se embananar com as estratégias de análise de recursão, fique tranquilo(a), é um assunto mais desafiador e com o tempo e experiência esse conhecimento vem. E não deixe de falar com a gente no Slack se algum exemplo estiver te confundindo!
# Ou seja: desenhe todas as recursões do problema até chegar aos casos base e some as complexidades! Fique de olho nas proporções! Se cada subproblema é O(n) e você criou um para cada elemento da sua entrada de tamanho n , você tem aí uma complexidade O(n * n) , ou seja, uma complexidade quadrática. Se, por outro lado, a cada subproblema você dividiu o tamanho do problema original por dois, você gerará log n subproblemas. Se cada um desses custa O(n) , você teria uma complexidade O(n* log n)
# A forma de traduzir a lógica da árvore de recursão para uma notação puramente matemática se chama Teorema Mestre ! Não é o nosso escopo por agora, ok? Mas fique à vontade para pesquisar a respeito e nos trazer todas as perguntas, se quiser!

