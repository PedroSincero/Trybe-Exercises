# Erros acontecem e nem sempre são inesperados. O Python utiliza de exceções para sinalizar que ocorreram erros durante a execução de um código e que nem sempre são fatais.
# Podemos escrever testes que verificam que um erro deve ocorrer a partir de uma determinada entrada.
# 📝 Um exemplo pode ser visto abaixo:

# codigo.py

# ...

def divide(a_number, other_number):
    "Retorna a divisão de a_number por other_number"
    return a_number / other_number

# test_codigo.py
import pytest
from codigo import is_odd, divide

# ...

def test_divide_when_other_number_is_zero_raises_an_exception():
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide(2, 0)