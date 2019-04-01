class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set()
        duplicates = set()
        for n in nums:
            if n not in seen:
                seen.add(n)
            else:
                duplicates.add(n)
        return list(duplicates)

class Solution:
  def findDuplicates(self, nums: 'List[int]') -> 'List[int]':
    N = len(nums)
    for n in nums:
      i = n%N - 1
      nums[i] += N
    return [i+1 for i in range(len(nums)) if nums[i] > 2*N ]


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # trick: for each num, encode the number at that num's idx-1
        
        res = []
        
        for idx, val in enumerate(nums):
            target_idx = abs(val)-1
            
            # if encoded entry is negative, we've seen it before
            if nums[target_idx] < 0:
                res.append(abs(val))
            
            # if not encoded, then we need to encode it
            else:
                nums[target_idx] = -nums[target_idx]
                
        return res 
