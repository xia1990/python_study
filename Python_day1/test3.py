#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import configparser

cf=configparser.ConfigParser()
cf.add_section("mq")
cf.set("mq","user","laozhang")
cf.add_section("kafa")
cf.set("kafa","user","xiaoming")
with open("test1.ini","w") as f:
    cf.write(f)