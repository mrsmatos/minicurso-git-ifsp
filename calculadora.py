"""Calculadora simples usada no minicurso de Git e GitHub."""


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("Nao e possivel dividir por zero")
    return a / b


if __name__ == "__main__":
    print("2 + 3 =", somar(2, 3))
    print("7 - 4 =", subtrair(7, 4))
    print("6 x 5 =", multiplicar(6, 5))
    print("9 / 3 =", dividir(9, 3))
