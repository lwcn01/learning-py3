#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'new'

import os

def scan_file_recursion(path):
        for scan_dir in os.listdir(path):
            sub_path = os.path.join(path,scan_dir)
            if os.path.isdir(sub_path):
                scan_file_recursion(sub_path)
            else:
                print(scan_dir)

def scan_file_walk(path):
    global Count
    l = []
    Count = 0
    [l.append(list_dir[0]) for list_dir in list(os.walk(path))]
    list_dir = list(os.walk(path))
    for i in range(len(l)):
        print(l[i])                    #返回目录文件
        list_file = list_dir[i][-1]    #返回文件列表
        for j in range(len(list_file)):
            print(list_file[j])
        if len(list_file) != 0:
            Count = 1 + j
        else:
            Count = 0
        print('Count: %s files\n' %Count)

if __name__ == '__main__':
    path = input('路径...')
    path = str(path).strip().rstrip('\\')
    print('\n数字1：递归函数实现\n')
    print('数字2：OS.WALK实现\n')
    print('数字3：OS.SCAN实现\n')
    ID = int(input('输入数字：'))
    if ID == 1:
        scan_file_recursion(path)
    elif ID == 2:
        scan_file_walk(path)
    elif ID == 3:
        print('3.5.1Version+ Support')
    else:
        pass
