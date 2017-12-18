'''
Prompts the user to input the digits 1 to 8 (with possibly whitespace inserted anywhere), in some order,
say d1 d2 d3 d4 d5 d6 d7 d8, without repetition; if the input is incorrect, then the program outputs an
error message and exits.

Finds the minimal number of steps needed to go from the initial state, represented as

            1 2 3 4
            8 7 6 5

to the final state given by user, using three operations:
    - row exchange
    - right circular shift
    - midlle clockwise rotation

Written by Benny Hwang 15/08/2017
'''

import sys
from collections import deque

def row_exchange(state1):
    s1 = deque(state1)
    s1.reverse()
    state2 = list(s1)
    return state2

def right_circular_shift(state1):
    
    s1 = deque(state1[0:4])
    s2 = deque(state1[4:8])
    s1.rotate(1)
    s2.rotate(-1)
    state2 = s1+s2
    state2 = list(state2)
    
    return state2

def mid_clockwise_rot(state1):
    
    s1 = deque(state1[0:4])
    s2 = deque(state1[4:8])
    ind_0_3 = s1.pop()
    ind_0_0 = s1.popleft()
    ind_1_3 = s2.pop()
    ind_1_0 = s2.popleft()
    state2 = s1+s2
    state2.rotate(1)
    state2.extendleft(ind_0_0)
    state2.extend(ind_1_3)
    state2.insert(3,ind_0_3)
    state2.insert(4,ind_1_0)
    state2 = list(state2)
    
    return state2

if __name__ == "__main__":
    user_input = input('Input final configuration: ')
    input_elements = list(user_input)   
    
    final = []
    try:
        for elements in input_elements:
            if elements != ' ':
                if not elements.isdigit():
                    raise ValueError
                if int(elements)>8 or int(elements)<1:
                    raise ValueError
                if elements not in final:
                    final.append(elements)
                else:
                    raise ValueError
        if len(final) != 8:
            raise ValueError
               
    except ValueError:
        print('Incorrect configuration, giving up...')
        sys.exit()     
       
    initial = deque('12345678')
    final_deq = deque(final)
    
    found = False
    steps = 0
    used_node = set()
    To_visit_nodes = []
    To_visit_nodes.append(list(initial))
    To_visit_nodes.append(steps)
    q = []
    q.append(To_visit_nodes)
    queue = deque(q)
    
    if final_deq == initial:
        print(str(steps) + ' steps are needed to reach the final configuration')
    
    else:
    
        while found == False:
            
            node_set = queue.popleft()
            node = node_set[0]
            steps = node_set[1]
            node_tup = tuple(node)
            steps += 1
            if node_tup not in used_node:
                
                used_node.add(node_tup)
                
                rcs = right_circular_shift(node)
                if rcs == final:
                    found = True
                    print(str(steps) + ' steps are needed to reach the final configuration')
                    break
                if tuple(rcs) not in used_node:
                    To_visit_nodes = []
                    To_visit_nodes.append(rcs)
                    To_visit_nodes.append(steps)                  
                    queue.append(To_visit_nodes)
                    
                msr = mid_clockwise_rot(node)
                if msr == final:
                    found = True
                    print(str(steps) + ' steps are needed to reach the final configuration')
                    break                
                if tuple(msr) not in used_node:
                    To_visit_nodes = []
                    To_visit_nodes.append(msr)
                    To_visit_nodes.append(steps)                    
                    queue.append(To_visit_nodes) 
                    
                row_exc = row_exchange(node)
                if row_exc == final:
                    found = True
                    print(str(steps) + ' steps are needed to reach the final configuration')
                    break                   
                if tuple(row_exc) not in used_node:
                    To_visit_nodes = []
                    To_visit_nodes.append(row_exc)
                    To_visit_nodes.append(steps)                                       
                    queue.append(To_visit_nodes)                
                           
