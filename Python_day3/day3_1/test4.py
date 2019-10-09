#!/usr/bin/python3
#_*_ coding:utf-8 _*_
#Author:gaoyuxia
#Time:2019/10/9 14:13

class Foo:

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print('__call__')

obj=Foo()
obj()

