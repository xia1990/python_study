#!/usr/bin/python
#_*_ coding:utf-8 _*_

class List(list):
    def __init__(self,item,tag=False):
        super().__init__(item)
        self.tag=tag
    def append(self,p_object):
        if not isinstance(p_object,str):
            raise TypeError
        super().append(p_object)
    def clear(self):
        if not self.tag:
            raise PermissionError
        super().clear()

l=List([1,2,3],False)
print(l)
print(l.tag)

l.append('saf')
print(l)

l.tag=True
l.clear()

