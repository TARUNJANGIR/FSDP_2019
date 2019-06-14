# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 18:21:35 2019

@author: HP
"""


# Ask the user for the name of a text file. 
#  Display the final line of that file.
#   Think of ways in which you can solve this problem, 
#    and how it might relate to your daily work with Python.

user_input = input ( "Enter your file name > ")
try:
    file = open("words.txt", "rt")
except:
    print("file cant open",file)
    exit
lines = file.readlines()
lines = lines[-1]
print (lines)