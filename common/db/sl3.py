import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()
sql = ''' create table atong(name TEXT, age NUMBER)'''
cur.execute(sql)
