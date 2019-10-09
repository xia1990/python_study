#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import configparser

cf=configparser.ConfigParser()
cf.read("test1.ini")
cf.remove_option("kafa","user")


with open("test2.ini","w+") as f:
    cf.write(f)
