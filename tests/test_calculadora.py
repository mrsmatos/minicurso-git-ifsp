"""Testes automatizados da calculadora (rode com: python -m pytest -v)."""
from calculadora import multiplicar, somar, subtrair


def test_somar():
    assert somar(2, 3) == 5


def test_subtrair():
    assert subtrair(7, 4) == 3


def test_multiplicar():
    assert multiplicar(6, 5) == 30
