import sqlite3

banco = '/home/enrico/SQLiteStudio/bd/agenda.db'
con = sqlite3.connect(banco)
cur = con.cursor()
# cur.execute("CREATE TABLE contato(nome, endereco, telefone)")
#
#

res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchone())
