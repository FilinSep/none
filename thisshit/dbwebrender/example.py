from dbwebrender import render
import sqlite3
import random

db = sqlite3.connect("database.db")
cur = db.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS workers (name TEXT, job TEXT, salary INTEGER)")
for i in range(3): cur.execute(f"INSERT INTO workers VALUES(\"worker{i}\", \"Python Programmer\", {random.randint(1, 100)})") 
db.commit()

render("database.db", "workers")