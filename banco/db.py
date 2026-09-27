"""365 Probabilidades — funções de apoio ao banco.

Uso no terminal, dentro do repositório:
    python3 banco/db.py colisao Lally          # busca por sobrenome
    python3 banco/db.py calendario             # o que falta em cada dia
    python3 banco/db.py ideia "Qual a chance de ..."   # nova entrada na fila
    python3 banco/db.py exportar               # grava banco/csv/*.csv

Uso no Python (notebook ou sessão com Claude):
    from banco.db import q, add
    q("select * from v_colisao where primeiro_autor='Cohen'")
    add('ideias', texto='...', rotacao='domingo_emocional')
"""
import sqlite3, sys, os, csv, datetime

DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), '365.db')
TABELAS = ['ideias', 'triagem', 'fontes', 'fontes_uso', 'dias', 'modelos',
           'validacoes', 'publicacoes', 'alertas', 'pendencias']


def conn():
    c = sqlite3.connect(DB)
    c.execute('PRAGMA foreign_keys = ON')
    c.row_factory = sqlite3.Row
    return c


def q(sql, *args):
    """Consulta; devolve lista de dicts."""
    with conn() as c:
        return [dict(r) for r in c.execute(sql, args).fetchall()]


def add(tabela, **campos):
    """Acrescenta uma linha. Devolve o id (ou o dia, em dias/publicacoes)."""
    assert tabela in TABELAS, tabela
    cols = ', '.join(campos)
    vals = ', '.join('?' for _ in campos)
    with conn() as c:
        cur = c.execute(f'INSERT INTO {tabela} ({cols}) VALUES ({vals})', tuple(campos.values()))
        return cur.lastrowid


def status(dia, novo):
    """Única atualização prevista: o status de um dia."""
    with conn() as c:
        c.execute('UPDATE dias SET status=? WHERE dia=?', (novo, dia))


def resolver(tabela, id_, campo='resolvido'):
    """Fecha uma validação ou pendência."""
    with conn() as c:
        c.execute(f"UPDATE {tabela} SET {campo}=1" + (", resolvida_em=date('now','localtime')" if tabela == 'pendencias' else '') + " WHERE id=?", (id_,))


def colisao(sobrenome):
    rows = q("SELECT * FROM v_colisao WHERE lower(primeiro_autor) LIKE lower(?)", f'%{sobrenome}%')
    alertas = q("SELECT tipo, texto FROM alertas WHERE ativo=1 AND lower(texto) LIKE lower(?)", f'%{sobrenome}%')
    return rows, alertas


def exportar(pasta=None):
    pasta = pasta or os.path.join(os.path.dirname(DB), 'csv')
    os.makedirs(pasta, exist_ok=True)
    with conn() as c:
        for t in TABELAS:
            rows = c.execute(f'SELECT * FROM {t} ORDER BY 1').fetchall()
            with open(os.path.join(pasta, f'{t}.csv'), 'w', newline='', encoding='utf8') as f:
                w = csv.writer(f)
                if rows:
                    w.writerow(rows[0].keys())
                    w.writerows([tuple(r) for r in rows])
                else:
                    w.writerow([d[1] for d in c.execute(f'PRAGMA table_info({t})')])
    return pasta


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'calendario'
    if cmd == 'colisao':
        rows, al = colisao(sys.argv[2])
        if not rows and not al:
            print('sem colisão')
        for r in rows:
            print(f"#{r['dia']:03d}  {r['primeiro_autor']} {r['ano']}  {r['papel']}  reuso_declarado={r['reuso_declarado']}  [{r['status']}]")
        for a in al:
            print(f"ALERTA ({a['tipo']}): {a['texto'][:200]}")
    elif cmd == 'calendario':
        for r in q('SELECT * FROM v_calendario'):
            print(f"#{r['dia']:03d}  {r['data_publicacao'] or '----------'}  {r['status']:12s}  bloqueios={r['bloqueios_abertos']}  pendências={r['pendencias_abertas']}  {(r['pergunta'] or '')[:60]}")
    elif cmd == 'ideia':
        i = add('ideias', texto=' '.join(sys.argv[2:]))
        print('ideia', i, 'registrada')
    elif cmd == 'exportar':
        print('CSVs em', exportar())
    else:
        print(__doc__)
