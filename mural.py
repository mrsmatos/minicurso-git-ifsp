"""Mostra o mural com todos os integrantes da equipe.

Cada pessoa adiciona UM arquivo dentro da pasta equipe/.
Rode com:  python mural.py
"""
import importlib
import pkgutil
import sys

import equipe

# Garante que nomes com acento aparecam corretamente no Git Bash do Windows.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def carregar_integrantes():
    integrantes = []
    for modulo in sorted(pkgutil.iter_modules(equipe.__path__), key=lambda m: m.name):
        if modulo.name.startswith("_"):
            continue  # ignora o _modelo.py
        integrantes.append(importlib.import_module(f"equipe.{modulo.name}"))
    return integrantes


def main():
    integrantes = carregar_integrantes()
    print("=" * 60)
    print(" MURAL DA EQUIPE - Git e GitHub na Pratica (IFSP Barretos)")
    print("=" * 60)
    for pessoa in integrantes:
        if getattr(pessoa, "PROFESSOR", False):
            rotulo = "professor"
        else:
            rotulo = f"{pessoa.PERIODO}o periodo"
        print(f"* {pessoa.NOME} ({rotulo})")
        print(f'    "{pessoa.mensagem()}"')
    print("-" * 60)
    print(f"Total de integrantes: {len(integrantes)}")


if __name__ == "__main__":
    main()
