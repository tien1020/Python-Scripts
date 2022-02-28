# -*- coding: utf-8 -*-
from collections import Counter
 
def file2list(filename):
    return open(filename).read()

a = file2list("healthyeating.txt")
b = a.split(" ")

#Words:
words_counter = len(b)

#Lines:
lines = a.split("\n")

line_counter = 0

for i in lines:
    if i:
        line_counter +=1

#Characters:

characters_counter = len(a)

      
#Unique words:     

uniqueWords= set()
for i in lines:
    uniqueWords |= set(i.split())
    
uniqueWords_counter = len(uniqueWords)

#Print:
    
print("lines:", line_counter, ",", "unique:", uniqueWords_counter, ",", "words:", words_counter, ",", "chars:", characters_counter)


    
def count_words(l_words):
    return Counter(l_words)

wc = count_words(b)

print('Most frequent word:',wc.most_common(1))
print('Least frequent word:',wc.most_common()[-1])