#!/usr/bin/env python
#_*_ coding:utf-8 _*_

for i in range(1,10):
    for j in range(1,i+1):
        print('%s*%s=%s' %(i,j,i*j),end=' ')
    print()
