"""
Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
Note:

All words in words and S will only consists of lowercase letters.
The length of S will be in the range of [1, 50000].
The length of words will be in the range of [1, 5000].
The length of words[i] will be in the range of [1, 50].
"""

"""
Next Letter Pointers

Intuition

Since the length of S is large, let's think about ways to iterate through S only once, instead of many times as in the brute force solution.

We can put words into buckets by starting character. If for example we have words = ['dog', 'cat', 'cop'], then we can group them 'c' : ('cat', 'cop'), 'd' : ('dog',). This groups words by what letter they are currently waiting for. Then, while iterating through letters of S, we will move our words through different buckets.

For example, if we have a string like S = 'dcaog':

heads = 'c' : ('cat', 'cop'), 'd' : ('dog',) at beginning;
heads = 'c' : ('cat', 'cop'), 'o' : ('og',) after S[0] = 'd';
heads = 'a' : ('at',), 'o' : ('og', 'op') after S[0] = 'c';
heads = 'o' : ('og', 'op'), 't': ('t',) after S[0] = 'a';
heads = 'g' : ('g',), 'p': ('p',), 't': ('t',) after S[0] = 'o';
heads = 'p': ('p',), 't': ('t',) after S[0] = 'g';

Time: O(S.length + sum(words[i].length))
Space: O(words.length)
"""
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        res = 0
        waiting = collections.defaultdict(list)
        for it in map(iter, words):
            waiting[next(it)].append(it)
        
        for c in S:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)
        return len(waiting[None]) # only the Nones are the ones where words has become empty

"""
Brute force
"""
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        count = 0
        
        for word in words:
            i = 0
            j = 0
            while j < len(word) and i < len(S):
                if S[i] == word[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            if j == len(word):
                count += 1
        
        return count
        

