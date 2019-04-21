"""
Algo to find all premutation given a list n and output all combination of size k. [order not matters]

"""

def comb(n, k): 
    return combHelper([i for i in range(1, n+1)], k)
    
def combHelper(nums, size):
    res = []
    for i in range(len(nums)):
        if size == 1:
            res.append([nums[i]])
        for c in combHelper(nums[i+1:], size-1):
            res.append([nums[i]] + c)
    return res