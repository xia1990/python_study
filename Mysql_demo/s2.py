#!/usr/bin/python3
#_*_ coding:utf-8 _*_
#Author:gaoyuxia
#Time:2019/10/14 15:54

import pymysql

mydb=pymysql.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="runoob_db"
)
mycursor=mydb.cursor()

sql="insert into sites (name,url) values (%s,%s)"
val=[
    ('google',"www.google.com"),
    ('baidu',"www.baidu.com"),
    ('taobao',"www.taobao.com")
]

#一次性插入多条记录
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"条记录")
