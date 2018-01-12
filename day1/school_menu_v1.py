#!/usr/bin/env python
# -*- coding: UTF-8 –*-
''' 
 -------------------------------
 @Author:    KEN
 @File:      school_menu_v1.py
 @Date:      2018/1/12 10:54
 @Version:   1.0
 @Function:  多级菜单，可按年级>班级，显示该年级该班的学生姓名
 @Useage:    
 -------------------------------
 @Update log:
 
 -------------------------------
'''
import os
dict_school = { '1年级':{
                    '1-1班':['小王','小明','小红']},
                '2年级':{
                    '2-1班':['马云','马化腾','李彦宏'],
                    '2-2班':['aaa','bbb','ccc']},
                '3年级':{
                    '3-1班':['小张','小李','小魔'],
                    '3-2班':['小于','小游','小菲'],
                    '3-3班':['Alice','Bob','John']}}

list_grade = [(num_grade,grade_name) for num_grade,grade_name in enumerate(dict_school)]
list_grade.append((len(list_grade),'退出')) #添加exit选项
break_flag = False
while True:
    if break_flag == True:
        break
    print('-----------------')
    print('欢迎使用学级学生信息系统')
    print('-----------------')

    for i in list_grade:
        for j in i:
            print(j,end=' ')
        print('')

    get_grade = input("选择一个年级: ")

    if not get_grade.isdecimal():
        print('请输入数字!')
    elif int(get_grade) >= len(list_grade):
        print('数字太大!')
    elif int(get_grade) == len(list_grade)-1:
        print('再见!')
        break
    else:
        choose_grade = list_grade[int(get_grade)][1]

        list_class = [(num_class,class_name) for num_class,class_name in enumerate(dict_school[choose_grade])]
        list_class.append((len(list_class),'返回上一级'))
        list_class.append((len(list_class),'退出'))

        while True:
            for i in list_class:
                for j in i:
                    print(j,end=' ')
                print('')

            get_class= input('选择一个班级: ')

            if not get_class.isdigit():
                print('请输入数字!')
            elif int(get_class) >= len(list_class):
                print('数字太大!')
            elif int(get_class) == len(list_class)-2:
                break
            elif int(get_class) == len(list_class)-1:
                break_flag = True
                print('再见!')
                break
            else:
                choose_class = list_class[int(get_class)][1]

                print('该班学生有 : %s' % dict_school[choose_grade][choose_class])
print('-----------------')