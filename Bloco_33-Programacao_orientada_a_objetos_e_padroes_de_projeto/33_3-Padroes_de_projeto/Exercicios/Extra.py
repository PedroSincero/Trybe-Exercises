# Crie uma classe Movie x
# Seu construtor deve receber 2 parâmetros: title e gender x
# Crie os métodos de instância get_title, get_gender e update_gender x
# Crie o método get_art_type, que poderá ser chamado pela classe Movie x
# Crie a classe abstrata Art, com o método abstrato get_title x
# Crie a classe Poetry, sem atributos ou métodos
# Faça Movie e Poetry herdarem de Art

from abc import ABC, abstractmethod


class Art(ABC):
  @abstractmethod
  def get_title(self):
    pass

class Poetry(Art):
  def get_title(self):
    pass

class Movie(Art):
    def __init__(self, title, gender):
      self.title = title
      self.gender = gender

    def get_title(self):
      return self.title

    def get_gender(self):
      return self.gender

    def update_gender(self, update):
      self.gender = update

    @staticmethod
    def get_art_type():
      return "Visual"


if __name__ == "__main__":
    pulp_fiction = Movie("Pulp Fiction", "Ação")

    assert pulp_fiction.get_title() == "Pulp Fiction"
    assert pulp_fiction.get_gender() == "Ação"

    pulp_fiction.update_gender("Comédia")
    assert pulp_fiction.get_gender() == "Comédia"

    assert Movie.get_art_type() == "Visual"

    assert issubclass(Movie, Art)  # retorna True se Movie herda de Art
    assert issubclass(Poetry, Art)

    try:
        pulp_fiction = Movie("Bacurau", "Drama")
        cancao_exilio = Poetry()
    except TypeError as err:
        # confere a mensagem de erro
        err_msg = (
            "Can't instantiate abstract class Poetry "
            "with abstract method get_title"
        )
        assert err.args[0] == err_msg