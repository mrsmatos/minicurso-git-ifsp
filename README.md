# Minicurso Git e GitHub na Prática

Repositório de exemplo do minicurso do IFSP - Campus Barretos.
**Do primeiro commit aos testes automatizados.**

## O que tem aqui

| Arquivo / pasta | Para que serve |
|---|---|
| `calculadora.py` | Funções simples usadas nos exemplos |
| `mural.py` | Mostra o mural com todos os integrantes |
| `equipe/` | Um arquivo por pessoa: é aqui que você entra no projeto |
| `tests/` | Testes automatizados (pytest) |
| `.github/workflows/testes.yml` | GitHub Actions: roda os testes a cada push e Pull Request |

## Como executar

```bash
python calculadora.py
python mural.py
python -m pytest -v
```

## Como entrar na equipe (resumo)

1. Faça um **fork** deste repositório no GitHub.
2. `git clone` do **seu** fork.
3. `git switch -c adiciona-SEU_USUARIO`
4. `cp equipe/_modelo.py equipe/SEU_USUARIO.py` e edite NOME, PERIODO e a mensagem.
5. `git add`, `git commit`, `git push -u origin adiciona-SEU_USUARIO`
6. Abra um **Pull Request** para este repositório e espere os testes ficarem verdes.
