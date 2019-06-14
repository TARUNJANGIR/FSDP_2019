# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:52:03 2019

@author: HP
"""

# This program accepts a sequence of comma separated numbers from user 
   # and generates a list and tuple with those numbers.  
   list1 = []
while True:
    user_input = input("Enter values >")
    
    #append this entry to other data structure
    list1.append(user_input)
    
    if not user_input:
        break
list1.pop()
print('list:',list1)
tuple1 = tuple(list1)
print(tuple1)
