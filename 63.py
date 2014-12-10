# -*-coding: utf-8 -*-

# easy_install mysql-connector-python
# easy_install MySQL-python

import mysql.connector

conn = mysql.connector.connect(user='testuser', password='ivmptest', database='wwtest', use_unicode=True)
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', '王玮'])
print cursor.rowcount
conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute('SELECT * FROM user where id = %s', ['1']) #['1'] !!!
values = cursor.fetchall()
print values
cursor.close()

conn.close()

# MySQL的SQL占位符是%s
# 通常我们在连接MySQL时传入use_unicode=True，让MySQL的DB-API始终返回Unicode
