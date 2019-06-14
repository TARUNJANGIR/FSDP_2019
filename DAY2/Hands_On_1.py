# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:51:39 2019

@author: HP
"""

# Create a list of number from 1 to 20 using range function. 
# Using the slicing concept print all the even and odd numbers from the list

our_list = list(range(21))
print (type(our_list))
print (our_list)
print ('even numbers>')
print (our_list[ ::2 ])
print('odd numvers>')
print (our_list[ 1::2 ])