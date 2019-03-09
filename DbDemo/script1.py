import sqlite3


def create_table():
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, qty INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,qty,price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("insert into store Values('Wine Glass',8,10.5)")
    conn.commit()
    conn.close()