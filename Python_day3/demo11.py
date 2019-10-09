#!/usr/bin/python
#_*_ coding:utf-8 _*_

format_dict={
    'nat':'{obj.name}-{obj.addr}-{obj.type}',
    'tna':'{obj.type}:{obj.name}:{obj.addr}',
    'tan':'{obj.type}/{obj.addr}/{obj.name}',
}

class School:
    def __init__(self,name,addr,type):
        self.name=name
        self.addr=addr
        self.type=type

    def __repr__(self):
        return 'School(%s,%s)' % (self.name,self.addr)

    def __str__(self):
        return '(%s,%s)' % (self.name,self.addr)

    def __format__(self, format_spec):
        if not format_spec or format_spec not in format_dict:
            format_spec='nat'
        fmt=format_dict[format_spec]
        return fmt.format(obj=self)

s1=School('oldboy1','北京','私立')
print('from repr:',repr(s1))
print('from str:',str(s1))
