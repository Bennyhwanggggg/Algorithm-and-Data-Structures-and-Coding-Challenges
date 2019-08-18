"""
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
"""

"""
Two pointers

Use two pointers to check each word and update result. Final sort may not be necessar
if we update results properly by checking lengths etc.

Time: O(n log n) due to sort
Space: O(n)

Time: O(n x) where n is number of words in d and x is length of string (without final sort)
Space: O(x) to store string result of len(x)
"""
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:        
        d.sort(key = lambda x: (-len(x), x))
        for word in d:
            i = 0
            for c in s:
                if i < len(word) and word[i] == c:
                    i += 1
            if i == len(word):
                return word
        return ""


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:        
        result = []
        for word in d:
            i, j = 0, 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            if j == len(word):
                result.append(word)
        
        if not result:
            return ''
        return sorted(result, key= lambda x:(-len(x), x))[0]
        

