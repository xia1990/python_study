#!/usr/bin/python3
#_*_ coding:utf-8 _*_
#Author:gaoyuxia
#Time:2019/10/9 14:16

s1 = 'hello'
try:
    int(s1)
except IndexError as e1:
    print("e1:",e1)
except KeyError as e2:
    print("e2:",e2)
except ValueError as e3:
    print("e3:",e3)

