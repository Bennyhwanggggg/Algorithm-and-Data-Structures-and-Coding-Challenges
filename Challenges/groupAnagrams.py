"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

"""
Intuition

Two strings are anagrams if and only if their sorted strings are equal.

Algorithm

Maintain a map ans : {String -> List} where each key K is a sorted string, and each value is the list of strings from the initial input that when sorted, are equal to K.

Time: O(NKlogK) where N is lenght of strs and K is the max length of a string in strs
Space: O(NK)
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            key = ''.join(sorted(word))
            anagrams[key].append(word)
        
        result = []
        for word in anagrams:
            result.append(anagrams[word])
        return result

"""
Categorize by count using some kind of hash
Time: O(NK)
Space: O(NK)
"""

class Solution:
    def groupAnagrams(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
