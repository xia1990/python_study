#!/usr/bin/python
#_*_ coding:utf-8 _*_

class Str:

    def __get__(self, instance, owner):
        print("调用")

    def __set__(self, instance, value):
        print("设置")

    def __delete__(self, instance):
        print("删除")

class People:
    name=Str()
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=People("gaoyuxia",22)

#print(p1.__dict__)
p1.name="tom"
print(p1.name)
#print(p1.__dict__)