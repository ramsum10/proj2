import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_user = 'CREATE TABLE users VALUES(_id INTEGER PRIMARY KEY, username text, password text)'
cursor.execute(create_user)
create_items = 'CREATE TABLE items VALUES(name text PRIMARY KEY, price real)'
cursor.execute(create_items)
connection.commit()
connection.close()