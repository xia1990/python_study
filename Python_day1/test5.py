#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import configparser

config=configparser.ConfigParser()
config['DEFAULT']={'name':'gaoyuxia','age':22,'salary':3000}
config['bitbucket.org']={}
config['bitbucket.org']['user']='hg'
config['topsecret.server.com']={}
topsecret=config['topsecret.server.com']
topsecret['Host Port']='50022'
topsecret['ForwardX11']='no'
config['DEFAULT']['ForwardX11']='yes'

with open("example.ini",'w') as configfile:
    config.write(configfile)