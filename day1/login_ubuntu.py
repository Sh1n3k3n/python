#!/usr/bin/env python
# -*- coding: UTF-8 –*-
''' 
 -------------------------------
 @Author:    KEN
 @File:      login.py
 @Date:      2018/1/10 13:30
 @Version:   1.0
 @Function:  模拟用户登录，3次密码错误后锁定
 @Useage:    
 -------------------------------
 @Update log:
 
 change work_path "\ to "/"
 change print f'' to '%s' ways
 -------------------------------
'''

import os
work_path = os.path.split(os.path.realpath(__file__))[0]

with open(work_path + r'/block.txt', 'r') as f:
    list_block = list(line.strip() for line in f)

with open(work_path + r'/user.txt', 'r') as f:
    dict_user = dict(line.strip().split(':') for line in f)

name = input("Please input username: ")
if name in list_block:
    print("User %s has been blocked!" % name)
elif name not in dict_user:
    print("User %s is not existed!" % name)
else:
    count = 3
    while count > 0:
        print("User %s you have %d times to login!" % (name, count))
        passwd = input("Input your password: ")
        if dict_user[name] == passwd:
            #print("Welcome {_name} !".format(_name=name))
            print("Welcome %s !" % name)
            break
        else:
            count -= 1
    else:
        print('User name [ %s ] have been blocked!' % name)
        with open(work_path + r'/block.txt', 'a') as f:
            f.write(name + '\n')
