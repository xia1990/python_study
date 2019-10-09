#!/usr/bin/python
#_*_ coding:utf-8 _*_

class A:
    pass

class B(A):
    pass

#B是A的子类
print(issubclass(B,A))
a1=A()
#a1是A的实例对象
print(isinstance(a1,A))