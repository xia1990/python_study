#!/usr/bin/python3
#_*_ coding:utf-8 _*_
#Author:gaoyuxia
#Time:2019/10/9 11:32

class Range:
    def __init__(self,n,stop,step):
        self.n=n
        self.stop=stop
        self.step=step

    def __next__(self):
        if self.n>=self.stop:
            print('超长了')
            raise StopIteration
        x=self.n
        self.n+=self.step
        return x

    def __iter__(self):
        return self

for i in Range(1,10,3):
    print(i)


