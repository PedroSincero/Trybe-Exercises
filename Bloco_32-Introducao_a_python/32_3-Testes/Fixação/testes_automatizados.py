# Quem nunca arrumou um problema em um código e acabou fazendo-o deixar de funcionar para outro cenário? Ou ficou horas testando as mais diversas condições para um algoritmo e no meio do caminho teve de mexer no código e recomeçar tudo novamente. 😁
# Através de testes automatizados, a pessoa desenvolvedora é capaz de identificar mais facilmente um bug ou verificar que alterações do código não afetaram o comportamento esperado do sistema.
# Em nosso curso utilizaremos a biblioteca pytest , um framework que facilita a escrita de testes simples, mas capazes de testar funcionalidades complexas em aplicações e bibliotecas.

# 📝 Que tal vermos um exemplo?
# codigo.py
def is_odd(number):
    'Retorna True se um número é ímpar, senão False.'
    return number % 2 != 0

# test_codigo.py
from codigo import is_odd


def test_is_odd_when_number_is_odd_returns_true():
    'Para um número ímpar a função deve retornar o valor True'
    assert is_odd(3) is True


def test_is_odd_when_number_is_even_returns_false():
    'Para um número par a função deve retornar o valor False'
    assert is_odd(2) is False

# Notem que o nome do arquivo de testes possui o prefixo test_ , assim como a definição das funções de teste. Isto é necessário para que seus testes sejam descobertos pela ferramenta.
# Uma função de teste é similar a qualquer outra, porém tem o propósito de verificar se o resultado obtido foi o mesmo do esperado. No código isto pode ser visto através da utilização da palavra reservada assert .
# O comando assert funciona da seguinte maneira: caso a expressão recebida seja verdadeira (avaliada como True ), nada acontece, porém caso seja falsa (avaliada como False ), uma exceção do tipo AssertionError é lançada. A pytest captura este erro e tenta apresentar uma comparação entre o esperado e o recebido da melhor maneira possível.