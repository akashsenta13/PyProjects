# sqllite example
import sqlite3

def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, qty INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,qty,price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("insert into store Values(?,?,?)",(item,qty,price))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute('Select * from store;')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute('Delete from store where item=?',(item,))
    conn.commit()
    conn.close()

def update(item):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute('Update store SET item=? where item LIKE "Juice%" ',(item,))
    conn.commit()
    conn.close()

# run commands
create_table()
insert('Mirror glass',10,10)
print(view())
delete('Mirror glass')
print(view())
update('wine Glass')
print(view())