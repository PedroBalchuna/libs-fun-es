import sqlite3

def criar_banco(nome_arquivo = 'meu_banco.db'):

    '''
    Criar (ou conecta) a um banco de dados SQLite e garante que a tabela 'arquivos' exista.
    Retorna a conexão e o cursor
    '''
    conexao = sqlite3.connect(nome_arquivo)
    cursor = conexao.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS arquivos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        caminho TEXT NOT NULL,
        tamanho REAL NOT NULL,
        criacao DATE NOT NULL
    )
    ''')

    conexao.commit()

    return conexao, cursor