# -*- coding: utf-8 -*-
"""
Created on Mon May  3 23:15:17 2021

@author: Tien
"""
import random
def file2courses(filename):
    return open(filename).read()
a = file2courses("cscourses.txt")
course = a.split("-")
print(course)

def file2constraints(filename):
    return open(filename).readlines()
b = file2constraints("constraints.txt")
constraintList=[]
for line in b:
    constraint = line.strip().split("-")
    print("Constraints: " , constraint)
    constraintList.append(constraint)    
'''print("Constraints List: ", constraintList)'''
c1=""
c2=""
for i in constraintList:
    '''print("C: ", i)'''
    for z in i:
        c1 = i[0]
        c2 = i[1]
    print(c1, c2)
    """P1pick = random.choice(course)"""
    P1pick = "CS400"
    P2=course    
    for x2 in P2:
        if x2 == P1pick:
            P2.remove(x2)
        if P1pick == c1 and x2 == c2:
            P2.remove(x2)
        if P1pick == c2 and x2 == c1:
            P2.remove(x2)
    P2pick=random.choice(P2)
    P3=P2   
    for x3 in P3:
        if x3 == P2pick:
            P3.remove(x3)
        if P2pick == c1 and x3 == c2:
            P3.remove(x3)
        if P2pick == c2 and x3 == c1:
            P3.remove(x3)
    P3pick=random.choice(P3)
    P4=P3  
    print("P4:", P4)
    for x4 in P4:
        if x4 == P3pick:
            P4.remove(x4)
        if P3pick == c1 and x4 == c2:
            P4.remove(x3)
        if P3pick == c2 and x4 == c1:
            P4.remove(x3)
        P4pick=random.choice(P4)

print("P2", P2)
print("P3: ", P3)

print("P1 pick: ", P1pick)
print("P2 pick: ", P2pick)
print("P3 pick: ", P3pick)
       
    
        


"""P2pick = random.choice(P2)
print("P2 pick: ", P2pick)

P3=P2
P3 = [x for x in P3 if not x in P2pick]
print("P3: ", P3)
P3pick = random.choice(P3)
print("P3 pick: ", P3pick)

P4=P3
P4 = [x for x in P4 if not x in P3pick]
print("P4: ", P4)
P4pick = random.choice(P4)
print("P4 pick: ", P4pick)
"""