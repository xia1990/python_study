#!/usr/bin/puython
#_*_ coding:utf-8 _*_

class Lazyproperty:
    def __init__(self,func):
        self.func=func

    def __get__(self, instance, owner):
        print("这是我们自己定制的静态属性，r1.area扑鼻是要执行r1.area")
        if instance is None:
            return self
        return self.func(instance)

class Room:
    def __init__(self,name,width,length):
        self.name=name
        self.width=width
        self.length=length

    @Lazyproperty
    def area(self):
        return self.width*self.length

r1=Room('alex',1,1)
print(r1.area)