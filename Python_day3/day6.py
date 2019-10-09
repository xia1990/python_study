#!/usr/bin/python
#_*_ coding:utf-8 _*_

class StaticMethod:
    def __init__(self,func):
        self.func=func

    def __get__(self, instance, owner):
        def feedback(*args,**kwargs):
            print('在这里可以增加功能啊。。。')
            return self.func(*args,**kwargs)
        return feedback

class People:
    @staticmethod
    def say_hi(x,y,z):
        print('--------->',x,y,z)

People.say_hi(1,2,3)
p1=People()
p1.say_hi(4,5,6)