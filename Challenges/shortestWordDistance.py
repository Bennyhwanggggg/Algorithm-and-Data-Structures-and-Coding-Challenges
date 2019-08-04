"""
Shortest Word Distance

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""

"""
store the most recent locations of word1 and word2. Each time we find a new occurrence of one of the words, we do not need to search the entire array for the other word, since we already have the index of its most recent occurrence.

Time: O(N)
Space: O(1)
"""
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        res = len(words)
        idx1, idx2 = -1, -1
        for i in range(len(words)):
            if words[i] == word1:
                idx1 = i
            elif words[i] == word2:
                idx2 = i
            
            if idx1 != -1 and idx2 != -1:
                res = min(res, abs(idx1-idx2))
        return res

