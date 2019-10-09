#!/usr/bin/python
#_*_ coding:utf-8 _*_

class Room:

    def __init__(self,name,width,length):
        self.name=name
        self.width=width
        self.length=length

    @property
    def area(self):
        return self.width*self.length

r1=Room('tom',10,20)
print(r1.__dict__)
print(r1.area)