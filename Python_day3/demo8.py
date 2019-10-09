#!/usr/bin/python
#_*_ coding:utf-8 _*_

class Foo:
    def setAAA(self):
        print('set的时候运行我啊。')

    def getAAA(self):
        print('get的时候运行我啊。')

    def deleteAAA(self):
        print('delete的时候运行我啊')

    AAA=property(setAAA,getAAA,deleteAAA)

f1=Foo()
f1.AAA
f1.AAA='aaa'
del f1.AAA