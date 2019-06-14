# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:36:32 2019

@author: HP
"""

#You are given a string N. 
 #   Your task is to verify that N is a floating point number.
  #  Take Input From User
  
user_input = input('enter a string')
import re
if (re.findall(r'^[+-]?\d+\.\d+',user_input)):
    print (user_input)
    print('true')
else:
    print (user_input)
    print ('false')