"""
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
"""
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # difference between each word's ord must be the same
        
        res = []
        for i in range(len(strings)):
            if not strings[i]:
                continue
            temp = [strings[i]]
            for j in range(i+1, len(strings)):
                if not strings[j] or len(strings[i]) != len(strings[j]):
                    continue
                if self.checkDiff(strings[i], strings[j]):
                    temp.append(strings[j])
                    strings[j] = None
            res.append(temp)
        return res
                
    
    def checkDiff(self, a, b):
        diff = None
        for i, j in zip(a, b):
            if diff is None:
                diff = (ord(i) - ord(j))%26
            else:
                if diff != (ord(i) - ord(j))%26:
                    return False
        return True

"""
Time complexity would be O(ab) where a is the total number of strings and b is the length of the longest string in strings.
Space complexity would be O(n), as the most space we would use is the space required for strings and the keys of our hashmap.
"""        
def groupStrings(self, strings: List[str]) -> List[List[str]]:
	hashmap = {}
	for s in strings:
		key = ()
		for i in range(len(s) - 1):
			circular_difference = 26 + ord(s[i+1]) - ord(s[i])
			key += (circular_difference % 26,)
		hashmap[key] = hashmap.get(key, []) + [s]
	return list(hashmap.values())


