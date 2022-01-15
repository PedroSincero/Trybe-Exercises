def sum_array(numbers):
    sum = 0
    for number in numbers:
            sum += number

    return sum

# Quanto tempo ele vai demorar para executar? 😁
# "Ora, impossível dizer!", diz a pessoa incrédula. Depende da máquina, do que está rodando nela, dos recursos, de tudo! Não dá pra dizer.
# Ok. Trave todas as configurações. É uma máquina padronizada, sem mais nada rodando, tudo certo. Quanto tempo ele vai demorar para executar? Um segundo? Dez segundos?
# ... Tem mais um "depende" aqui, não tem? O tempo de execução depende do tamanho do array passado por parâmetro! Quanto maior o dado passado por parâmetro, mais o algoritmo demorará para executar .
# Hmmm. Legal! Vamos usar isso então! Eu não sei quanto tempo o algoritmo vai demorar para executar: dependem de inúmeros fatores além do meu controle. Mas uma coisa eu tenho certeza: o tempo de execução dele é proporcional ao tamanho do meu dado entrado! Por exemplo:

# def sum_array(numbers):
  # ...

# Suponha que, para o array abaixo, o tempo de execução seja `n`
sum_array(array_com_dez_mil_numeros)

# Nesse caso, aqui o tempo de execução vai ser `10 * n`, ou `10n`, já que o array é dez vezes maior que o anterior!
sum_array(array_com_cem_mil_numeros)

# Já esse é dez mil vezes maior que o primeiro, então esse aqui executa em `100n`
sum_array(array_com_um_milhão_de_numeros)

# Pois bem!! A todas e a todos eu tenho o orgulho de apresentar a Ordem de Complexidade ! Mas o que raios é isso?! É o quanto que o tempo de execução do algoritmo varia na medida em que a entrada cresce! Observe:

# def sum_array(numbers):
  # ...

sum_array(array_com_dez_mil_numeros)
# O tempo de execução deste algoritmo foi 0.0004s

sum_array(array_com_cem_mil_numeros)
# Para uma execução com dez vezes mais números, o tempo aumentou em dez vezes: 0.004s

sum_array(array_com_um_milhão_de_numeros)
# Multiplicando o tamanho da entrada por dez novamente, temos um tempo dez vezes maior: 0.05s

# Faça o teste na sua máquina (você já tem os conhecimentos para descobrir como fazer um script que mede esses tempos 🚀). Os valores podem variar, mas as proporções não! Um aumento no tamanho da entrada aumenta o tempo de execução na mesma proporção. Se fizéssemos um gráfico disso, ele seria assim:

# A Ordem de Complexidade nada mais é do que a representação dessa proporção! Dado que o algoritmo é linearmente proporcional ao tempo de execução (ou seja, se a entrada aumenta em 10 vezes o tempo de execução também aumenta em 10 vezes), dizemos que este é um algoritmo linear!
# A função matemática que representa uma relação linear é f(n) = n . Na notação de Ordem de Complexidade, dizemos que esse algoritmo é O(n) ! Guardem essa notação, vamos usá-la bastante!
# 💡 A Ordem de Complexidade pode ser chamada, também, de Complexidade Assintótica.