#!/usr/bin/python3
#_*_ coding:utf-8 _*_
#Author:gaoyuxia
#Time:2019/10/9 14:31

class Foo(object):

    def __init__(self):
        self.name="wupeiqi"

    def func(self):
        return "func"

obj=Foo()
hasattr(obj,"name")
hasattr(obj,"func")

getattr(obj,"name")
getattr(obj,"func")

setattr(obj,"age",18)
setattr(obj,"show",lambda num:num+1)

#delattr(obj,"name")
#delattr(obj,"func")


