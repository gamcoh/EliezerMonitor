import sqlite3

conn = sqlite3.connect('database/eliezermonitor.db')
c = conn.cursor()

c.execute('''CREATE TABLE keys
             (date text, key text)''')

conn.commit()
conn.close()