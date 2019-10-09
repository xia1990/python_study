#!/usr/bin/python
#_*_ coding:utf-8 _*_

class Foo:

    def __get__(self,instance,owner):
        print('触发get')

    def __set__(self, instance, value):
        print('触发set')

    def __delete__(self, instance):
        print("触发delete")

f1=Foo()
f1.name='egon'
f1.name
del f1.name
