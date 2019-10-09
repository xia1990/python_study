#!/usr/bin/python
#_*_ coding:utf-8 _*_

class Str:
    def __init__(self,name):
        self.name=name

    def __get__(self, instance, owner):
        print("get",instance,owner)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print("set",instance,value)
        instance.__dict__[self.name]=value

    def __delete__(self, instance):
        print("delete",instance)
        instance.__dict__pop(self.name)

class People:
    name=Str('name')
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

p1=People('egon',18,3231.3)
print(p1.__dict__)
p1.name


