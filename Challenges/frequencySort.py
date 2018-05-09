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