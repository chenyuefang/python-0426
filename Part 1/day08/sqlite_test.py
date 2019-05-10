#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2019/5/8 8:41
# @Author : mingfei.net@gmail.com
# @FileName : sqlite_test.py
# @GitHub : https://github.com/thu/python-0426

import sqlite3

connection = sqlite3.connect('test.db')

# print(connection)
# print(type(connection))

cursor = connection.cursor()

sql = """
    create table if not exists user(
        id int primary key, 
        name varchar(255)
    )
"""

cursor.execute(sql)

cursor.execute("insert into user values(1, 'Tom')")
cursor.execute("insert into user values(2, 'Jerry')")

print(cursor.rowcount)

# cursor.execute('select * from user where id = ?', (1,))
cursor.execute('select * from user')

values = cursor.fetchall()

print(values)

cursor.execute('update user set name = ? where id = ?', ('Spike', 2))

print(cursor.rowcount)

cursor.execute('select * from user where id = ?', (2,))

print(cursor.fetchall())

cursor.execute('delete from user where id = ?', (2,))

print(cursor.rowcount)

cursor.execute('select * from user')

print(cursor.fetchall())

cursor.close()
connection.close()

