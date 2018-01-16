#!/usr/bin/env python
# -*- coding: UTF-8 –*-
''' 
 -------------------------------
 @Author:    KEN
 @File:      1.py
 @Date:      2018/1/16 14:48
 @Version:   1.0
 @Function:  
 @Useage:
 -------------------------------
 @Update log:
 
 -------------------------------
'''
import math

def quadratic(a,b,c):
    print('%dx**2 + %dx + %d = 0' % (a,b,c))
    print('---------------')
    tmp = b**2-4*a*c
    if a ==0:
        x1 = (0-c)/b
        x2 = x1
        return x1,x2
    elif tmp < 0:
        print("无解")
        return
    else:
        x1 = (0-b + math.sqrt(tmp))/2/a
        x2 = (0-b - math.sqrt(tmp))/2/a
        return x1,x2
print("一元二次方程求解 ax*x+bx+c=0")
answer = quadratic(int(input('a = ')), int(input('b = ')), int(input('c = ')))
if answer != None:
    print('x1=%.2f x2=%.2f' % (answer[0], answer[1]))




