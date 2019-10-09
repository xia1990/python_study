#!/usr/bin/python3
#_*_ coding:utf-8 _*_
#Author:gaoyuxia
#Time:2019/10/9 14:08

class Open:
    def __init__(self,filepath,mode='r',encoding='utf-8'):
        self.filepath=filepath
        self.mode=mode
        self.encoding=encoding

    def __enter__(self):
        self.f=open(self.filepath,mode=self.mode,encoding=self.encoding)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
        return True

    def __getattr__(self, item):
        return getattr(self.f,item)

with open('a.txt','w') as f:
    print(f)
    f.write('aaaaaa')
    f.wasdf

