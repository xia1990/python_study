#!/usr/bin/python3
#_*_ coding:utf-8 _*_
#Author:gaoyuxia
#Time:2019/10/9 11:36


class Foo:
    "我是文档字符串"
    pass

class Bar(Foo):
    pass

print(Foo.__doc__)
#__doc__无法被子类继承
print(Bar.__doc__)
