"""
Sort Characters By Frequency

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""

"""
Time: O(nlog(n))
Space: O(n)
"""
class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = collections.Counter(s)
        s = list(s)
        s.sort(key = lambda x: (-frequency[x], x))
        return ''.join(s)
    
"""
Frequency of a character can vary from 0 to len(s).
Create a hashmap H1 of character to character frequency for the input string.
Iterate H1 to create hashmap H2 with key as frequency and value as substrings of repeated strings with length as the frequency.
Finally lookup all potential frequencies in decreasing order in H2 and produce the final result.

Time: O(N)
Space: O(N)
"""
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        c1, c2 = collections.Counter(s), {}
        for k,v in c1.items():
            c2.setdefault(v, []).append(k*v)
        return "".join(["".join(c2[i]) for i in range(len(s), -1, -1) if i in c2])


class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        charToFreq = {}
        freqToChar = {}
        for c in s:
            if c not in charToFreq:
                charToFreq[c] = 0
            charToFreq[c] += 1
        print(charToFreq)
        for key, value in charToFreq.items():
            if value not in freqToChar:
                freqToChar[value] = []
            freqToChar[value].append(key)
        print(freqToChar)
        result = []
        for key in sorted(freqToChar, reverse = True):
            for char in freqToChar[key]:
                result += [char] * key
        return "".join(result)


class Solution2:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        characters = dict()
        for c in s:
            if c not in characters:
                characters[c] = 1
            else:
                characters[c] += 1
        res = ''
        for c in sorted(characters, key=characters.get, reverse=True):
            n = characters[c]
            for i in range(n):
                res += c

        return res

counter = collections.Counter(s)
        ret = ""
        for char, freq in counter.most_common():
            ret += char * freq
        return ret
