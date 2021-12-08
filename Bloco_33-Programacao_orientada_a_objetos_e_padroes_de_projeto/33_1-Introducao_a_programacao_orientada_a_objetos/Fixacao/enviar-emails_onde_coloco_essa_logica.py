# Enviar emails - onde coloco essa lógica?
# Bem! Se temos uma entidade User que quer enviar emails de recuperação de senha, em princípio faz sentido que essa entidade saiba enviar emails, certo? Então bora lá! Para uma entidade saber fazer algo, precisamos definir nela uma função que represente essa ação. Algo assim:

class User:
    def __init__(self, name, email, password):
        """ Método construtor da classe User. Note que
        o primeiro parâmetro deve ser o `self`. Isso é
        uma particularidade de Python, vamos falar mais
        disso adiante!"""
        self.name = name
        self.email = email
        self.password = password

    def reset_password(self):
        print("Envia email de reset de senha")


meu_user = User("Valentino Trocatapa", "valentino@tinytoons.com", "Grana")
meu_user.reset_password()

# Olha que interessante! Se definimos numa classe uma função, podemos chamar ela a partir do objeto que criamos! Quando pedimos para um objeto fazer algo, dizemos que estamos enviando uma mensagem àquele objeto . Atenção para isso! Na essência, toda lógica da orientação a objetos parte do envio de mensagens entre objetos.
# No código acima, estamos pedindo para meu_user resetar sua senha! Não nos interessa como a ação será feita, só nos interessa que ela será feita! Imagine duas pessoas escrevendo esse código. A pessoa que cria o objeto e pede que ele resete sua senha não precisa saber como ele faz isso! Temos uma classe bem nomeada, com uma função bem nomeada, e isso basta! Ao invés de gastar tempo precioso entendendo seu código, a pessoa pode usá-lo sem esse esforço!

class User:
    # Não preciso saber como a classe funciona, lalalalala

    def reset_password(self):
      # A classe tem essa função? Ótimo! Pra mim basta!


# Já sei o suficiente pra agir!
meu_user = User("Valentino Trocatapa", "valentino@tinytoons.com", "Grana")
meu_user.reset_password()