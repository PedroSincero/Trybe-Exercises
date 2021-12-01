# Módulos
# Um módulo é um arquivo que contém definições e instruções em Python. O nome do arquivo é um nome acrescido de .py . Dentro de um outro arquivo python, você pode importar um módulo e ter acesso às suas funções, classes, etc.
# Em linhas gerais, todo arquivo que é escrito com a linguagem Python e com a extensão .py é considerado um módulo.
# Observe o arquivo my_math.py abaixo:
def sum(a, b):
  return a + b


def pot(a, b):
  return a ** b


print(sum(2, 2))
print(pot(2, 3))

# Pacotes 📦
# Pacotes são módulos Python que contêm outros módulos e/ou pacotes , comumente separados por responsabilidades similares. Na prática, um pacote é um diretório que pode conter vários módulos (arquivos de extensão .py ) e/ou outros pacotes .
# Exemplo de tipos diferentes de imports de pacotes :

import http  # importa o pacote http como um módulo

from http import client  # importa o módulo client do pacote http

from http.client import HTTP_PORT  # importa a constante HTTP_POST do módulo client do pacote http