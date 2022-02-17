import pytest
from func_fibo import fibonacci_

def test_Zero():
    resultado = fibonacci_(0)
    assert resultado == 'Não possivel realizar essa Operação, pois o valor foi 0'

def test_Cinco():
    resultado = fibonacci_(5)
    assert resultado == [0, 1, 1, 2, 3]

def test_Dez():
    resultado = fibonacci_(10)
    assert resultado == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
