"""
Function that takes two lists, and returns two things: elements in the first list not in the second, and elements in the second list which are not in the first.

list1 = [a, a, b, c]
list2 = [a, b, b, d]
want output: [a, c], [b, d]
"""

import collections

def uniqueElements(a,b):
    cnt_a = collections.Counter(a)
    cnt_b = collections.Counter(b)

    res_a = [x for x, i in (cnt_a - cnt_b).items() for _ in range(i)]
    res_b = [x for x, i in (cnt_b - cnt_a).items() for _ in range(i)]

    return (res_a, res_b)

if __name__ == '__main__':
 	  assert uniqueElements(['a', 'a', 'b', 'c'], ['a', 'b', 'b', 'd']) == (['a', 'c'], ['b', 'd'])