import sqlite3
from hashlib import md5
def dbconnect():
    return sqlite3.connect('ea.db')

def signin(username,password):
    db = dbconnect()
    cursor = db.cursor()
    cursor.execute("SELECT firstname,lastname,username,role FROM users WHERE password='{password}'".format(password=md5(password.encode()).hexdigest()))
    user = cursor.fetchone()
    cursor.close()
    db.close()
    return user
def signup(firstname,lastname,username,password,role='user'):
    db = dbconnect()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users(firstname,lastname,username,password,role)VALUES('{firstname}','{lastname}','{username}','{password}','{role}')".format(
        firstname=firstname,lastname=lastname,username=username,password=md5(password.encode()).hexdigest(),role=role
    ))
    db.commit()
    cursor.close()
    db.close()

# user = signin('mile','milepass')
# if user:
#    print(user)
#else:
#    print('user not available.')
