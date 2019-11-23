"""
Permutation in String

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""

"""
Sliding Window
Time: O(l1 + 26*(l2-l1))
Space: O(1)?
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        counts = collections.Counter(s1)
        i = 0
        while i < len(s2)-len(s1)+1:
            if s2[i] in counts:
                remain = collections.Counter(s2[i:i+len(s1)])
                if remain == counts:
                    return True
            i += 1
        return False
    
        '''
        Approach 2:
        Use the same counter but much more effeciently
        63% beated, okay not bad..
        two pointers i(front) j(last), delete and add accordingly and check for the counts
        
        # Code Below
        '''
        ctr1 = collections.Counter(s1)
        ctr2 = collections.Counter(s2[:len(s1)])
            
        i = 0; j = len(s1)
        
        while j < len(s2):
            if ctr2 == ctr1: return True
            ctr2[s2[i]] -= 1
            if ctr2[s2[i]] < 1: ctr2.pop(s2[i]); 
            ctr2[s2[j]] = ctr2.get(s2[j], 0) + 1
            i += 1; j += 1
            
        return ctr2 == ctr1
                
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        counts1 = collections.Counter(s1)
        counts2 = collections.Counter(s2[:len(s1)])
        i, j = 0, len(s1)
        
        while j < len(s2):
            if counts1 == counts2:
                return True
            counts2[s2[i]] -= 1
            
            if counts2[s2[i]] == 0:
                counts2.pop(s2[i])
            
            counts2[s2[j]] = counts2.get(s2[j], 0) + 1
            
            i += 1
            j += 1
        
        return counts1 == counts2
