#!/usr/bin/env python
# -*- coding: UTF-8 –*-
''' 
 -------------------------------
 @Author:    KEN
 @File:      school_menu_v1.py
 @Date:      2018/1/12 10:54
 @Version:   2.0
 @Function:  多级菜单，可按年级>班级，显示该年级该班的学生姓名
 @Useage:    
 -------------------------------
 @Update log:

 -------------------------------
'''
import os
school = { '1年级':{
                    '1-1班':['小王','小明','小红']},
                '2年级':{
                    '2-1班':['马云','马化腾','李彦宏'],
                    '2-2班':['aaa','bbb','ccc']},
                '3年级':{
                    '3-1班':['小张','小李','小魔'],
                    '3-2班':['小于','小游','小菲'],
                    '3-3班':['Alice','Bob','John']}}

current_layer = school
last_layer = [current_layer]  #初始化上一次访问记录
while True:
    for i in current_layer:
        print(i)
    get_input = input('>>:')
    if get_input in current_layer:
        last_layer.append(current_layer)  #将当前访问的层作为最后一个元素写入list
        current_layer = current_layer[get_input]  #重新定义当前层，并进入循环开始打印
    if last_layer == []:
        print('已经在最顶层')
    if get_input == 'q':
        print('Bye')
        break
    if get_input == 'b':
        current_layer = last_layer[-1]   #重新定义当前层
        last_layer.pop()   #去除最后一个元素
