#!/usr/bin/python
#_*_ coding:utf-8 _*_

class Foo:
    def __set__(self, instance, value):
        print("set")
    def __get__(self, instance, owner):
        print("get")

class Room:
    name=Foo()
    def __init__(self,name,width,length):
        self.name=name
        self.width=width
        self.length=length

r1=Room('厕所',1,1)
r1.name
r1.name='厨房'
