#!/usr/bin/python
#_*_ coding:utf-8 _*_

class List(list):
    def append(self,p_object):
        if not isinstance(p_object,int):
            raise TypeError('must be int')
        super().append(p_object)

    @property
    def mid(self):
        '新增自己的属性'
        #长度除以2，并返回所得数的下标
        index=len(self)//2
        return self[index]

l=List([1,2,3,4])
print(l)
l.append(5)
print(l)
print(l.mid)
l.insert(0,-123)
print(l)
#clear清除整个列表
l.clear()
print(l)