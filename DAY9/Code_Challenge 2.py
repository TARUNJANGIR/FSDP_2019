# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:46:17 2019

@author: HP
"""
   """ Code Challenge 2
  
      Perform similar steps as in the above code challenge but store the contents in 
            an online mongo atlas database.
"""


import pymongo
client = pymongo.MongoClient("mongodb://yourusername:dbpassword@cluster0-shard-00-00-tdcf5.mongodb.net:27017,cluster0-shard-00-01-tdcf5.mongodb.net:27017,cluster0-shard-00-02-tdcf5.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
mydb = client.db_university

def add_university(Student_Name, Student_Age, Student_Roll_no, Student_Branch):
    mydb.students,insert_one(
        {
       "Student_Name": Student_Name,
      "Student_Age": Student_Age,
      "Student_Roll_no": Student_Roll_no,
      "Student_Branch": Student_Branch
        })
    return "student asses successfully"
def fetch_all_STUDENT():
    user = mudb.STUDENT.find
    for i in user:
        print(i)
        
        
        
add_university('TARUN JANGIR',20,19,'ECE')
add_university('REENA KATARIYA',19,1,'CS')
add_university('DEEPAK SWAMI',19,5,'ECE')
add_university('TARUN MANDANI',16,20,'ECE')
add_university('RISHIPAL YADAV',20,29,'CS')
add_university('RITESH JANGIR',24,19,'CS')
add_university('CHANDRA SHEKHER',21,26,'CS')
add_university('SHARIKA YADAV',20,16,'CS')
add_university('NEHA YADAV',19,2,'CS')
add_university('MONIKA',18,3,'ECE')

fetch_all_students()




