# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:41:42 2019

@author: HP
"""

#  You are given N email addresses. 
 #   Your task is to print a list containing only valid email addresses in alphabetical order.
  #  Valid email addresses must follow these rules:

   # It must have the username@websitename.extension format type.
    #The username can only contain letters, digits, dashes and underscores.
    #The website name can only have letters and digits.
    #The minimum length is 2 and maximum length of the extension is 4.
     """lara@hackerrank.com
    brian-23@hackerrank.com
    britts_54@hackerrank.com"""
import re    
user_input = input('enter a email').split(",")
for i in user_input:
    if re.findall(r'\w+\_?\w+?\@\w+\.\w+',i):
        print (user_input)
    else:
        print ('invalid email')
