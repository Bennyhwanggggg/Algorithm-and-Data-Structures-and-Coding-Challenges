'''
Written by Benny Hwang 09/09/2017
 Prompts the user for an integer N and finds all perfect numbers up to N.
 Quadratic complexity, can deal with small values only.
'''

import sys


try:
    N = int(input('Input an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

# To find a numbers divisior, we need to go through the whole range up to half
# of that number and check if modulus is 0
def find_divisors(num):
    divisors = []
    for n in range(1,num//2+1):
        if num%n == 0:
            divisors.append(n)
    return divisors

for i in range(2, N + 1):
    divisors = find_divisors(i)
    if i == sum(divisors):
        print(i, "is a perfect number.")


