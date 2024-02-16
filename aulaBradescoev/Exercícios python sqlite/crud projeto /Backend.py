import sqlite3 as sql

class TransactinObject():
    database = "clientes.db"
    conn = None
    cur = None
    connected = False

    def connect(self):
        TransactinObject.conn = sql.connect(TransactinObject.database)
        TransactinObject.cur = TransactinObject.conn.cursor()
        TransactinObject.connected = True

    def execute(self, sql, parms = None):
        if TransactinObject.connected:
            if parms == None:
                TransactinObject.cur.execute(sql)
            else:
                TransactinObject.cur.execute(sql,parms)
            return True
        else:
            return False
    def fetchall(self):
        return TransactinObject.cur.fetchall()

    def persist(self):
        if TransactinObject.connected:
            TransactinObject.conn.commit()
            return True
        else:
            return False
    def disconnect(self):
        if TransactinObject.connected:
            TransactinObject.conn.close()
            TransactinObject.connected=False
            return True
        else:
            return False
def initDB():
    trans = TransactinObject()
    trans.connect()

    trans.execute('CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)')
    trans.persist()
    trans.disconnect()

def insert(nome, sobrenome, email, cpf):
    trans = TransactinObject()
    trans.connect()
    trans.execute('INSERT INTO clientes VALUES (NULL, ?,?,?,?)',(nome,sobrenome,email,cpf))
    trans.persist()
    trans.disconnect()

def view():
    trans = TransactinObject()
    trans.connect()
    trans.execute('SELECT * FROM clientes')
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def search(nome='', sobrenome='', email='',cpf=''):
    trans = TransactinObject()
    trans.connect()
    trans.execute('SELECT * FROM clientes WEHRE nome=? or sobrenome=? or email=? or cpf=?',(nome,sobrenome,email,cpf))
    rows=trans.fetchall()
    trans.disconnect()
    return rows

def delete(id):
    trans= TransactinObject()
    trans.connect()
    trans.execute('DELETE FROM clientes WHERE id = ?',(id,))
    trans.persist()
    trans.disconnect()

def update(id,nome,sobrenome,email,cpf):
    trans = TransactinObject
    trans.connect()
    trans.execute('UPDATE cliente SET nome=? , sobrenome=?, email=? cpf=? WHERE id = ?',(nome, sobrenome,email,cpf,id))
    trans.persist()
    trans.disconnect()

initDB()



