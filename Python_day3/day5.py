#!/usr/bin/python
#_*_ coding:utf-8 _*_

class ClassMethod:
    def __init__(self,func):
        self.func=func

    def __get__(self, instance, owner):
        def feedback():
            print('在这里可以加功能啊...')
            return self.func(owner)
        return feedback

class People:
    name='linhaifeng'
    @classmethod
    def say_hi(cls):
        print('你好啊，帅哥%s' % cls.name)

People.say_hi()
p1=People()
p1.say_hi()
