#!/usr/bin/python
#_*_ coding:utf-8 _*_

class People:

    def __init__(self,name):
        self.name=name

    @property
    def name(self):
        print('get------->')
        return self.DouNiWan

    @name.setter
    def name(self,value):
        print('set------->')
        self.DouNiWan=value

    @name.deleter
    def name(self):
        print('delete-------->')
        del self.DouNiWan

p1=People('alex')
print(p1.name)
print(p1.name)
print(p1.name)
print(p1.__dict__)