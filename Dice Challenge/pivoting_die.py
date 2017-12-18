'''
Consider a board similar to the one below

                    7   8   9   10   
                    6   1   2   11
                    5   4   3
                    
However, imagine it as being infinite. A die is initially placed at 1 and can only
move to the next consecutive number (e.g 1 to 2, 2 to 3...)

Prompts the user for a natural number N at least equal to 1, and outputs the numbers at the top, the front and the right after the die has been moved to cell N.

Written by Benny Hwang 13/08/2017
'''


import math

def move_right(Current_faces):
    Top_old = Current_faces[0]
    Right_old = Current_faces[2]
    Bottom_old = Current_faces[3]
    Left_old = Current_faces[5]
    
    Top_new = Left_old
    Front_new = Current_faces[1]
    Right_new = Top_old
    Bottom_new = Right_old
    Back_new = Current_faces[4]
    Left_new = Bottom_old
    
    Current_faces = [Top_new, Front_new, Right_new, Bottom_new, Back_new, Left_new]
    
    return Current_faces
    
def move_left(Current_faces):
    Top_old = Current_faces[0]
    Right_old = Current_faces[2]
    Bottom_old = Current_faces[3]
    Left_old = Current_faces[5]
    
    Top_new = Right_old
    Front_new = Current_faces[1]
    Right_new = Bottom_old
    Bottom_new = Left_old
    Back_new = Current_faces[4]
    Left_new = Top_old
    
    Current_faces = [Top_new, Front_new, Right_new, Bottom_new, Back_new, Left_new]
    
    return Current_faces
    
def move_forward(Current_faces):
    Top_old = Current_faces[0]
    Front_old = Current_faces[1]
    Bottom_old = Current_faces[3]
    Back_old = Current_faces[4]
    
    Top_new = Back_old
    Front_new = Top_old
    Right_new = Current_faces[2]
    Bottom_new = Front_old
    Back_new = Bottom_old
    Left_new = Current_faces[5]
    
    Current_faces = [Top_new, Front_new, Right_new, Bottom_new, Back_new, Left_new]
    
    return Current_faces
    
def move_back(Current_faces):
    Top_old = Current_faces[0]
    Front_old = Current_faces[1]
    Bottom_old = Current_faces[3]
    Back_old = Current_faces[4]
    
    Top_new = Front_old
    Front_new = Bottom_old
    Right_new = Current_faces[2]
    Bottom_new = Back_old
    Back_new = Top_old
    Left_new = Current_faces[5]
    
    Current_faces = [Top_new, Front_new, Right_new, Bottom_new, Back_new, Left_new]
    
    return Current_faces

if __name__ == '__main__':
    
    N = False

    while N == False:
        
        N = input("Enter the desired goal cell number: ")
        
        if not N.isdigit():
            print('Incorrect value, try again')
            N = False
        elif int(N) <1:
            print('Incorrect value, try again')
            N = False

    N = int(N)
            
    Top = 3
    Front = 2
    Right = 1
    Bottom = 4
    Back = 5
    Left = 6

    Current_faces = [Top, Front, Right, Bottom, Back, Left]

    Square_size = []
    if N > 1:
        for i in range(1, N, 2):
            if i**2 <= N:
                i_copy = i
                Square_size.append(i**2)
    else:
        i = 1;
        Square_size.append(i)
            
    if N not in Square_size:
        val = (i_copy+2)**2
        Square_size.append(val)
            
    Cell = int(1)

    for i in Square_size:
        
        if Cell < N & Cell==1:
            Current_faces = move_right(Current_faces)
            Cell += 1
               
        max_dir_step = int(math.sqrt(i) - 1)
        
        if max_dir_step == 0:
            max_dir_step == 1

        steps = 0
        while steps < max_dir_step-1 and Cell < N:
            Current_faces = move_forward(Current_faces)
            steps += 1
            Cell += 1
        steps = 0
        while steps < max_dir_step and Cell < N:
            Current_faces = move_left(Current_faces)
            steps += 1
            Cell += 1 
        steps = 0
        while steps < max_dir_step and Cell < N:
            Current_faces = move_back(Current_faces)
            steps += 1
            Cell += 1
        steps = 0
        while steps < max_dir_step+1 and Cell < N:
            Current_faces = move_right(Current_faces)
            steps += 1
            Cell += 1       
                    
    Top = Current_faces[0]
    Front = Current_faces[1]
    Right = Current_faces[2]
    Bottom = Current_faces[3]
    Back = Current_faces[4]
    Left = Current_faces[5]

    print('On cell ' + str(N) + ', ' + str(Top) + ' is at the top, ' + str(Front) + ' at the front, and ' + str(Right) + ' on the right.')
        

    

