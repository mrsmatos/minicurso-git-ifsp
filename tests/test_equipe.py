"""Confere se cada arquivo da pasta equipe/ segue o modelo combinado."""
import pytest

from mural import carregar_integrantes

INTEGRANTES = carregar_integrantes()


def test_existe_pelo_menos_um_integrante():
    assert len(INTEGRANTES) >= 1


@pytest.mark.parametrize("pessoa", INTEGRANTES, ids=lambda m: m.__name__)
def test_cartao_segue_o_modelo(pessoa):
    assert isinstance(pessoa.NOME, str) and pessoa.NOME.strip() != ""
    assert pessoa.NOME != "Seu Nome Completo", "Troque o NOME pelo seu nome"
    assert pessoa.PERIODO in range(1, 9), "PERIODO deve ser um numero de 1 a 8"
    assert isinstance(pessoa.mensagem(), str) and pessoa.mensagem().strip() != ""
