#!/usr/bin/python
#_*_ coding:utf-8 _*_

class Foo:
    x=1
    def __init__(self,y):
        self.y=y
    def __getattr__(self, item):
        print("------> from getattr:你找的属性不存在")

    def __setattr__(self, key, value):
        print("-------> from setattr")

    def __delattr__(self, item):
        print("-------> from delattr")
        self.__dict__.pop(item)

f1=Foo(10)
print(f1.__dict__)
f1.z=3
print(f1.__dict__)
f1.__dict__['a']=3
del f1.a
print(f1.__dict__)

