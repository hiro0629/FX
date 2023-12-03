import sqlite3

dbname = 'term.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute("SELECT * FROM term")

for row in cur:
  print(row[2])
