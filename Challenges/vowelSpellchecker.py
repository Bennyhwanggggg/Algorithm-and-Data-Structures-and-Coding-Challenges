"""
Vowel Spellchecker

Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

For a given query word, the spell checker handles two categories of spelling mistakes:

Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
In addition, the spell checker operates under the following precedence rules:

When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
When the query matches a word up to capitlization, you should return the first such match in the wordlist.
When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
If the query has no matches in the wordlist, you should return the empty string.
Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].
"""

"""
Intuition and Algorithm

We analyze the 3 cases that the algorithm needs to consider: when the query is an exact match, when the query is a match up to capitalization, and when the query is a match up to vowel errors.

In all 3 cases, we can use a hash table to query the answer.

For the first case (exact match), we hold a set of words to efficiently test whether our query is in the set.
For the second case (capitalization), we hold a hash table that converts the word from its lowercase version to the original word (with correct capitalization).
For the third case (vowel replacement), we hold a hash table that converts the word from its lowercase version with the vowels masked out, to the original word.
The rest of the algorithm is careful planning and reading the problem carefully.

Time: O(C)
Space: O(C)
"""
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        wordSet = set(wordlist)
        wordCap, wordVowel = dict(), dict()
        
        def devowel(w):
            return ''.join('*' if c in 'aeiou' else c for c in w)
        
        for word in wordlist:
            if word.lower() not in wordCap:
                wordCap[word.lower()] = word
            devowelWord = devowel(word.lower())
            if devowelWord not in wordVowel:
                wordVowel[devowelWord] = word
            
        res = []
        for query in queries:
            if query in wordSet:
                res.append(query)
                continue
            
            if query.lower() in wordCap:
                res.append(wordCap[query.lower()])
                continue
            dword = devowel(query.lower())
            if dword in wordVowel:
                res.append(wordVowel[dword])
                continue
            res.append('')
        return res
                
        
                

