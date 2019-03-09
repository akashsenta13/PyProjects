# PostgreSQL example
# post : 5432   
# User : user_1
# pwd : user123

import psycopg2 as pg

def create_table():
    conn = pg.connect("dbname='database1' user='user_1' password='user123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, qty INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,qty,price):
    conn = pg.connect("dbname='database1' user='user_1' password='user123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("insert into store Values(%s,%s,%s)",(item,qty,price))
    conn.commit()
    conn.close()

def view():
    conn = pg.connect("dbname='database1' user='user_1' password='user123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute('Select * from store;')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete(item):
    conn = pg.connect("dbname='database1' user='user_1' password='user123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute('Delete from store where item=%s',(item,))
    conn.commit()
    conn.close()

def update(qty,price,item):
    conn = pg.connect("dbname='database1' user='user_1' password='user123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute('Update store SET qty=%s, price=%s where item=%s',(qty,price,item))
    conn.commit()
    conn.close()

# run commands
create_table()
insert('Water glass',10,10)
#print(view())
#delete('Mirror glass')
print(view())
update(20,15.5,'Water glass')
print(view())