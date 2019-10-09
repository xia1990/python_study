#!/usr/bin/python
#_*_ coding:utf-8 _*_

import time

class FileHandle:
    def __init__(self,filename,mode='r',encoding='utf-8'):
        self.file=open(filename,mode,encoding=encoding)
    def write(self,line):
        t=time.strftime('%Y-%m-%d %T')
        self.file.write('%s %s' % (t,line))
    def __getattr__(self, item):
        return getattr(self.file,item)

f1=FileHandle('b.txt','w+')
f1.write('你好啊\n')
f1.write('我是gaoyuxia,学习python第二天\n')
f1.seek(0)
print(f1.read())
f1.close()