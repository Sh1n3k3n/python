#!/usr/bin/env python
# -*- coding: UTF-8 –*-
''' 
 -------------------------------
 @Author:    KEN
 @File:      school_menu.py
 @Date:      2018/1/12 10:54
 @Version:   1.0
 @Function:  多级菜单，可按年级>班级，显示该年级该班的学生姓名
 @Useage:    
 -------------------------------
 @Update log:
 
 -------------------------------
'''
import os
dict_school = { 'grade1':{
                    'class1_1':['1_1_a','1_1_b','1_1_c']},
                'grade2':{
                    'class2_1':['2_1_a','2_1_b','2_1_c'],
                    'class2_2':['2_2_a','2_2_b','2_2_c']},
                'grade3':{
                    'class3_1':['3_1_a','3_1_b','3_1_c'],
                    'class3_2':['3_2_a','3_2_b','3_2_c'],
                    'class3_3':['3_3_a','3_3_b','3_3_c']}}

list_grade = [(num_grade,grade_name) for num_grade,grade_name in enumerate(dict_school)]
list_grade.append((len(list_grade),'exit')) #添加exit选项
break_flag = False
while True:
    if break_flag == True:
        break
    print('-----------------')
    print('欢迎使用学生查询系统')
    print('-----------------')

    for i in list_grade:
        for j in i:
            print(j,end=' ')
        print('')

    get_grade = input("Choose one grade: ")

    if not get_grade.isdecimal():
        print('Please input a number!')
    elif int(get_grade) >= len(list_grade):
        print('Number is too bigger!')
    elif int(get_grade) == len(list_grade)-1:
        print('Bye!')
        break
    else:
        choose_grade = list_grade[int(get_grade)][1]

        list_class = [(num_class,class_name) for num_class,class_name in enumerate(dict_school[choose_grade])]
        list_class.append((len(list_class),'return to choose grade'))
        list_class.append((len(list_class),'exit'))

        while True:
            for i in list_class:
                for j in i:
                    print(j,end=' ')
                print('')

            get_class= input('Choose one class: ')

            if not get_class.isdigit():
                print('Please input a number!')
            elif int(get_class) >= len(list_class):
                print('Number is too bigger!')
            elif int(get_class) == len(list_class)-2:
                break
            elif int(get_class) == len(list_class)-1:
                break_flag = True
                print('Bye!')
                break
            else:
                choose_class = list_class[int(get_class)][1]

                print('Students names are : %s' % dict_school[choose_grade][choose_class])
print('-----------------')