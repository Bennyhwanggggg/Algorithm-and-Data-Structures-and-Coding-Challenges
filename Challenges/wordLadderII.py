"""
Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

"""
BFS, better one is two direction bfs
Time: O(b*d)
Space: O(nL)
"""
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        graph = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                tranWord = word[:i] + '*' + word[i+1:]
                graph[tranWord].append(word)
        
        queue = collections.deque([(beginWord, [beginWord])])
        
        res = []
        minLen = float('inf')
        seen = set()
        while queue:
            currWord, currSeq = queue.popleft()
            if currWord == endWord:
                if len(currSeq) == minLen:
                    res.append(currSeq)
                elif len(currSeq) < minLen:
                    res = [currSeq]
                minLen = min(minLen, len(currSeq))
            
            seen.add(currWord)
            
            for i in range(len(currWord)):
                neiWord = currWord[:i] + '*' + currWord[i+1:]
                for nei in graph[neiWord]:
                    if nei not in seen:
                        queue.append((nei, currSeq+[nei]))
        return res
                

