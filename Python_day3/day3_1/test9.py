#!/usr/bin/python3
#_*_ coding:utf-8 _*_
#Author:gaoyuxia
#Time:2019/10/9 14:55

class Foo(object):

    staticField="old boy"

    def __init__(self):
        self.name="wupeiqi"

    #类的普通方法，必须要使用类的实例调用
    def func(self):
        return "func"

    #类的静态方法，可以使用类名.方法名来进行调用
    @staticmethod
    def bar():
        return "bar"

print(getattr(Foo,"staticField"))
#print(getattr(Foo,"func"))
#print(getattr(Foo,"bar"))
print(Foo.bar())
#类实例
f1=Foo()
print(f1.func())





