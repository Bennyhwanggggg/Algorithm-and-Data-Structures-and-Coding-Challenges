# Randomly fills a grid of size 10 x 10 with digits between 0
# and bound - 1, with bound provided by the user.
# Given a point P of coordinates (x, y) and an integer "target"
# also all provided by the user, finds a path starting from P,
# moving either horizontally or vertically, in either direction,
# so that the numbers in the visited cells add up to "target".
# The grid is explored in a depth-first manner, first trying to move north,
# always trying to keep the current direction,
# and if that does not work turning in a clockwise manner.
#
# Written by Benny Hwang 11/11/2017


import sys
from random import seed, randrange
import time
from stack_adt import *


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

def explore_depth_first(x, y, target):
    directions = {'N': (-1, 0),'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}
    next_direction = {'': ('W','S','E','N'), 'N': ('W','E','N'), 'W': ('S','N','W'), 'S': ('E','W','S'), 'E': ('N','S','E')}
    paths = Stack()
    current_sum = 0
    paths.push(([(x,y)],current_sum,''))
    final_path = False
    timeout = time.time() + 28
    while not paths.is_empty():
        
        (path, pos_sum, previous_direction) = paths.pop()
        current_position = path[-1]
        current_sum = pos_sum + grid[current_position[0]][current_position[1]]

        if current_sum == target:
            final_path = path
            break
        if not final_path and time.time()>timeout:
            break        
        if not final_path:
            for new_direction in next_direction[previous_direction]:
                new_position = (current_position[0] + directions[new_direction][0],
                                current_position[1] + directions[new_direction][1])
                        # Check if still within grid when moving in this direction
                if new_position[0] not in range(10) or new_position[1] not in range(10):
                    direction_change = True
                    move = False
                    continue
                        # Check if repeated cell
                if new_position in path:
                    direction_change = True
                    move = False
                    continue
                    # Check if the sum will exceed
                if current_sum + grid[new_position[0]][new_position[1]] > target:
                    direction_change = True
                    move = False
                    continue
                path_copy = list(path)
                path_copy.append(new_position)
                pos_sum = current_sum
                paths.push((path_copy,pos_sum,new_direction))
        
    return final_path
      

try:
    for_seed, bound, x, y, target = [int(x) for x in input('Enter five integers: ').split()]
    if bound < 1 or x not in range(10) or y not in range(10) or target < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [[randrange(bound) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
path = explore_depth_first(x, y, target)
if not path:
    print(f'There is no way to get a sum of {target} starting from ({x}, {y})')    
else:
    print('With North as initial direction, and exploring the space clockwise,')
    print(f'the path yielding a sum of {target} starting from ({x}, {y}) is:')    
    print(path)

