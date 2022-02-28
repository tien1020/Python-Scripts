# -*- coding: utf-8 -*-

List = [10, 5, 8, 7, -50, 20 ,-10, 2, 7, 9, 30, 50, 6, 8, 50, 4, 3, 50, -9, 0]

def most_times(List):
    counter = 0
    num = List[0]
    
    for i in List:
        curr = List.count(i)
        if(curr > counter):
            counter = curr
            num = i
    return num

print(most_times(List))