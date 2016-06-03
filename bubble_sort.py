#!/usr/bin/env python
# -*- coding: utf-8 -*-
#an example
import os
def bubblesort(numbers):
    for j in range(len(numbers)-1,-1,-1):
        for i in range(j):
            if numbers[i]<numbers[i+1]:
                numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
            print(i,j)
            print(tuple(numbers))
    os.system('pause')

if __name__ == '__main__':
    numbers = (1,2,3,4,5,6,7,8,9)
    numbers = list(numbers)
    bubblesort(numbers)
