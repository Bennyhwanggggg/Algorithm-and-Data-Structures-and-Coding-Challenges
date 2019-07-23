"""
Given 2 strings s and t, determine if you can convert s into t. The rules are:

You can change 1 letter at a time.
Once you changed a letter you have to change all occurrences of that letter.
Example 1:

Input: s = "abca", t = "dced"
Output: true
Explanation: abca ('a' to 'd') -> dbcd ('c' to 'e') -> dbed ('b' to 'c') -> dced
Example 2:

Input: s = "ab", t = "ba"
Output: true
Explanation: ab -> ac -> bc -> ba
Example 3:

Input: s = "abcdefghijklmnopqrstuvwxyz", t = "bcdefghijklmnopqrstuvwxyza"
Output: false
Example 4:

Input: s = "aa", t = "cd"
Output: false
Example 5:

Input: s = "ab", t = "aa"
Output: true
Example 6:

Input: s = "abcdefghijklmnopqrstuvwxyz", t = "bbcdefghijklmnopqrstuvwxyz"
Output: true
Both strings contain only lowercase English letters.
"""

"""
Time Complexity: O(s)
Space Complexity: O(s)

This seems like those mapping problems of one string to another on steroids. After we modify a certain letter, the new letter for that group may be the same as a later letter in s. So we'd want to use a placeholder for certain mappings, but at what point do we run out of placeholders? Definitely when we're using all 26 letters, but is that the only time? It seems like it's very hard to prove that, given all the potential overlaps of mappings that may occur.

If that is the reality though, I'd say as long as we can map every letter in s to the same letter in b, and as long as there aren't 26 letters (or if there are 26 letters, the strings must be identical), then we can do the conversion...
"""
def convert(s, t):
  if len(s) != len(t):
    return False
        
  if s == t:
    return True
    
  dict_s = {}  # match char in s and t
  unique_t = set()  # count unique letters in t
    
  for i in range(len(s)):
    if (s[i] in dict_s):
      if dict_s[s[i]] != t[i]:
        return False 
    else:
      dict_s[s[i]] = t[i]
    unique_t.add(t[i])
    
  if len(dict_s) == 26:
    return len(unique_t) < 26
    
  return True




if __name__ == '__main__':
	assert convert('abca', 'dced') == True
	assert convert('ab', 'ba') == True
	assert convert('abcdefghijklmnopqrstuvwxyz', 'bcdefghijklmnopqrstuvwxyza') == False
	assert convert('aa', 'cd') == False
	assert convert('ab', 'aa') == True
	assert convert('abcdefghijklmnopqrstuvwxyz', 'bbcdefghijklmnopqrstuvwxyz') == True






