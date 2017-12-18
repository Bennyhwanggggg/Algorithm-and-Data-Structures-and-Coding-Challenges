'''
Written by Benny Hwang 09/09/2017
 Finds all triples of consecutive positive three-digit integers
 each of which is the sum of two squares.
'''


def nb_of_consecutive_squares(n):
    for i in range(n//2+1):
        for j in range(i,n//2+1):
            if (i**2+j**2) == n:
                return (i,j)
    return False

sums_of_two_squares = [None] * 1000
for n in range(100, 1001-2):
    i = nb_of_consecutive_squares(n)
    if i:
        j = nb_of_consecutive_squares(n+1)
        if j:
            k = nb_of_consecutive_squares(n+2)
            if k:
                print(('({}, {}, {}) (equal to ({}^2+{}^2, {}^2+{}^2, {}^2+{}^2)) is a solution.').format(n,n+1,n+2, i[0], i[1], j[0], j[1], k[0], k[1]))
