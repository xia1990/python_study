#!/usr/bin/python
#_*_ coding:utf-8 _*_

class Foo:
    @property
    def AAA(self):
        print('get的时候运行我啊')

    @AAA.setter
    def AAA(self,value):
        print('set的时候运行我啊')

    @AAA.deleter
    def AAA(self):
        print('delete的时候运行我啊')

f1=Foo()
f1.AAA
f1.AAA='aaa'
del f1.AAA