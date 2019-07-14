"""
You have N bulbs in a row numbered from 1 to N. Initially, all the bulbs are turned off. We turn on exactly one bulb everyday until all bulbs are on after N days.

You are given an array bulbs of length N where bulbs[i] = x means that on the (i+1)th day, we will turn on the bulb at position x where i is 0-indexed and x is 1-indexed.

Given an integer K, find out the minimum day number such that there exists two turned on bulbs that have exactly K bulbs between them that are all turned off.

If there isn't such day, return -1.
"""

"""
Sliding window
"""
class Solution(object):
    def kEmptySlots(self, bulbs, K):
        """
        :type bulbs: List[int]
        :type K: int
        :rtype: int
        """
        days = [0]*len(bulbs)
        
        for day, pos in enumerate(bulbs, 1):
            days[pos-1] = day
            
        left, right = 0, K+1
        result = float('inf')
        i = 0
        while right < len(days):
            if days[i] > days[left] and days[i] > days[right]:
                i += 1
                continue
            if i == right:
                result = min(result, max(days[right], days[left]))
            left = i
            right = i + K + 1
            i += 1
                
        return -1 if result == float('inf') else result
                

def kEmptySlot(flowers, k):

    days = [0] * len(flowers)
    # Get an list that has position as index and day they bloom as value
    for day, pos in enumerate(flowers):
        days[pos-1] = day

    print(days)
    result = 20001
    # Go through the array and at each step, check if the elements between i and i+k+1 have bloomed or not
    left = 0
    right = k+1
    i = 0
    while right < len(flowers):
        if days[i] < days[left] or days[i] <= days[right]:
            if i == right:
                result = min(result, max(days[left], days[right]))
            left, right = i, k+1+i
        i += 1
    return -1 if result == 200001 else result + 1




flowers = [1,3,2]
print(kEmptySlot(flowers, 1))
flowers = [1,3,2,4,5,10,11,12,6,7,8,9]

print(kEmptySlot(flowers, 3))

flowers = [6,5,8,9,7,1,10,2,3,4]

print(kEmptySlot(flowers, 3))
