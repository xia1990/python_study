#!/usr/bin/python3
#_*_ coding:utf-8 _*_
#Author:gaoyuxia
#Time:2019/10/14 15:50
#python操作mysql,案例一：插入数据

import pymysql

mydb=pymysql.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="runoob_db"
)

mycursor=mydb.cursor()
sql="insert into sites (name,url) value (%s,%s)"
val=("runoob","https://www.runoob.com")
mydb.commit()
print(mycursor.rowcount,"记录插入成功")

