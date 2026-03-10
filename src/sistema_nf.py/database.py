import sqlite3
import os

# 1. Descobre onde o arquivo database.py está (dentro de /src)
CAMINHO_ATUAL = os.path.dirname(os.path.abspath(__file__))

# 2. Sobe um nível para sair da /src e chegar na raiz do projeto
BASE_DIR = os.path.abspath(os.path.join(CAMINHO_ATUAL, ".."))

# 3. Cria o caminho final para a pasta /data/banco.db
DB_PATH = os.path.join(BASE_DIR, "data", "banco.db")

def conectar():
    # Isso garante que a pasta 'data' seja criada no seu Ubuntu
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return sqlite3.connect(DB_PATH)

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    # Mantive a tabela como você enviou, mas se quiser 
    # adicionar 'produtos' depois, é só incluir aqui!
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notas (
        numero INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente TEXT,
        valor REAL,
        usuario_criacao TEXT,
        data_criacao TEXT
    )
    """)

    conn.commit()
    conn.close()