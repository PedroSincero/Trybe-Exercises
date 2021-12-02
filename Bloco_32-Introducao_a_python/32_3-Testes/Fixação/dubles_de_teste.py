# Na literatura encontramos as técnicas de dublê com os nomes mocks , fakes , stubs e spy , e de uma forma bem resumida podemos defini-las:
# fakes: objetos que possuem implementações funcionais, porém normalmente simplificadas;
# mocks: são pré programados para verificarem as chamadas das funções que receberem;
# stubs: proveem respostas predefinidas;
# spies: são como stubs, mas também armazenam informações de como foram chamados.

# Vamos analisar dois cenários e escrever seus respectivos testes utilizando dublês, evitando assim a dependência externa a um arquivo real.
# No primeiro cenário nós temos nossa dependência externa (o arquivo) sendo recebido como parâmetro.
# pokemon.py

import json


def retrieve_pokemons_by_type(type, reader):
    # lê o conteudo de reader e o transforma de json
    # para dicionário
    pokemons = json.load(reader)["results"]
    # filtra somente os pokemons do tipo escolhido
    pokemons_by_type = [
        pokemon for pokemon in pokemons if type in pokemon["type"]
    ]
    return pokemons_by_type

# Vamos utilizar uma técnica onde substituiremos a abertura do nosso arquivo real por um objeto que possui as implementações funcionais de um arquivo (método read , necessário na operação de leitura). Este objeto será alocado na memória, "simulando" nosso arquivo real.
# test_pokemon.py
import json
from pokemon import retrieve_pokemons_by_type
from io import StringIO


def test_retrieve_pokemons_by_type():
    # definimos um pokemon do tipo grama
    grass_type_pokemon = {
        "national_number": "001",
        "evolution": None,
        "name": "Bulbasaur",
        "type": ["Grass", "Poison"],
        "total": 318,
        "hp": 45,
        "attack": 49,
        "defense": 49,
        "sp_atk": 65,
        "sp_def": 65,
        "speed": 45,
    }
    # definimos também um pokemon do tipo água
    water_type_pokemon = {
        "national_number": "007",
        "evolution": None,
        "name": "Squirtle",
        "type": ["Water"],
        "total": 314,
        "hp": 44,
        "attack": 48,
        "defense": 65,
        "sp_atk": 50,
        "sp_def": 64,
        "speed": 43,
    }
    # criamos um arquivo em memória que o seu conteúdo são os dois pokemons
    fake_file = StringIO(
        json.dumps({"results": [grass_type_pokemon, water_type_pokemon]})
    )
    # quando pesquisamos por pokemons do tipo grama,
    # o pokemon do tipo água não deve ser retornado
    assert retrieve_pokemons_by_type("Grass", fake_file) == [
        grass_type_pokemon
    ]

# Um segundo cenário é onde a função espera o nome de um arquivo e a abertura do mesmo acontece dentro da função.
# pokemon.py

import json


def retrieve_pokemons_by_type(type, filepath):
    with open(filepath) as file:
        pokemons = json.load(file)["results"]
        pokemons_by_type = [
            pokemon for pokemon in pokemons if type in pokemon["type"]
        ]
        return pokemons_by_type

# Para escrever este teste, vamos aproveitar da natureza dinâmica da linguagem e substituir o método open em tempo de execução por um objeto mock_open , que já vem embutido na linguagem e se comporta como o open , retornando o que foi definido em read_data como seu conteúdo. Um detalhe interessante é que esse objeto obtido através da função mock_open também possui a capacidade de armazenar informações sobre como foram as chamadas de seus métodos e os parâmetros recebidos.
# test_pokemon.py

import json
from unittest.mock import mock_open, patch
from pokemon import retrieve_pokemons_by_type

def test_retrieve_pokemons_by_type():
    # definimos um pokemon do tipo grama
    grass_type_pokemon = {
        "national_number": "001",
        "evolution": None,
        "name": "Bulbasaur",
        "type": ["Grass", "Poison"],
        "total": 318,
        "hp": 45,
        "attack": 49,
        "defense": 49,
        "sp_atk": 65,
        "sp_def": 65,
        "speed": 45,
    }
    # definimos também um pokemon do tipo água
    water_type_pokemon = {
        "national_number": "007",
        "evolution": None,
        "name": "Squirtle",
        "type": ["Water"],
        "total": 314,
        "hp": 44,
        "attack": 48,
        "defense": 65,
        "sp_atk": 50,
        "sp_def": 64,
        "speed": 43,
    }
    pokemon_json_content = json.dumps({"results": [grass_type_pokemon, water_type_pokemon]})
    # substituímos a função padrão do python open por mock_open
    # uma versão que se comporta de forma parecida, porém simulada
    with patch("builtins.open", mock_open(read_data=pokemon_json_content)):
        # repare que o nome do arquivo não é importante aqui
        # a esses parâmetros não utilizados damos o nome de dummies
        # como neste contexto alteramos o open pelo mock_open,
        # o argumento "dummy" poderia ser substituído por qualquer coisa, já que não será utilizado pela função
        assert retrieve_pokemons_by_type("Grass", "dummy") == [
            grass_type_pokemon
        ]

# A primeira abordagem torna o código menos acoplado a um arquivo e nos permite utilizar qualquer objeto (que tenha o método reader) em seu lugar. Assim, essa função pode ser reutilizável, por exemplo, para ler pokemons a partir de uma requisição web ou outra fonte.
# 💡 Testes de unidade são muito importantes, mas não se esqueça de testar também a integração de suas funções e a funcionalidade como um todo.
# https://martinfowler.com/bliki/TestDouble.html