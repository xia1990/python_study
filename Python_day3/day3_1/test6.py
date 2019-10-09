#!/usr/bin/python3
#_*_ coding:utf-8 _*_
#Author:gaoyuxia
#Time:2019/10/9 14:26

class WupeiqiException(Exception):

    def __init__(self,msg):
        self.message=msg

    def __str__(self):
        return self.message

try:
    raise WupeiqiException('我的异常')
except WupeiqiException as e:
    print(e)

