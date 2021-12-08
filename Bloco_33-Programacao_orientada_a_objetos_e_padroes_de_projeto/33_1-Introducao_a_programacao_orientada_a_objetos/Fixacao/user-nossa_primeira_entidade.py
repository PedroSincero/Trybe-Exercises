# O que é a nossa entidade User? É alguém que quer recuperar uma senha por email. Esse alguém, portanto, tem um email e uma senha. Para identificarmos a pessoa, vamos dar um nome também. Por enquanto, parece que é só disso que precisamos. O Python nos dá ferramentas para criar entidades da forma como quisermos! Com o exemplo, vamos conhecer essas ferramentas um pouco melhor.

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

# No Python, a palavra reservada class é usada, como você talvez imagine, para definir entidades. Não uma entidade específica, uma pessoa específica, mas a entidade de uma forma um pouco mais abstrata, como vimos acima. "Uma entidade user contém um nome, um email e uma senha". É isso que fizemos aí em cima. Para, a partir dessa definição, criarmos uma entidade, precisamos do código abaixo:

class User:
    def __init__(self, name, email, password):
        """ Método construtor da classe User. Note que
        o primeiro parâmetro deve ser o `self`. Isso é
        uma particularidade de Python, vamos falar mais
        disso adiante!"""
        self.name = name
        self.email = email
        self.password = password

# Para invocar o método construtor, a sintaxe é NomeDaClasse(parametro 1, parametro 2)
# Repare que o parâmetro self foi pulado -- um detalhe do Python.
meu_user = User("Valentino Trocatapa", "valentino@tinytoons.com", "Grana")
print(meu_user)
print(meu_user.name)
print(meu_user.email)
print(meu_user.password)

# A variável `meu_user` contém o objeto criado pelo construtor da classe User!
