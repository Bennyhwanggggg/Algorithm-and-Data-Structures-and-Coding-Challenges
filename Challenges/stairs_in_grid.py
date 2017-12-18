# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and finds out, for given step_number >= 1
# and step_size >= 2, the number of stairs of step_number many steps,
# with all steps of size step_size.
#
# A stair of 1 step of size 2 is of the form
# 1 1
#   1 1
#
# A stair of 2 steps of size 2 is of the form
# 1 1
#   1 1
#     1 1
#
# A stair of 1 step of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#
# A stair of 2 steps of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#         1
#         1 1 1
#
# The output lists the number of stairs from smallest step sizes to largest step sizes,
# and for a given step size, from stairs with the smallest number of steps to stairs
# with the largest number of stairs.
#
# Written by Benny Hwang 24/08/2017


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))

def stairs_in_grid():
    d = defaultdict()
    count = 0
    
    #print(listof1s_Ind)
    valid_step_size = []
    for step_size in range(1,dim):
        nb_of_steps_nb_of_stairs_set = set()
        stair_used = set()
        number_of_stair_cnt = []
        for i in listof1s_Ind:
            x = i[0]
            y = i[1]
            
            
            #step_size = 1
    
            start = check_if_stairs(i,step_size)
            
            if start == True:
                
                if i not in stair_used:
                    stair_used.add(i)
                    corner = tuple([x+step_size,y+step_size])
                    stair_used.add(corner)
                    
                    number_of_steps = 1
                    
                    first_xend = x+step_size
                    first_yend = y+step_size+step_size
                    location = tuple([first_xend,first_yend])

                    while step_extend(location,step_size) == True:
                        
                        x = location[0]+step_size
                        y = location[1]+step_size
                        location = tuple([x,y]) 
                        corner = tuple([x,y-step_size])
                        stair_used.add(corner) 
                        number_of_steps += 1
                    
                    number_of_stair_cnt.append(number_of_steps)
                    
        if len(number_of_stair_cnt)>0:
            valid_step_size.append(step_size)
            elements = set(number_of_stair_cnt)
            for i in elements:
                count = number_of_stair_cnt.count(i)
                
                combine = [i,count]
                combined_tuple = tuple(combine)
                nb_of_steps_nb_of_stairs_set.add(combined_tuple)
            
            nb_of_steps_nb_of_stairs_set2 = sorted(nb_of_steps_nb_of_stairs_set)
            d[step_size+1] = nb_of_steps_nb_of_stairs_set2
			
    return d
    
def check_if_stairs(location,step_size):
    x = location[0]
    y = location[1] 
    
    stair_start = False
    horizontal = False
    vertical = False
    end = False
    
    set_to_check = set()
    for step_range in range(1,step_size+1):
        set_to_check.add(tuple([x,y+step_range]))
    if set_to_check.issubset(listof1s_Ind)==True:
        horizontal = True
    
    set_to_check = set()
    if horizontal == True:
        for step_range in range(1,step_size+1):
            set_to_check.add(tuple([x+step_range,y+step_size]))
        if set_to_check.issubset(listof1s_Ind)==True:                 
            vertical = True
    
    set_to_check = set()           
    if vertical == True:
        for step_range in range(1,step_size+1):
            set_to_check.add(tuple([x+step_size,y+step_size+step_range]))
        if set_to_check.issubset(listof1s_Ind)==True:                     
            stair_start = True
                     
    return stair_start
                
    
def step_extend(location,step_size):
    x = location[0]
    y = location[1] 
    stair_exist = False
    
    horizontal = False
    set_to_check = set() 
    for step_range in range(1,step_size+1):
        set_to_check.add(tuple([x+step_range,y]))
    if set_to_check.issubset(listof1s_Ind)==True:
        horizontal = True
     
    set_to_check = set()   
    if horizontal == True:
        for step_range in range(1,step_size+1):
            set_to_check.add(tuple([x+step_size, y+step_range]))
        if set_to_check.issubset(listof1s_Ind)==True:
            stair_exist = True            

    return stair_exist
        

# Possibly define other functions

try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()

listof1s_Ind = [(ix,j) for ix, row in enumerate(grid) for j, i in enumerate(row) if i != 0]
# A dictionary whose keys are step sizes, and whose values are pairs of the form
# (number_of_steps, number_of_stairs_with_that_number_of_steps_of_that_step_size),
# ordered from smallest to largest number_of_steps.
stairs = stairs_in_grid()
for step_size in sorted(stairs):
    print(f'\nFor steps of size {step_size}, we have:')
    for nb_of_steps, nb_of_stairs in stairs[step_size]:
        stair_or_stairs = 'stair' if nb_of_stairs == 1 else 'stairs'
        step_or_steps = 'step' if nb_of_steps == 1 else 'steps'
        print(f'     {nb_of_stairs} {stair_or_stairs} with {nb_of_steps} {step_or_steps}')
