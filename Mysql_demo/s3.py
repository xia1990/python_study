#!/usr/bin/python3
#_*_ coding:utf-8 _*_
#Author:gaoyuxia
#Time:2019/10/14 15:59

import pymysql

mydb=pymysql.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="runoob_db"
)
mycursor=mydb.cursor()

mycursor.execute("select * from sites")
#获取所有记录
myresul=mycursor.fetchall()
for x in myresul:
    print(x)

mycursor.execute("select name,url from sites")
#获取一条数据
myresul2=mycursor.fetchone()
print(myresul2)
