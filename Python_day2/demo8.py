#!/usr/bin/python
#_*_ coding:utf-8 _*_

class Foo:
    def func(self):
        print("我湖汉三又回来了")

f1=Foo()
f1.func()
print(dir(Foo.func))
print(hasattr(Foo.func,'__get__'))
print(hasattr(Foo.func,'__et__'))
print(hasattr(Foo.func,'__delete__'))

f1.func='这是实例属性啊'
print(f1.func)

del f1.func
f1.func()