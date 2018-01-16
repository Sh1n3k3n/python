#!/usr/bin/env python
# -*- coding: UTF-8 –*-
''' 
 -------------------------------
 @Author:    KEN
 @File:      test.py
 @Date:      2018/1/11 17:49
 @Version:   1.0
 @Function:  练习 list dict tuple
 @Useage:    
 -------------------------------
 @Update log:
 
 -------------------------------
'''

menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

current_layer = menu  # 当前层
last_layers = [menu]  # 上一层
while True:
    for key in current_layer:  # 打印第一层菜单
        print(key)
    choice = input(">>:").strip()  # 选择第二层菜单
    if choice in current_layer:
        last_layers.append(current_layer)  # 进入下一层菜单前，把当前层菜单加入上一次菜单中
        current_layer = current_layer[choice]  # 当前层菜单被重新定义，进入循环打印下一层菜单
    if choice == 0:  # 选择菜单层为空，结束本次循环
        continue
    if choice == "q":  # 选择菜单层为“q”，结束本层循环
        break
    if choice == "b":  # 选择菜单层为“b”，返回上一层菜单
        current_layer = last_layers[-1]  # 返回上一层菜单前，当前层被重新定义
        last_layers.pop()  # 删除最后一次进入下一层菜单所加入的上一层列表数据
print("程序结束！")