#!/usr/bin/python3
#_*_ coding:utf-8 _*_
#Author:gaoyuxia
#Time:2019/10/14 16:03
#搜索指定数据

import pymysql

mydb=pymysql.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="runoob_db"
)
mycursor=mydb.cursor()
sql="select * from sites where name='baidu'"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for i in myresult:
    print(i)

print("========================")
sql="select * from sites where url like '%oo%'"
mycursor.execute(sql)

result2=mycursor.fetchall()
for i in result2:
    print(i)

print("========================")
sql="select * from sites where name=%s"
val=("baidu",)
mycursor.execute(sql,val)
result3=mycursor.fetchall()
for i in result3:
    print(i)
print("===========排序=============")
sql="select * from sites order by id"
mycursor.execute(sql)
result4=mycursor.fetchall()
for i in result4:
    print(i)

print("===========limit=============")
#只允许输出2条记录，limit限制输出记录条数
sql="select * from sites limit 2"
mycursor.execute(sql)
result5=mycursor.fetchall()
for i in result5:
    print(i)
print("===========offset=============")
#offset后面跟数字几，就代表从第几条开始输出
sql="select * from sites limit 2 offset 1"
mycursor.execute(sql)
result6=mycursor.fetchall()
for i in result6:
    print(i)
