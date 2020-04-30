import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = 'CREATE TABLE users (id INTEGER PRIMARY KEY, username text, password text)'
cursor.execute(create_table)

create_item = 'CREATE TABLE items (name text, price real)'
cursor.execute(create_item)

user = ('John', 'Password1')
insert_query = 'INSERT INTO users VALUES (NULL, ?, ?)'
cursor.execute(insert_query, user)

users = [
    ('Rushikesh', 'Password2'),
    ('Sidhant', 'Password3')
]

cursor.executemany(insert_query, users)

select_query = 'SELECT * FROM users'

for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()