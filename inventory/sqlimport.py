import  sqlite3
database = "clientes.db"

conn = sqlite3.connect(database)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS cliente (id INTERGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email, TEXT, cpf TEXT)")
conn.commit()
con.close()