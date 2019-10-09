#!/usr/bin/python
#_*_ coding:utf-8 _*_
#Author:gaoyuxia
#Time:2019/10/9 14:43

class Foo(object):

    def __init__(self):
        self.name='alex'

    def func(self):
        return 'func'

obj=Foo()
print(getattr(obj,'name'))
print(obj.__doc__['name'])

