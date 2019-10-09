#!/usr/bin/python3
#_*_ coding:utf-8 _*_
#Author:gaoyuxia
#Time:2019/10/9 11:27

class Foo:
    def __init__(self,start,stop):
        self.num=start
        self.stop=stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.num>=self.stop:
            raise StopIteration
        n=self.num
        self.num+=1
        return n

f=Foo(1,5)
#from collections import Iterable
from collections import Iterator
print(isinstance(f,Iterator))

for i in Foo(1,5):
    print(i)
