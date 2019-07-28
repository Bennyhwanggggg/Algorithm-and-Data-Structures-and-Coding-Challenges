"""

Given a positive integer represented as a string of length N, and an integer K (0 <= K <= N), find the largest subsequence of length K in the string.

Input: "3141592", K == 4
Output: "4592"
"""

"""
Use the num from the N-K element, start from that position, I go backwards and find the maximum number in that range and its index

in the next search, I use n-k-1 element, and search the range between the previous index and the n-k-1 element
repeat until i reach the n element

9991911
k=3


  v
3141 | 592

xx
31 15 | 92

Push each element into a heap with (val, idx), for each K
pop the top element and keep track of current idx, if an element is before the current idx, keep popping until we get the next largest one that is after the current idx
"""

def solution(input_string, k):
    N = len(input_string) # N = 7
    nums = list(map(int, list(input_string))) # [3 1 4 1 5 9 2]
    start = 0
    res = ''
    while k > 0:
        curr = N-k # 6
        num = int(input_string[curr]) # 2
        max_index = nums.index(max(nums[start: curr+1])) # 9
        start = max_index+1 # 
        res += input_string[max_index] # 4592
        k -= 1
    
    return res

print(solution('3141592', 4))

"""
"Hashmap " time: O(N)
3141

{
    1: [1, 3]
    3: [0]
    4: [2]
}

{
    3: 0
    1: 0
    4: 0 => max 4 add to res
    5: 1
    9: 1
    2: 1
}
"""

"""
Heap: O(NlogN)
"""
def solution2(input_string, k):
    N = len(input_string) 
    nums = []
    for idx, val in enumerate(input_string[:N-k+1]):
        nums.append((-val, idx))
    heapq.heapify(nums) # 3141 with idx
    prev = 0
    res = ''
    for i in range(1, k+1):
        -val, idx = heapq.heapop(nums)
        while idx < prev:
            # continue pop
            -val, idx = heapq.heapop(nums)
        prev = idx+1 # prev = 3
        res += val # 4
        heapq.heappush((-int(input_string[N-k+i], N-k+i))) # N-k
    return res
                       
# "911111", K == 3

'''

"3141592"
"1123459"

'''
