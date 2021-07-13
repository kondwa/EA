import sqlite3
from hashlib import md5
db = sqlite3.connect('ea.db')
cursor = db.cursor()
firstname="Super"
lastname="User"
username='admin'
password='admin123'
role='admin'
cursor.execute("INSERT INTO users(firstname,lastname,username,password,role)VALUES('{firstname}','{lastname}','{username}','{password}','{role}')".format(
    firstname=firstname,lastname=lastname,username=username,password=md5(password.encode()).hexdigest(),role=role
))
db.commit()
cursor.close()
db.close()
