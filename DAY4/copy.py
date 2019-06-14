# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:14:12 2019

@author: HP
"""
#   Make a program that create a copy of a file  

with open('words.txt',mode = 'rt') as file :
    with open('wordscp:.txt', mode = 'wt') as file2 :
        for line in file:
          file2.write(line)
