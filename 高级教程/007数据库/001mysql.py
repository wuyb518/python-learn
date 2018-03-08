#!/usr/bin/env python
# _*_ coding:UTF-8_*_

import MySQLdb
conn=MySQLdb.connect(user='test',passwd='test123',host='localhost')
cursor=conn.cursor()
cursor.execute('create database test;')
# cursor.commit() MySqldb开启了自动提交所有不用手动commit
cursor.execute('use test;')
cursor.execute('create table friend(name nvarchar(50),age int);')
cursor.execute("insert into friend values('wuyb',28);")
print '受影响行数:%d' % cursor.rowcount
cursor.execute("insert into friend values('yy',27);")
print '受影响行数:%d' % cursor.rowcount
cursor.execute("update friend set age=29 where name='wuyb';")
print '受影响行数:%d' % cursor.rowcount
cursor.execute("select name,age from friend;")
for data in cursor.fetchall():
    print '%s, %d' % data
cursor.execute("delete from friend where name='wuyb';")
print '删除了%d行' % cursor.rowcount
cursor.execute('drop table friend')
cursor.execute('drop database test')
cursor.close()
conn.commit()
conn.close()
