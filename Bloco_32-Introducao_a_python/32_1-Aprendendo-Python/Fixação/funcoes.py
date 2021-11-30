# Notamos que funções são definidas através da palavra reservada def , seguido por um nome e os parâmetros entre parenteses. Como todo bloco de código em Python o caractere : define o início do bloco e a indentação seu fim.
# Os parâmetros podem ser passados de forma posicional ou nomeada. Os posicionais são aqueles definidos através da posição ao qual é chamado e os nomeados são definidos através do nome.

def soma(x, y):
    return x + y

soma(2, 2)  # os parâmetros aqui são posicionais

soma(x=2, y=2)  # aqui estamos nomeando os parâmetros

# Os parâmetros também podem ser variádicos. Ou seja, podem variar em sua quantidade. Parâmetros posicionais variádicos são acessados como tuplas no interior de uma função e parâmetros nomeados variádicos como dicionário.
def concat(*strings):
    # Equivalente a um ", ".join(strings), que concatena os elementos de um iterável em uma string utilizando um separador
    # Nesse caso a string resultante estaria separada por vírgula
    final_string = ""
    for string in strings:
        final_string += string
        if not string == strings[-1]:
            final_string += ', '
    return final_string

# pode ser chamado com 2 parâmetros
concat("Carlos", "João")  # saída: "Carlos, João"

# pode ser chamado com um número n de parâmetros
concat("Carlos", "João", "Maria")  # saída: "Carlos, João, Maria"

# dict é uma função que já vem embutida no python
dict(nome="Felipe", sobrenome="Silva", idade=25)  # cria um dicionário utilizando as chaves passadas

dict(nome="Ana", sobrenome="Souza", idade=21, turma=1)  # o número de parâmetros passados para a função pode variar

# Variáveis definidas dentro das funções tem escopo local, porém uma função quando não encontra um nome no escopo local irá procurar no espaço de nomes global.
# Em alguns casos, podemos querer limitar um parâmetro em nomeado ou posicional para evitar ambiguidades e/ou aumentar legibilidade.

len([1, 2, 3, 4])  # função len não aceita argumentos nomeados

len(obj=[1, 2, 3, 4])  # este código irá falhar

print("Botaro", "Cássio", ", ")  # imprime Botaro Cássio ,

print("Botaro", "Cássio", sep=", ")  # nomeando o terceiro parâmetro, agora temos a saída: Botaro, Cássio