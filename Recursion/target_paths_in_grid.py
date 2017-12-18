# Randomly fills a grid of size height and width whose values are input by the user,
# with nonnegative integers randomly generated up to an upper bound N also input the user,
# and computes, for each n <= N, the number of paths consisting of all integers from 1 up to n
# that cannot be extended to n+1.
# Outputs the number of such paths, when at least one exists.
#
# Written by Benny Hwang 07/09/2017


from random import seed, randint
import sys
from collections import defaultdict

def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

def get_paths():

    paths= defaultdict(list)
    max_list = []
    find_paths()
    
    for i in range(len(cords)):
        if cords[i] == 'End':
            if str(cords[i-1]).isdigit():
                max_list.append(cords[i-1])

    max_set = set(max_list)

    for i in max_set:
        paths[i] = max_list.count(i)

    return paths


def find_paths(i=None,j=None):
    
    if (i, j) == (None, None):
        for i in range(height):
            for j in range(width):
                if grid[i][j] != 1:
                    continue
                find_paths(i,j)
                       
    else: 
        max_number = grid[i][j]
        cords.append(max_number)
    
        if i and grid[i-1][j] == grid[i][j] +1:
            find_paths(i-1,j)

        if i < height - 1 and grid[i + 1][j] == grid[i][j] + 1:
            find_paths(i+1,j)

        if j and grid[i][j - 1] == grid[i][j] + 1:
            find_paths(i,j-1)
            
        if j < width - 1 and grid[i][j + 1] == grid[i][j] + 1:
            find_paths(i,j+1)

        cords.append("End")

    return 

        
try:
    for_seed, max_length, height, width = [int(i) for i in
                                                  input('Enter four nonnegative integers: ').split()
                                       ]
    if for_seed < 0 or max_length < 0 or height < 0 or width < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randint(0, max_length) for _ in range(width)] for _ in range(height)]
print('Here is the grid that has been generated:')
display_grid()
cords = []
paths = get_paths()
if paths:
    for length in sorted(paths):
        print(f'The number of paths from 1 to {length} is: {paths[length]}')

