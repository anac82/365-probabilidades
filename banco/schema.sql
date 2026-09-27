-- 365 Probabilidades — esquema do banco (SQLite)
-- Uso: sqlite3 banco/365.db < banco/schema.sql
-- Regra: linhas entram, quase nunca mudam. Só status e "resolvido" se atualizam.

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS ideias (
  id          INTEGER PRIMARY KEY,
  criada_em   TEXT NOT NULL DEFAULT (date('now','localtime')),
  texto       TEXT NOT NULL,
  origem      TEXT NOT NULL DEFAULT 'ana' CHECK (origem IN ('ana','claude','leitor')),
  data_alvo   TEXT,
  rotacao     TEXT CHECK (rotacao IN ('sabado_leve','domingo_emocional','segunda_trabalho','livre')),
  status      TEXT NOT NULL DEFAULT 'nova' CHECK (status IN ('nova','triada','go','reserva','descartada'))
);

CREATE TABLE IF NOT EXISTS fontes (
  id              INTEGER PRIMARY KEY,
  primeiro_autor  TEXT NOT NULL,            -- sobrenome; a busca de colisão é aqui
  autores         TEXT NOT NULL,            -- lista completa, como será citada
  ano             INTEGER,
  titulo          TEXT,
  revista         TEXT,
  doi_url         TEXT,
  desenho         TEXT CHECK (desenho IN ('survey','rct','coorte','meta','experimento','registro','simulacao','revisao','conceito')),
  medida          TEXT CHECK (medida IN ('autorrelato','objetiva','codificacao','mista')),
  n               INTEGER,                  -- NULL = não localizado (declarar em n_nota)
  n_nota          TEXT,
  achado          TEXT,
  efeito          TEXT,                     -- d, r, HR, OR, %, como publicado
  ic95            TEXT,
  replicacao      TEXT CHECK (replicacao IN ('ok','disputada','falhou','retratado','nao_testada')),
  status          TEXT NOT NULL DEFAULT 'validada' CHECK (status IN ('validada','publicada','queimada','blacklist')),
  validada_em     TEXT,
  nota            TEXT
);
CREATE INDEX IF NOT EXISTS ix_fontes_autor ON fontes(primeiro_autor);

CREATE TABLE IF NOT EXISTS triagem (
  id                    INTEGER PRIMARY KEY,
  ideia_id              INTEGER REFERENCES ideias(id),
  data                  TEXT NOT NULL DEFAULT (date('now','localtime')),
  veredito              TEXT NOT NULL CHECK (veredito IN ('go','go_ressalva','no_go')),
  motivo                TEXT,
  fonte_central_id      INTEGER REFERENCES fontes(id),
  x080                  TEXT CHECK (x080 IN ('sim','nao','parcial')),
  x080_motivo           TEXT,
  colisoes              TEXT,
  forma                 TEXT,                -- magnitude, contraste, disputa, mecanismo, gradiente, ...
  modelo_proprio        TEXT,                -- camadas possíveis
  riscos                TEXT,
  perguntas_candidatas  TEXT
);

CREATE TABLE IF NOT EXISTS dias (
  dia               INTEGER PRIMARY KEY,    -- 106; dias na gaveta usam número provisório 900+
  data_publicacao   TEXT,
  pergunta          TEXT,
  capa              TEXT,
  tipo              TEXT,
  forma             TEXT,
  rotacao           TEXT,
  x080              TEXT CHECK (x080 IN ('sim','nao','parcial')),
  gancho            TEXT CHECK (gancho IN ('nenhum','universal','pessoal')),
  cordas            TEXT,                    -- "#014, #100"
  notebook          TEXT,
  pasta             TEXT,
  status            TEXT NOT NULL DEFAULT 'calibrado'
                    CHECK (status IN ('calibrado','notebook_ok','substack_v1','substack_ok','pronto','publicado','gaveta')),
  commit_msg        TEXT
);

CREATE TABLE IF NOT EXISTS fontes_uso (
  id               INTEGER PRIMARY KEY,
  fonte_id         INTEGER NOT NULL REFERENCES fontes(id),
  dia              INTEGER NOT NULL REFERENCES dias(dia),
  papel            TEXT NOT NULL CHECK (papel IN ('central','apoio','contraste','conceito','contrapeso')),
  x080_aplicado    INTEGER NOT NULL DEFAULT 0,
  reuso_declarado  INTEGER NOT NULL DEFAULT 0,
  nota             TEXT
);
CREATE INDEX IF NOT EXISTS ix_uso_dia ON fontes_uso(dia);

CREATE TABLE IF NOT EXISTS modelos (
  id         INTEGER PRIMARY KEY,
  dia        INTEGER NOT NULL REFERENCES dias(dia),
  camada     INTEGER NOT NULL DEFAULT 1,
  nome       TEXT,
  metodo     TEXT CHECK (metodo IN ('beta_jeffreys','posterior','monte_carlo','poder','tost','equacao','simulacao','traducao','forest','outro')),
  fonte_id   INTEGER REFERENCES fontes(id),
  entrada    TEXT,                           -- os números que alimentam a camada
  resultado  TEXT,
  ic_baixo   REAL,
  ic_alto    REAL,
  semente    INTEGER,
  grafico    TEXT,                           -- dia-NNN-grafico-NN-nome.png
  auditoria  TEXT                            -- desenho, família do teste, distribuição, comparações múltiplas
);

CREATE TABLE IF NOT EXISTS validacoes (
  id         INTEGER PRIMARY KEY,
  dia        INTEGER NOT NULL REFERENCES dias(dia),
  etapa      TEXT NOT NULL CHECK (etapa IN ('numeros','metodo','externa','overflow')),
  validador  TEXT NOT NULL,                  -- 'claude', 'ana', nome da segunda IA
  versao     INTEGER NOT NULL DEFAULT 1,
  data       TEXT NOT NULL DEFAULT (date('now','localtime')),
  item       INTEGER,
  gravidade  TEXT NOT NULL CHECK (gravidade IN ('bloqueia','ajusta','estilo')),
  trecho     TEXT,
  problema   TEXT,
  acao       TEXT,
  resolvido  INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS publicacoes (
  dia             INTEGER PRIMARY KEY REFERENCES dias(dia),
  data_real       TEXT NOT NULL,
  github_url      TEXT,
  substack_url    TEXT,
  instagram_url   TEXT,
  wayback_url     TEXT,
  dashboard_ok    INTEGER NOT NULL DEFAULT 0,
  commit_hash     TEXT
);

CREATE TABLE IF NOT EXISTS alertas (
  id          INTEGER PRIMARY KEY,
  criado_em   TEXT NOT NULL DEFAULT (date('now','localtime')),
  tipo        TEXT NOT NULL CHECK (tipo IN ('fonte','autor','tema','rigor','forma','voz','vocabulario','capa')),
  texto       TEXT NOT NULL,
  dia_origem  INTEGER,
  fonte_id    INTEGER REFERENCES fontes(id),
  ativo       INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS pendencias (
  id           INTEGER PRIMARY KEY,
  criada_em    TEXT NOT NULL DEFAULT (date('now','localtime')),
  dia          INTEGER,
  texto        TEXT NOT NULL,
  urgencia     TEXT CHECK (urgencia IN ('alta','media','baixa','antes_do_commit','dossie')),
  resolvida    INTEGER NOT NULL DEFAULT 0,
  resolvida_em TEXT
);

-- Consultas de rotina -------------------------------------------------------

-- Colisão: antes de propor tema
CREATE VIEW IF NOT EXISTS v_colisao AS
SELECT f.primeiro_autor, f.ano, f.revista, u.dia, u.papel, u.reuso_declarado, f.status
FROM fontes f JOIN fontes_uso u ON u.fonte_id = f.id
ORDER BY f.primeiro_autor, u.dia;

-- O que falta em cada dia do calendário
CREATE VIEW IF NOT EXISTS v_calendario AS
SELECT d.dia, d.data_publicacao, d.pergunta, d.status,
       (SELECT COUNT(*) FROM validacoes v WHERE v.dia = d.dia AND v.gravidade = 'bloqueia' AND v.resolvido = 0) AS bloqueios_abertos,
       (SELECT COUNT(*) FROM pendencias p WHERE p.dia = d.dia AND p.resolvida = 0) AS pendencias_abertas
FROM dias d WHERE d.status <> 'publicado' ORDER BY d.dia;

-- Cota de forma por bloco de dez
CREATE VIEW IF NOT EXISTS v_cota_forma AS
SELECT ((dia - 1) / 10) * 10 + 1 AS bloco_inicio, forma, COUNT(*) AS dias
FROM dias WHERE status = 'publicado' GROUP BY bloco_inicio, forma;
