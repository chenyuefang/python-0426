import mysql.connector

connection = mysql.connector.connect(user='root', password='system')

connection.autocommit = True

cursor = connection.cursor()


cursor.execute('select * from db_python.user')

records = cursor.fetchall()

# print(records)

# for record in records:
#     print(record)

cursor.execute("""
    select * from db_python.book
    where id > 10 
    order by id desc 
    limit 0, 2
""")

rows = cursor.fetchall()

# for row in rows:
#     print(row)


# cursor.execute("""
#     update db_python.book
#     set title = 'JavaScript'
#     where title = 'JavaScript 高级编程'
# """)

# connection.commit()

# cursor.execute("""
#     select u.email , b.title
#     from db_python.user u join db_python.book b
#     on u.id = b.userId
# """)
#
# values = cursor.fetchall()
#
# for value in values:
#     print(value)


# cursor.execute('alter table db_python.book drop foreign key book_fk_userId')

# cursor.execute("""
#     alter table db_python.book
#     add constraint
#     book_fk_userId
#     foreign key (userId)
#     references db_python.user(id)
#     on delete set null
# """)

# cursor.execute("""
#     delete from db_python.user
#     where id = 1
# """)

cursor.execute('drop table db_python.book')
cursor.execute('drop table db_python.user')

