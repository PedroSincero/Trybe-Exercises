from abc import ABC, abstractmethod
import gzip
import json
from zipfile import ZipFile


class ZipCompressor():
    ''' Nossos compressores terão fixado o local de salvamento
    do arquivo, então vamos defini-lo nos construtores'''
    def __init__(self, filepath='./'):
        self.filepath = filepath

    def compress(self, file_name):
        with ZipFile(file_name + '.zip', 'w') as zip_file:
            zip_file.write(file_name)


class GzCompressor():
    def __init__(self, filepath='./'):
        self.filepath = filepath

    def compress(self, file_name):
        with open(file_name, 'rb') as content:
            with gzip.open(file_name + '.gz', 'wb') as gzip_file:
                gzip_file.writelines(content)


class SalesReport(ABC):
    # Nossa classe agora espera *instâncias* de compressor como um parâmetro.
    # Temos um valor padrão para suportar o código que usava as SalesReport
    # sem parâmetros -- não precisa correr pra re-escrever nada ;)
    def __init__(self, export_file, compressor=GzCompressor()):
        self.export_file = export_file
        self.compressor = compressor

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

    # Aqui temos um atributo de classe!
    FILE_EXTENSION = ''

    def get_export_file_name(self):
      # Aqui usamos o atributo de classe
      # Vai fazer mais sentido nas classes herdeiras!
      return self.export_file + self.FILE_EXTENSION

    def compress(self):
        self.serialize()
        self.compressor.compress(self.get_export_file_name())

    @abstractmethod
    def serialize(self):
        raise NotImplementedError


class SalesReportJSON(SalesReport):
    # Nós não reimplementamos o get_export_file_name
    # mas como ele usa um atributo de classe pra pegar a extensão
    # só de redefinir o atributo já vamos conseguir mudar o resultado!
    FILE_EXTENSION = '.json'

    def serialize(self):
        with open(self.get_export_file_name(), 'w') as file:
            json.dump(self.build(), file)


class SalesReportCSV(SalesReport):
    # Sua implementação vai aqui
    pass


# Para testar
relatorio_de_compras = SalesReportJSON('meu_relatorio_1')
relatorio_de_vendas = SalesReportJSON('meu_relatorio_2', ZipCompressor())

relatorio_de_compras.compress()
relatorio_de_vendas.compress()

# Composição e Interfaces
# Nós falamos lá em cima que qualquer outra classe de compressor que surgir funcionará com nosso código! Certo? Observe que, pra isso acontecer, tal classe precisa, necessariamente, implementar a função .compress() com a mesma assinatura que nossas duas classes atuais.
# O grande risco que temos ao fazer composição é a classe que passarmos para a outra não ter o mesmo formato que imaginamos! Ou seja: se o nosso novo compressor não tiver uma função chamada compress que receba o mesmo parâmetro que definimos, usá-la dará erro. Como podemos garantir que isso nunca acontecerá? Nós podemos fazer um combinado na empresa mas, já diria o sábio:
# Um combinado que não está codado não existe. (Clarice Lispector)
# Como a gente coda um combinado ?! A resposta...? Definindo uma interface!
# Você, então, dita uma regra: Todo compressor deve ter uma função chamada compress que receba esse parâmetro! E como você faz isso?
# Com...

# ...


class Compressor(ABC):
    def __init__(self, filepath='./'):
        self.filepath = filepath

    @abstractmethod
    def compress(self, file_name):
        raise NotImplementedError


class ZipCompressor(Compressor):
    def compress(self, file_name):
        with ZipFile(file_name + '.zip', 'w') as zip_file:
            zip_file.write(file_name)


class GzCompressor(Compressor):
    def compress(self, file_name):
        with open(file_name, 'rb') as content:
            with gzip.open(file_name + '.gz', 'wb') as gzip_file:
                gzip_file.writelines(content)

# Com uma classe abstrata 😎
# Ou seja: todo compressor que for criado precisa ter uma função compress que receberá esse parâmetro específico para funcionar!
# Você usa uma classe abstrata com um método abstrato para definir uma interface que, através de herança , definirá o comportamento de todos os compressores futuros, assegurando que sua composição sempre funcionará!
