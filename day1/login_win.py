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
# print(work_path)
with open(work_path + r'\block.txt', 'r') as f:
    list_block = list(line.strip() for line in f)

with open(work_path + r'\user.txt', 'r') as f:
    dict_user = dict(line.strip().split(':') for line in f)

name = input("Please input username: ")
if name in list_block:
    print(f"User {name} has been blocked!")
elif name not in dict_user:
    print(f"User {name} is not existed!")
else:
    count = 3
    while count > 0:
        print(f"User {name} you have {count} times to login!")
        passwd = input("Input your password: ")
        if dict_user[name] == passwd:
            #print("Welcome {_name} !".format(_name=name))
            print(f"Welcome {name} !")
            break
        else:
            count -= 1
    else:
        print(f"User name [ {name} ] have been blocked!")
        with open(work_path + r'\block.txt', 'a') as f:
            f.write(name + '\n')
