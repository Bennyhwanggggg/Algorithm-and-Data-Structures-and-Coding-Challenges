"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
"""

"""
Time: O(3^N x 4^M) where N is the number of digits in the input that maps to 3 letters and M is the number of digits that maps to 4 letters and N+M is the total number of digits

Space complexity is the same since that is the number of solutions
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        
        def backtrack(combination, nextDigits):
            if len(nextDigits) == 0:
                output.append(combination)
            else:
                for letter in phone[nextDigits[0]]:
                    backtrack(combination+letter, nextDigits[1:])
        
        output = []
        if digits:
            backtrack('', digits)
        return output


import itertools


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        chars = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        if not digits:
            return []

        letters = []
        for i in digits:
            if i in chars:
                letters.append(chars[i])

        result = []
        for n in itertools.product(*letters):
            word = "".join(list(n))
            result.append(word)
        return result

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        self.dict = {"1":"", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs","8":"tuv","9":"wxyz","10":" "}
        result = [""]
        for digit in digits:
            lst = self.dict[digit]
            newresult = []
            for char in lst:
                for str in result:
                    newresult.append(str+char)
            result = newresult
        return result
