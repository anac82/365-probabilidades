"""Carga inicial do 365.db a partir dos notebooks, do fontes_usadas.md e do dashboard."""
import json, re, glob, os, sqlite3, sys, html

REPO = '/home/claude/anac82/365-probabilidades'
DASH = '/home/claude/anac82/365-dashboard/index.html'
OUT  = '/home/claude/sistema-365/banco/365.db'
SCHEMA = '/home/claude/sistema-365/schema.sql'

if os.path.exists(OUT): os.remove(OUT)
db = sqlite3.connect(OUT)
db.executescript(open(SCHEMA).read())
cur = db.cursor()

# ---------------------------------------------------------------- dashboard
pub = {}
rows = re.split(r'<tr class="valid">', open(DASH, encoding='utf8').read())[1:]
for r in rows:
    dia = int(re.search(r'class="day"[^>]*>#(\d+)', r).group(1))
    if dia == 0: continue
    data = re.search(r'class="date"[^>]*>([^<]+)', r).group(1).strip()
    links = dict(re.findall(r'href="([^"]+)"[^>]*>(GitHub|Substack|Instagram|Archive)<', r))
    inv = {v: k for k, v in links.items()}
    pub[dia] = dict(data=data, github=inv.get('GitHub'), substack=inv.get('Substack'),
                    instagram=inv.get('Instagram'), wayback=inv.get('Archive'))
print('dashboard: dias publicados', len(pub), 'min', min(pub), 'max', max(pub))

# ---------------------------------------------------------------- fontes_usadas.md
FU = open(f'{REPO}/fontes_usadas.md', encoding='utf8').read()
forma = {}
for m in re.finditer(r'^### Dia #(\d+) - (.+?) - forma: (.+)$', FU, re.M):
    forma[int(m.group(1))] = (m.group(2).strip(), m.group(3).strip())
print('fontes_usadas: formas', len(forma))

# ---------------------------------------------------------------- notebooks
YEAR = re.compile(r'\b(1[89]\d\d|20[0-2]\d)\b')
NRE  = re.compile(r'\bN\s*(?:total\s*)?[=≈]\s*\*{0,2}\s*([\d][\d\.\,]*)')

def md_cells(nb):
    return [''.join(c['source']) for c in nb['cells'] if c['cell_type'] == 'markdown']
def code_cells(nb):
    return [''.join(c['source']) for c in nb['cells'] if c['cell_type'] == 'code']

def first_author(bullet):
    t = re.sub(r'[\*_`]', '', bullet).lstrip('- ').strip()
    t = re.sub(r'^(de |van der |van de |van |von )', '', t, flags=re.I)  # 'de Fleurian' -> Fleurian
    t = re.sub(r'^(U\.S\. |US )', '', t)
    m = re.match(r"([A-ZÁÉÍÓÚÂÊÔÃÕÇÖÜÄ][\w'\-ÁÉÍÓÚÂÊÔÃÕÇÖÜÄáéíóúâêôãõçöüä]+(?: [A-Z][\w'\-]+)?)", t)
    if not m: return None
    a = m.group(1)
    # institution names: keep first word only if it's a person-looking token followed by ',' or '&' or ' et'
    return a.split()[0] if re.match(r"[A-Z][a-zà-ÿ'\-]+$", a.split()[0]) else a

def parse_fontes(md):
    """returns (items, found): items = (raw, primeiro_autor, ano, n, revista) for every Fonte(s) block"""
    items = []; found = False
    for txt in md:
        for m in re.finditer(r'\*\*Fontes?(?: principal| central|s?)[^*\n]{0,40}\*\*:?', txt):
            found = True
            tail = txt[m.end():]
            same_line = tail.split('\n', 1)[0].strip()
            block = tail.split('\n', 1)[1] if '\n' in tail else ''
            cut = re.search(r'\n(#{2,}\s|\*\*(⚠️|Nota metodol|Nota sobre|O resto|Amostra)|---)', block)
            if cut: block = block[:cut.start()]
            buf = None
            if same_line and YEAR.search(same_line): items.append('- ' + same_line)
            for line in block.split('\n'):
                if re.match(r'\s*[-•]\s', line):
                    if buf: items.append(buf)
                    buf = line.strip()
                elif line.strip() and buf is not None:
                    buf += ' ' + line.strip()
                elif not line.strip() and buf:
                    items.append(buf); buf = None
            if buf: items.append(buf)
    out = []
    for it in items:
        if not YEAR.search(it) or re.match(r'\s*[-•]\s*\**(Contexto|Estudo \d|Experimento|Sobre |Nota|Também|Mais|Fora|Apoio|Contraforças|Reforços|Nuance)', it):
            if out: out[-1] = (out[-1][0] + ' | ' + re.sub(r'[\*]', '', it.lstrip('- ').strip()),) + out[-1][1:]
            continue
        raw = re.sub(r'\s+', ' ', it).strip()
        clean = re.sub(r'[\*_]', '', raw).lstrip('- ').strip()
        ano = int(YEAR.search(clean).group(1))
        nm = NRE.search(clean)
        n = None
        if nm:
            digits = re.sub(r'[\.\,]', '', nm.group(1))
            n = int(digits) if digits.isdigit() else None
        revista = None
        for cand in re.findall(r'\*{1,2}([^*]{4,90})\*{1,2}', raw):
            if re.search(r'Journal|Review|Science|Psycholog|Bulletin|Nature|PNAS|Economics|Medicine|JAMA|Lancet|Emotion|Memory|Cognition|Quarterly|Proceedings|Reports|Chaos|Frontiers|Behavior|Management|Marketing|Finance|Sociology|Physiology|Neuro|Pain|Perspectives|Advances|Studies|Circulation', cand) and not re.search(r'^(The |A |An |When |Why |How )', cand):
                revista = cand.strip(); break
        out.append((clean, first_author(raw), ano, n, revista))
    return out, found

files = sorted(glob.glob(f'{REPO}/modelos/**/*.ipynb', recursive=True))
by_dia = {}
for f in files:
    nb = json.load(open(f, encoding='utf8'))
    md = md_cells(nb); code = code_cells(nb)
    head = md[0] if md else ''
    mf = re.search(r'dia-?(\d{3})', os.path.basename(f)); mh = re.search(r'Dia #(\d+)', head)
    dia = int(mf.group(1)) if mf else int(mh.group(1))
    header_dia = int(mh.group(1)) if mh else None
    q = re.search(r'^## (.+)$', head, re.M)
    pergunta = q.group(1).strip() if q else None
    g = lambda k: (lambda mm: mm.group(1).strip() if mm else None)(re.search(r'\*\*'+k+r'[^*]*\*\*:?\s*(.+)', head))
    tipo = g('Tipo'); data = g('Data de publica'); decisao = g('Decisão analisada') or g('Decisao analisada')
    if data and not re.match(r'20\d\d-\d\d-\d\d', data): data = None
    alltext = '\n'.join(md + code)
    # x0.80
    x080 = None
    if re.search(r'aplica_fator_080\s*=\s*False', alltext) or re.search(r'(×|x)\s?0[,\.]80?[^\n]{0,60}não se aplica', alltext, re.I) or re.search(r'não se aplica[^\n]{0,80}(×|x)\s?0[,\.]80?', alltext, re.I):
        x080 = 'nao'
    elif re.search(r'fator_correcao\s*=\s*0\.8', alltext) and re.search(r'\*\s*fator_correcao', alltext):
        x080 = 'sim'
    graficos = re.findall(r"savefig\(\s*['\"]([^'\"]+\.png)", alltext)
    fontes, fblock = parse_fontes(md)
    by_dia.setdefault(dia, []).append(dict(file=os.path.relpath(f, REPO), pergunta=pergunta, tipo=tipo, data=data,
                                           decisao=decisao, x080=x080, graficos=graficos, fontes=fontes,
                                           code='\n'.join(code), has_block=fblock, header_dia=header_dia))

# choose the published notebook when a number has two
def pick(dia, cands):
    if len(cands) == 1: return cands[0], []
    link = pub.get(dia, {}).get('github', '') or ''
    for c in cands:
        if os.path.basename(c['file']) in link: return c, [x for x in cands if x is not c]
    # fall back: the one whose question matches fontes_usadas
    fu_q = re.search(r'### Dia #%03d[^\n]*\n\*\*([^*]+)\*\*' % dia, FU)
    if fu_q:
        for c in cands:
            if c['pergunta'] and c['pergunta'][:30] in fu_q.group(1): return c, [x for x in cands if x is not c]
    return cands[0], cands[1:]

metodo_kw = [('tost|equival', 'tost'), ('nct|poder|power|mde', 'poder'), ('jeffreys', 'beta_jeffreys'),
             ('stats\.beta\(', 'beta_jeffreys'), ('posterior', 'posterior'), ('choice|binomial\(|rng\.|random\.|np\.random', 'monte_carlo'),
             ('brentq|curve_fit|polyfit|np\.exp\(|logistic', 'equacao'), ('norm\.cdf\(.*sqrt\(2', 'traducao')]

fonte_ids = {}   # (autor, ano) -> id
n_uso = 0; gaveta = 901
for dia in sorted(by_dia):
    chosen, others = pick(dia, by_dia[dia])
    status = 'publicado' if dia in pub else 'notebook_ok'
    fu = forma.get(dia)
    cur.execute('INSERT OR REPLACE INTO dias(dia,data_publicacao,pergunta,tipo,forma,notebook,pasta,status) VALUES (?,?,?,?,?,?,?,?)',
                (dia, pub.get(dia, {}).get('data') or chosen['data'], chosen['pergunta'], chosen['tipo'],
                 fu[1] if fu else None, os.path.basename(chosen['file']), os.path.dirname(chosen['file']), status))
    if chosen['x080']:
        cur.execute('UPDATE dias SET x080=? WHERE dia=?', (chosen['x080'], dia))
    # fontes + uso
    for k, (raw, autor, ano, n, revista) in enumerate(chosen['fontes']):
        key = (autor or raw[:30], ano)
        if key in fonte_ids and cur.execute('select 1 from fontes_uso where fonte_id=? and dia=?', (fonte_ids[key], dia)).fetchone():
            key = (autor or raw[:30], ano, k)
        if key not in fonte_ids:
            cur.execute('INSERT INTO fontes(primeiro_autor,autores,ano,revista,n,status,validada_em,nota) VALUES (?,?,?,?,?,?,?,?)',
                        (autor or '?', raw[:400], ano, revista, n, 'publicada' if status == 'publicado' else 'validada',
                         chosen['data'], 'carga inicial: linha extraída do bloco Fontes do notebook; conferir campos'))
            fonte_ids[key] = cur.lastrowid
        fid = fonte_ids[key]
        reuso = 1 if re.search(r'já utilizad|reus|declarad', raw, re.I) else 0
        cur.execute('INSERT INTO fontes_uso(fonte_id,dia,papel,x080_aplicado,reuso_declarado) VALUES (?,?,?,?,?)',
                    (fid, dia, 'central' if k == 0 else 'apoio', 1 if chosen['x080'] == 'sim' else 0, reuso)); n_uso += 1
    if chosen['header_dia'] is not None and chosen['header_dia'] != dia:
        cur.execute("INSERT INTO pendencias(dia,texto,urgencia) VALUES (?,?,?)",
                    (dia, f"Cabeçalho do notebook {os.path.basename(chosen['file'])} diz 'Dia #{chosen['header_dia']:03d}', mas o arquivo e o dashboard são o #{dia:03d}. Corrigir o cabeçalho", 'dossie'))
    if not chosen['has_block']:
        cur.execute("INSERT INTO pendencias(dia,texto,urgencia) VALUES (?,?,?)",
                    (dia, f"Notebook {os.path.basename(chosen['file'])} sem bloco **Fontes:** estruturado; fontes não carregadas no banco", 'baixa'))
    # modelos: one row per graph, method guessed from the code before its savefig
    code = chosen['code']
    pos = 0
    for i, gname in enumerate(chosen['graficos'], 1):
        j = code.find(gname, pos)
        seg = code[max(0, j - 2500):j] if j >= 0 else ''
        met = 'outro'
        for pat, name in metodo_kw:
            if re.search(pat, seg, re.I): met = name; break
        cur.execute('INSERT INTO modelos(dia,camada,nome,metodo,grafico,auditoria) VALUES (?,?,?,?,?,?)',
                    (dia, i, gname.replace('.png', '').split('grafico-')[-1], met, gname, 'carga inicial: método inferido do código, conferir'))
        pos = j + 1 if j >= 0 else pos
    # duplicates -> gaveta
    for o in others:
        cur.execute('INSERT INTO dias(dia,pergunta,tipo,notebook,pasta,status,commit_msg) VALUES (?,?,?,?,?,?,?)',
                    (gaveta, o['pergunta'], o['tipo'], os.path.basename(o['file']), os.path.dirname(o['file']), 'gaveta',
                     f'número provisório; arquivo no repo com o mesmo número do dia #{dia:03d}'))
        cur.execute("INSERT INTO pendencias(dia,texto,urgencia) VALUES (?,?,?)",
                    (dia, f"Dois notebooks com o número #{dia:03d} no repositório: {os.path.basename(chosen['file'])} (publicado) e {os.path.basename(o['file'])} (gaveta, provisório #{gaveta}). Renomear ou mover o segundo", 'dossie'))
        gaveta += 1

# ---------------------------------------------------------------- publicacoes
for dia, p in pub.items():
    cur.execute('INSERT OR IGNORE INTO dias(dia,data_publicacao,status) VALUES (?,?,?)', (dia, p['data'], 'publicado'))
    cur.execute('INSERT INTO publicacoes(dia,data_real,github_url,substack_url,instagram_url,wayback_url,dashboard_ok) VALUES (?,?,?,?,?,?,1)',
                (dia, p['data'], p['github'], p['substack'], p['instagram'], p['wayback']))
# published days without notebook in repo
for dia in sorted(pub):
    if dia not in by_dia:
        cur.execute("INSERT INTO pendencias(dia,texto,urgencia) VALUES (?,?,?)", (dia, f'Dia #{dia:03d} está no dashboard mas não tem notebook no repositório', 'dossie'))

# ---------------------------------------------------------------- alertas
def add_alerta(tipo, texto, dia_origem=None):
    cur.execute('INSERT INTO alertas(tipo,texto,dia_origem,criado_em) VALUES (?,?,?,?)', (tipo, texto.strip(), dia_origem, '2026-09-25'))

# Parte 4: numbered permanent alerts
p4 = FU[FU.index('# PARTE 4'):FU.index('# PARTE 5')]
for m in re.finditer(r'^(\d+)\.\s+(.*?)(?=^\d+\.\s|\Z|^\*\*Acrescentados)', p4, re.M | re.S):
    txt = re.sub(r'\s+', ' ', re.sub(r'\*\*', '', m.group(2)))
    tipo = 'rigor'
    if re.search(r'vocabul|"número"|reticênc|verbo|palavra', txt, re.I): tipo = 'vocabulario'
    elif re.search(r'capa|manchete', txt, re.I): tipo = 'capa'
    elif re.search(r'forma|cota|bloco de dez|eixo', txt, re.I): tipo = 'forma'
    elif re.search(r'queimad|não usar|nunca citar|fora|não é fonte|retratad|lista negra|morto', txt, re.I): tipo = 'fonte'
    d = re.search(r'#(\d{3})', txt)
    add_alerta(tipo, f'[alerta {m.group(1)}] ' + txt, int(d.group(1)) if d else None)
# Parte 1: author alerts (## headings + paragraph)
p1 = FU[FU.index('# PARTE 1'):FU.index('# PARTE 2 ')]
for m in re.finditer(r'^## (.+?)\n(.*?)(?=^## |^# |\Z)', p1, re.M | re.S):
    body = re.sub(r'\s+', ' ', re.sub(r'\|[^\n]*', '', m.group(2))).strip()
    head = m.group(1).strip()
    tipo = 'tema' if 'Eixo' in head or 'Temas queimados' in head else 'autor'
    if 'Temas queimados' in head:
        for row in re.findall(r'^\| ([^|\n]+) \| ([^|\n]+) \|$', m.group(2), re.M):
            if row[0].strip() in ('Tema', '---'): continue
            motivo_q = re.sub(r'\*\*', '', row[1]).strip()
            add_alerta('tema', f'Tema queimado: {row[0].strip()}. {motivo_q}')
        continue
    add_alerta(tipo, f'{head}. {body[:700]}')
# Notas de janela: lições
nj = FU[FU.index('# NOTAS DE JANELA'):]
for m in re.finditer(r'^(\d)\.\s+\*\*(.+?)\*\*(.*?)(?=^\d\.\s|\Z|^\*\*Cota)', nj, re.M | re.S):
    txt = re.sub(r'\s+', ' ', m.group(2) + m.group(3))
    tipo = 'capa' if 'capa' in txt.lower() or 'legenda' in txt.lower() else ('forma' if 'overflow' in txt.lower() or 'poder' in txt.lower() else 'voz')
    add_alerta(tipo, '[lição de janela] ' + txt)

# ---------------------------------------------------------------- pendencias (tabela do md)
pp = FU[FU.index('# PENDÊNCIAS ABERTAS'):FU.index('# CALENDÁRIO')]
for m in re.finditer(r'^\| (\d+) \| (.*?) \| ([^|\n]+) \|$', pp, re.M | re.S):
    txt = re.sub(r'\s+', ' ', re.sub(r'\*\*', '', m.group(2)))
    resolved = 1 if '~~' in txt or 'RESOLVIDA' in txt or 'fechada' in m.group(3) else 0
    urg = m.group(3).strip().lower()
    urg = 'dossie' if 'dossi' in urg else 'antes_do_commit' if 'antes' in urg else 'alta' if 'alta' in urg else 'media' if 'média' in urg else 'baixa' if 'baixa' in urg else None
    d = re.search(r'#(\d{3})', txt)
    cur.execute('INSERT INTO pendencias(criada_em,dia,texto,urgencia,resolvida,resolvida_em) VALUES (?,?,?,?,?,?)',
                ('2026-09-25', int(d.group(1)) if d else None, f'[pendência {m.group(1)} do livro-caixa] ' + txt.replace('~~', ''), urg, resolved, '2026-09-25' if resolved else None))

# ---------------------------------------------------------------- calendário #099-#110 (status, rotação, ×0,80)
cal = FU[FU.index('# CALENDÁRIO'):FU.index('# RESERVAS')]
for m in re.finditer(r'^\| #(\d+) \| (\d\d/\d\d) \| (\w+) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \|$', cal, re.M):
    dia = int(m.group(1)); rot = m.group(3)
    rot = {'sábado': 'sabado_leve', 'domingo': 'domingo_emocional', 'segunda': 'segunda_trabalho'}.get(rot, 'livre')
    x = m.group(6).strip().lower(); x = 'sim' if x.startswith('sim') else 'nao' if x.startswith('não') else None
    cur.execute('INSERT OR IGNORE INTO dias(dia,data_publicacao,status) VALUES (?,?,?)', (dia, '2026-' + m.group(2)[3:] + '-' + m.group(2)[:2], 'calibrado'))
    cur.execute('UPDATE dias SET rotacao=?, x080=COALESCE(x080,?), capa=COALESCE(capa,?) WHERE dia=?', (rot, x, None, dia))
    if dia not in by_dia and dia not in pub:
        cur.execute('UPDATE dias SET pergunta=COALESCE(pergunta,?), commit_msg=? WHERE dia=?', (None, 'calendário 25/09: ' + m.group(4).strip() + ' · ' + m.group(7).strip(), dia))
# perguntas dos dias #107-#110 a partir da Parte 2
for m in re.finditer(r'^### Dia #(1(?:07|08|09|10)) - (\d{4}-\d\d-\d\d)[^\n]*\n\*\*(?:Pergunta:\*\* )?([^*\n]+)', FU, re.M):
    cur.execute('UPDATE dias SET pergunta=COALESCE(pergunta,?), data_publicacao=COALESCE(data_publicacao,?) WHERE dia=?', (m.group(3).strip(), m.group(2), int(m.group(1))))

# ---------------------------------------------------------------- reservas -> ideias + triagem + dias(gaveta / marcados)
res = FU[FU.index('# RESERVAS'):FU.index('# NOTAS DE JANELA')]
def table_rows(section):
    return [[c.strip() for c in r.strip().strip('|').split('|')] for r in re.findall(r'^\|.*\|$', section, re.M) if not re.match(r'^\|[\s\-|]+\|$', r.strip())]
sec = lambda a, b: res[res.index(a):res.index(b)] if b else res[res.index(a):]
pronto = table_rows(sec('## Com notebook pronto', '## Com dia marcado'))
marcado = table_rows(sec('## Com dia marcado', '## Validados sem dia'))
prateleira = table_rows(sec('## Validados sem dia', None))
def ideia(texto, status, motivo, veredito='go_ressalva', data_alvo=None):
    cur.execute('INSERT INTO ideias(criada_em,texto,origem,status,data_alvo) VALUES (?,?,?,?,?)', ('2026-09-25', re.sub(r'\*\*', '', texto), 'ana', status, data_alvo))
    iid = cur.lastrowid
    cur.execute('INSERT INTO triagem(ideia_id,data,veredito,motivo) VALUES (?,?,?,?)', (iid, '2026-09-25', veredito, re.sub(r'\*\*', '', motivo)))
    return iid
for r in pronto:
    if r[0] in ('Material', 'Tema') or len(r) < 3: continue
    if r[0] == 'Tema': continue
    ideia(f'{r[0]} | fontes: {r[1]}', 'reserva', r[2])
    nbm = re.search(r'`([^`]+\.ipynb)`', r[0])
    cur.execute('INSERT INTO dias(dia,pergunta,notebook,status,commit_msg) VALUES (?,?,?,?,?)',
                (gaveta, re.sub(r'\s*\(.*', '', re.sub(r'\*\*', '', r[0])).strip(), nbm.group(1) if nbm else None, 'gaveta', 'reserva com material pronto; renumerar ao usar. ' + re.sub(r'\*\*', '', r[2])[:300]))
    gaveta += 1
for r in marcado:
    if r[0] in ('Dia',) or len(r) < 4: continue
    dm = re.match(r'#(\d+)', r[0])
    if dm:
        d = int(dm.group(1))
        cur.execute('INSERT OR IGNORE INTO dias(dia,pergunta,status) VALUES (?,?,?)', (d, r[1], 'calibrado'))
        cur.execute('UPDATE dias SET commit_msg=? WHERE dia=? AND commit_msg IS NULL', (f'marcado: fontes {r[2]}. {r[3]}'[:500], d))
    else:
        ideia(f'{r[1]} | fontes: {r[2]}', 'reserva', f'{r[0]}: {r[3]}', data_alvo=r[0])
for r in prateleira:
    if r[0] in ('Tema',) or len(r) < 3: continue
    veredito = 'no_go' if re.search(r'descartad|recusad|não quer', r[2], re.I) else 'go_ressalva'
    status = 'descartada' if veredito == 'no_go' else 'reserva'
    ideia(f'{r[0]} | fontes: {r[1]}', status, r[2], veredito)

# ajustes conhecidos
cur.execute("UPDATE pendencias SET resolvida=1, resolvida_em='2026-09-27' WHERE texto LIKE '%Pergunta exata do #085%'")
cur.execute("UPDATE pendencias SET resolvida=1, resolvida_em='2026-09-27' WHERE texto LIKE '%#083 e do #085 ausentes%'")
cur.execute("INSERT INTO pendencias(dia,texto,urgencia) VALUES (83,'Os notebooks do #083 (dia083_rede_v2.ipynb) e do #085 (dia085_coincidencia.ipynb) estão no GitHub, mas fora do padrão de nome dia-NNN-tema.ipynb; renomear para o dossiê','dossie')")
# fontes queimadas
for a in ('Lally', 'MacLaren', 'Layton', 'Walker'):
    cur.execute("UPDATE fontes SET status='queimada' WHERE primeiro_autor=?", (a,))

db.commit()
for t in ['ideias', 'triagem', 'fontes', 'fontes_uso', 'dias', 'modelos', 'validacoes', 'publicacoes', 'alertas', 'pendencias']:
    print(f'{t:12s}', cur.execute(f'select count(*) from {t}').fetchone()[0])
