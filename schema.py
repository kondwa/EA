import sqlite3

db = sqlite3.connect("ea.db")
cursor = db.cursor()
cursor.execute(
"""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname VARCHAR(100),
    lastname VARCHAR(100),
    username VARCHAR(100),
    password VARCHAR(100),
    role VARCHAR(100)
);
"""
)
db.commit()
cursor.close()
db.close()
