'''
Written by Benny Hwang 15/09/2017
 Prompts the user for two numbers, say available_digits and desired_sum, and
 outputs the number of ways of selecting digits from available_digits
 that sum up to desired_sum.
'''

import sys

def solve(available_digits, desired_sum):    
    digits = [int(n) for n in str(available_digits)]
    if sum(digits) == desired_sum:
        return 1
    if not available_digits:
        return 0
    return solve(available_digits//10, desired_sum) + solve(available_digits//10, desired_sum-available_digits%10)
try:
    available_digits = abs(int(input('Input a number that we will use as available digits: ')))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    desired_sum = int(input('Input a number that represents the desired sum: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_solutions = solve(available_digits, desired_sum)
if nb_of_solutions == 0:
    print('There is no solution.')
elif nb_of_solutions == 1:
    print('There is a unique solution.')
else:
    print(('There are {} solutions.').format(nb_of_solutions))

