"""
Find Common Characters

Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
"""
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        check = set(A[0])
        result = [[l] * min([a.count(l) for a in A]) for l in check]
        return sorted([i for e in result for i in e])
    
from collections import Counter

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        my_list, res = [], []
        for v in A:
            my_list.append(Counter(v))
        for key in my_list[0]:
            times = my_list[0][key]
            for e in my_list[1:]:
                times = min(times, e[key])
            for _ in range(times):
                res.append(key)
        return res
    
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        output = []
        for letter in set(min(A)):
            count = 100
            for word in A:
                count = min(count, word.count(letter))
            while count > 0:
                count -= 1
                output.append(letter)
        return output


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []

        letters = set()
        for word in A:
            for letter in word:
                letters.add(letter)
        repeats = []
        for l in letters:
            occurance = min([word.count(l) for word in A])
            repeats.extend([l]*occurance)
        return repeats
