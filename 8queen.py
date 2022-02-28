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
def hillclimb(list, search_cost):
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
        return hillclimb(best_list, search_cost)
    else:
        return (False, search_cost)

' function to create a random board'
def randomBoard():
    list = [random.randint(1, 8) for i in range(8)]
    print(list)
    h = compute_h(list)
    print('Heuristic', h)
    adjustQueen(list,h)
    return list

' function to adjust the queen'
def adjustQueen(list,h):
    print('----')

def boards():
    for i in range(n):
        hillclimb(randomBoard(), 0)
if __name__ == "__main__":
    boards()


