# -*- coding: utf-8 -*-
"""
Created on Sat May  1 23:49:36 2021

@author: Tien
"""

courses =["CS200","CS201","CS400","CS420"]

c1 = [courses[1], courses[2]]
c2 = [courses[0],courses[3]]
c3 = [courses[2],courses[3]]
c4 = [courses[0],courses[1]]

schedule=[]
value= bool
for x in courses:
    schedule.append(x)
    for y in schedule:
        if y in c1:
            schedule.remove(y)
print(schedule)