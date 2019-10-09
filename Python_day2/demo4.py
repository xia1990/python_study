#!/usr/bin/python
#_*_ coding:utf-8 _*_

__author__='Linhaifeng'

class Foo:
    def __init__(self,x):
        self.x=x
    def __getattr__(self, item):
        print("执行的是我")
    def __getattribute__(self, item):
        print("不管是否存在，我都会执行")
        raise AttributeError('哈哈')

f1=Foo(10)
f1.x
f1.xxxxxx