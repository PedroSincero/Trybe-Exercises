# Nós queremos estender nosso código sem modificar o que já existe . Leia o código abaixo! Ele faz a mesma coisa que o código anterior, mas está refatorado. Ele usa, para resolver o nosso problema, os conceitos de classes abstratas, métodos abstratos e o conceito de herança .

from abc import ABC, abstractmethod
import json
from csv import DictWriter

class SalesReport(ABC):
    def __init__(self, export_file):
        self.export_file = export_file

    def build(self):
        return [{
                'Coluna 1': 'Dado 1',
                'Coluna 2': 'Dado 2',
                'Coluna 3': 'Dado 3'
                },
                {
                'Coluna 1': 'Dado A',
                'Coluna 2': 'Dado B',
                'Coluna 3': 'Dado C'
                }]

    @abstractmethod
    def serialize(self):
        raise NotImplementedError


class SalesReportJSON(SalesReport):
    def serialize(self):
        with open(self.export_file + '.json', 'w') as file:
            json.dump(self.build(), file)


# 💡 Como boa prática, cada classe deve ser definida em seu próprio arquivo! Para nossos exercícios isso não é necessário
# Herança nada mais é do que especializar o comportamento de uma classe. A classe herdeira é tudo que a classe ascendente é e um pouco mais! Pense assim:
# Se FileCompressor é a classe ascendente, ZipFileCompressor e TarFileCompressor são classes herdeiras! Ambas são um tipo específico de compressor de arquivos.
# Se DatabaseConnector é a classe ascendente, MySQLConnector e MongoConnector são as classes herdeiras! Ambas são um tipo específico de conector de banco de dados.
# Se Model é a classe ascendente, UserModel é a classe herdeira! É um tipo específico de model .
# Se Service é a classe ascendente, AuthenticationService é a classe herdeira! É um tipo específico de service .
# 💡 Lembre-se: O Model Service Controller é uma arquitetura que usa como base a Programação Orientada a Objetos!
# A Programação Orientada a Objetos, portanto, te dá o poder de criar classes herdeiras que especializam, mais e mais, o comportamento das classes ascendentes! Não há limite pra quantidade de classes herdeiras que uma classe pode ter, mas é crucial que tais classes sempre sejam uma especialização de comportamento! Já já vamos ver o porquê.
# No Python, definimos uma classe como herdeira da outra na linha que a define, como acima em class SalesReportJSON(SalesReport) . A lógica é: class MinhaClasseHerdeira(ClasseAscendente)

# Exercício de Fixação
# Antes de prosseguirmos para entender o que é aquele @abstractmethod e aquele (ABC) , vamos fixar o entendimento de herança! Implemente uma classe SalesReportCSV que seja herdeira da classe SalesReport , da mesma forma que fizemos com a SalesReportJSON . Para testar seu funcionamento, instancie-a e chame sua função serialize .

class SalesReportCSV(SalesReport):
    def serialize(self):
      with open(self.export_file + '.csv', 'w') as file:
        headers = ['Coluna 1', 'Coluna 2', 'Coluna 3']
        csv_writer = DictWriter(file, headers)
        csv_writer.writeheader()
        for item in self.build():
          csv_writer.writerow(item)

relatorio_de_vendas = SalesReportJSON('meu_relatorio')
relatorio_de_vendas.serialize()

relatorio_de_compras = SalesReportCSV('meu_relatorio')
relatorio_de_compras.serialize()

# https://dictionary.cambridge.org/pt/dicionario/ingles/serialization
# Serializar é o processo de mudar o formato dos seus dados para que possam ser armazenados ou enviados para serem, depois, convertidos de volta à sua forma original