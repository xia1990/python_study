#!/usr/bin/python3
#_*_ coding:utf-8 _*_
#Author:gaoyuxia
#Time:2019/10/9 11:49

class Foo:

    def __del__(self):
        print('执行我啦')

f1=Foo()
print('--------->')