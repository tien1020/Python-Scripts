#!/usr/bin/env python3
""" CS 335: Logical Agents """
__author__="Tien Nguyen"
# # -*- coding: utf-8 -*-

import sys
def file2list(filename):
    return open(filename).readlines()

a = file2list(sys.argv[1])

for line in a:
    dict = {}
    words=line.split(",")
    cnf = words[0]
       
    for word in words:
        if '=' in word:
            word = word.strip()
            print(word)
            dict[word[:-2]]=word[-1] == 'T'


    print("Dictionary: " , dict)
    clause_value = True
    for or_clause in cnf.split("^"):
        or_clause = or_clause.replace('(', '').replace(')','')
        print("OR CLAUSE " + or_clause)
        or_clause_value = False
        for component in or_clause.split('V'):
            component = component.strip()
            value = None
            if component[0] == '~':
                value = not dict[component[1:]]
            else:
                value = dict[component]
            print(component + " " + str(value))
            if value:
                or_clause_value = True
        print("value of " + or_clause + " is " + str(or_clause_value))
        if not or_clause_value:
            clause_value = False
    print("---Sentence value--- " + str(clause_value))