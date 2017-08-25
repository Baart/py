import sqlite3

conn = sqlite3.connect("test.db")
c = conn.cursor()

# Create table
#c.execute('''CREATE TABLE stocks(date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

#conn.commit()

t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print (c.fetchone())

conn.close()
