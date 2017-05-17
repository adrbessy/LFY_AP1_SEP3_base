#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('LFY_base.db')

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     age INTERGER
)
""")
conn.commit()

users = []
users.append(("olivier", 30))
users.append(("jean-louis", 90))
cursor.executemany("""
INSERT INTO users(name, age) VALUES(?, ?)""", users)

cursor.execute("""SELECT id, name, age FROM users""")
for row in cursor:
    print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))
    
id = 2
cursor.execute("""SELECT id, name FROM users WHERE id=?""", (id,))
response = cursor.fetchone()  
print("response : ",response)
    
"""

########"To remove a table#########
cursor = conn.cursor()
cursor.execute("""
#DROP TABLE users
""")
conn.commit()

"""

#db.close()