"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""

# Time O(n), Space: O(n)
class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s:
            return s
        left, right = 0, len(s)-1
        letters = list(s)
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        while left < right:
            while left < len(s) and letters[left].lower() not in vowels:
                left += 1
            while right >= 0 and letters[right].lower() not in vowels:
                right -= 1
            
            if left < right:
                letters[left], letters[right] = letters[right], letters[left]
        
            left += 1
            right -= 1
        
        return ''.join(letters)
            
                
                
        
        

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        i, j = 0, len(s)-1
        while i < j:
            if s[i] not in vowels:
                i += 1
            if s[j] not in vowels:
                j -= 1
            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return ''.join(s)
