#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
""" Beyond Search program """
__author__="Tien Nguyen"
print ("Beyond Search Homework")

import random

print('Enter an integer:')
n = input()
n = int(n)

def compute_h(list):
    h = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if (list[i] == list[j]) or (abs(list[j] - list[i]) == j - i):
                h += 1
    return h

# list: board , search_cost: the search cost up to now
# return (True if solved, the search cost)
def hillclimb_helper(list, search_cost):
    current_h = compute_h(list)
    # if the board is solved, return true and the search_cost
    if current_h == 0:
        return (True, search_cost)
    # choose the new board configuration that yields the smallest h
    best_h = current_h
    best_list = list
    # try to move queen at row i
    for i in range(8):
        for col in range(8):
            if col == list[i]:
                continue
            new_list = list.copy()
            new_list[i] = col
            new_h = compute_h(new_list)
            search_cost += 1
            if new_h < best_h:
                best_h = new_h
                best_list = new_list
    if best_h < current_h:
        return hillclimb_helper(best_list, search_cost)
    else:
        return (False, search_cost)

def hillclimb(n):
    n_solved = 0
    total_search_cost = 0
    for i in range(n):
        # create a random board
        list = [random.randint(1, 8) for i in range(8)]
        # solve it
        solved, cost = hillclimb_helper(list, 0)    
        # record result
        if solved:
            n_solved += 1
        total_search_cost += cost
    print('Hill-climbing:',int((n_solved / n)*100), '% solved, ', 'average search cost:', int(total_search_cost / n))
print(n,'puzzles')    

hillclimb(n)





