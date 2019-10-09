#!/usr/bin/python
#_*_ coding:utf-8 _*_

class Str:
    def __get__(self, instance, owner):
        print("Str调用")

    def __set__(self, instance, value):
        print("Str设置")

    def __delete__(self, instance):
        print("Str删除")

class Int:
    def __get__(self, instance, owner):
        print("Int调用")

    def __set__(self, instance, value):
        print("Int设置")

    def __delete__(self, instance):
        print("Int删除")

class People:
    name=Str()
    age=Int()
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=People('alex',18)
p1.name
p1.name='egon'
del p1.name

p1.age
p1.age=18
del p1.age

print(p1.__dict__)
print(People.__dict__)

print(type(p1)==People)
print(type(p1).__dict__==People.__dict__)