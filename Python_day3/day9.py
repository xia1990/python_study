#!/usr/bin/python3
#_*_ coding:utf-8 _*_
#Author:gaoyuxia
#Time:2019/10/9 11:21

class Foo:
    __slots__ = ['name','age']

f1=Foo()
f1.name='alex'
f1.age=18
print(f1.__slots__)

f2=Foo()
f2.name='egon'
f2.age=19
print(f2.__slots__)

print(Foo.__dict__)