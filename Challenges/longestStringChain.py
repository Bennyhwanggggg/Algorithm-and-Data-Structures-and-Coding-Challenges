"""
Longest String Chain

Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.

 

Example 1:

Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".
 

Note:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of English lowercase letters.
"""

"""
Explanation
Sort the words by word's length. (also can apply bucket sort)
For each word, loop on all possible previous word with 1 letter missing.
If we have seen this previous word, update the longest chain for the current word.
Finally return the longest word chain.


Complexity
Time O(NlogNS)
Space O(NS)
"""
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x: len(x))
        dp = dict()
        for word in words:
            for i in range(len(word)):
                dp[word] = max(dp.get(word[:i]+word[i+1:], 0) + 1, dp.get(word, 0))
        return max(dp.values())
    
class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = sorted(words, key=lambda word:len(word))
        word_dict = {}
        
        for word in words:
            word_dict[word] = 1
        
        longest = 1
        for word in words:
            for i in xrange(len(word)):
                if word[:i] + word[i + 1:] in word_dict:
                    word_dict[word] = word_dict[word[:i] + word[i + 1:]] + 1
                    longest = max(longest, word_dict[word])
        
        return longest

