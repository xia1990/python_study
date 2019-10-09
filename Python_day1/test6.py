#！/usr/bin/python
#_*_ coding:utf-8 _*_

class OldboyStudent:
    school="oldboy"
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def learn(self):
        print('%s is learning' % self.name)

    def eat(self):
        print('%s is eating' % self.name)

    def sleep(self):
        print('%s is sleeping' % self.name)

s1=OldboyStudent("tom","22","男")
print(s1)
print(s1.__dict__)