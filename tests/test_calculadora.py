"""Testes automatizados da calculadora (rode com: python -m pytest -v)."""
import pytest

from calculadora import dividir, multiplicar, somar, subtrair


def test_somar():
    assert somar(2, 3) == 5


def test_subtrair():
    assert subtrair(7, 4) == 3


def test_multiplicar():
    assert multiplicar(6, 5) == 30


def test_dividir():
    assert dividir(9, 3) == 3


def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(1, 0)
