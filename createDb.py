import sqlite3

db = sqlite3.connect('msgs.db')
db.execute("""CREATE TABLE IF NOT EXISTS tweet (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        msg TEXT  
       );""")
db.close()