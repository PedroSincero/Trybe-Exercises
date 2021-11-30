# Digite algumas operações básicas como adições e multiplicações e veja que o valor será avaliado e impresso.

 2 * 3  # saída: 6
 2 + 3  # saída: 5
 3 / 2  # saída: 1.5

#  Para atribuir esses valores a um nome, basta utilizar o operador de atribuição = .

square_root = 25 ** (1/2)  # raiz quadrada de 25. O operador `**` significa "elevado a"

print(square_root + 1)  # saída: 6.0

# Não é necessário a utilização de let , var ou const nas atribuições. Veremos escopo e questões de mutabilidade mais adiante.
# Mas existe algum operador que Python não tenha? E se eu tentar incrementar um valor?

counter = 0
# counter++  # esse código vai falhar

# Ainda que possamos simplificar operações e atribuições, o incremento ou decremento não é válido na sintaxe ++ , -- .
# Um exemplo de simplificação válida é:

# original
counter = counter + 1

# simplificado
counter += 1

# Um outro operador que pode ser um pouco diferente é o // . Consegue imaginar para que serve?

3 // 2  # saída: 1
3 / 2  # saída: 1.5

# O operador // realiza a divisão e arredonda o resultado para baixo. Ou seja, realiza o quociente.
# Hummm... Tirando o let e var , ainda parece bem similar com Javascript .🤔
# De fato, operadores são comuns a todas as linguagens de programação, por isso tamanha semelhança.
# Porém, nem tudo é tão semelhante. Se realizarmos a operação de comparação entre '1' == 1 , o resultado será falso ( False ), pois como são valores de tipos diferentes, nenhuma conversão é realizada.
# Dado as listas a = [1, 2, 3] e b = [1, 2, 3] , se compararmos as duas a == b teremos como retorno True , ainda que representem listas diferentes.
# Acho que "Python" != "Javascript" , ainda que tenham suas similaridades. 😅
# Mas e sobre os operadores && e || , não são operações de and e or ?
# Quando queremos fazer operações lógicas, como verificar se uma temperatura está entre dois valores, utilizamos o operador and . Ou seja, para verificar se uma temperatura é menor que 25 graus e maior que 18 graus, podemos fazer algo como temperatura < 25 and temperatura > 18 . Embora uma maneira mais pythonica de se escrever esta operação seja 18 < temperatura < 25 . 🤓
# Assim como podemos validar intervalos utilizando o operador or . Por exemplo, se em um parque pessoas com idade menor ou igual a 5 e maiores de 65 anos não pagam, poderíamos escrever uma validação da seguinte maneira idade <= 5 or idade >= 65 .


# Exercício 1: No terminal, inicialize duas variáveis a e b, sendo a = 10 e b = 5. Mostre o resultado das 7 operações básicas (soma, subtração, multiplicação, divisão, divisão inteira, potenciação e módulo) envolvendo essas variáveis.
a = 10
b = 5
a + b # 15 soma
a - b # 5  subtração
a * b # 50 multiplicação
a / b # 2.0  divisão
a // b # 2 divisão inteira
a ** b # 100000 potenciação
a % b # 0 módulo
# Exercício 2: Declare e inicialize uma variável: hours = 6 . Quantos minutos têm em 6 horas? E quantos segundos? Declare e inicialize variáveis minutes e seconds que recebem os respectivos resultados das contas. Depois, imprima cada uma delas.
hours = 6
minutes = hours * 60 # 360
seconds = minutes * 60 # 21600
# Exercício 3: Teste e verifique o que acontece se você colocar um ponto e vírgula no final de uma instrução em Python.
1 + 1; ola = 8
# Exercício 4: Suponha que o preço de capa de um livro seja 24,20, mas as livrarias recebem um desconto de 40%. O transporte custa 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias? Escreva uma expressão que receba o custo total e a imprima.
# porcentagem >> 0.4 * 24,20
#  1 = 100%, 0.4 = 40%
books = 60
book_price = (1 - 0.4) * 24.20 #14,52
logistic = 3 + (books - 1) * 0.75
cost = books * book_price + logistic
cost
