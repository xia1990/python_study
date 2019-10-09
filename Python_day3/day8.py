#!/usr/bin/python3
#_*_ coding:utf-8 _*_
#Author:gaoyuxia
#Time:2019/10/9 11:15

class Foo:
    __slots__ = 'x'

f1=Foo
f1.x=1
f1.y=2
print(f1.__slots__)

class Bar:
    __slots__ = ['x','y']

n=Bar()
n.x,n.y=1,2
n.z=3

