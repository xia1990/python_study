#!/usr/bin/python3
#_*_ coding:utf-8 _*_
#Author:gaoyuxia
#Time:2019/10/9 15:02

class People:

    def __init__(self,name,gender,age,fight):
        self.name=name
        self.gender=gender
        self.age=age
        self.fight=fight

    def grassland(self):
        """注释：草丛战斗，消耗200战斗力"""
        self.fight=self.fight - 200

    def returning(self):
        #print("name:%s,gender:%s,age:%d,fight:%s" % (self.name,self.gender,self.age,self.fight))
        return "name:",self.name,"gender:",self.gender,"age:",self.age,"fight:",self.fight

p1=People("苍井井","女",18,"初始战斗力1000")
p2=People("东尼木木","男",20,"初始战斗力1800")
p3=People("波多多","女",19,"初始战斗力2500")
print(p1.returning())
print(p2.__doc__)
print(p3.__doc__)

