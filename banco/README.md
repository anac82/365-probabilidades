# banco/ — o livro-caixa do 365 Probabilidades

Um arquivo SQLite (`365.db`) com dez tabelas. Linhas entram; só `dias.status`,
`validacoes.resolvido` e `pendencias.resolvida` mudam.

| arquivo | o que é |
|---|---|
| `365.db` | o banco |
| `schema.sql` | as dez tabelas e três consultas prontas (`v_colisao`, `v_calendario`, `v_cota_forma`) |
| `db.py` | funções de apoio: `colisao`, `calendario`, `ideia`, `exportar` |
| `carga_inicial.py` | como o banco foi carregado em 27/09/2026 (notebooks + fontes_usadas.md + dashboard) |
| `csv/` | uma cópia de cada tabela, regravada por `python3 banco/db.py exportar`, para o diff no GitHub ser legível |

## Rotina

    python3 banco/db.py colisao Sobrenome     # antes de propor tema
    python3 banco/db.py calendario            # o que falta em cada dia
    python3 banco/db.py ideia "Qual a chance de ..."
    python3 banco/db.py exportar              # depois de cada sessão, antes do commit

## O que a carga inicial deixou marcado para conferir

- `fontes.nota` = "carga inicial" em todas as 278 linhas: autor, ano, N e revista foram extraídos do bloco Fontes de cada notebook por regra, não à mão. N ausente em 169 linhas (o notebook não o traz no bloco, ou está em prosa).
- `dias.x080` foi inferido do código e das notas metodológicas (sim 30, não 68, sem sinal 12).
- `modelos.metodo` foi inferido do código que antecede cada `savefig`; `auditoria` vazia.
- Dias na gaveta receberam números provisórios 901 a 919.
- As 33 pendências abertas estão em `pendencias` (`resolvida = 0`).
