"""
Algo to find all premutation given a list n and output all combination of size k. [order matters]

"""

def perm(n, a): # n = size, a = list of nums
  # recursion anchor
  if n <= 0:
    return [[]]
  else:
    result = []
    for smallPerm in perm(n-1, a):
      # take all elements from a
      for elem in a:
        # and prepend them to all permutations we get from perm(n-1, 1)
        result.append([elem] + smallPerm)
    return result