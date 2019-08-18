"""
Palindrome Permutation

Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
"""

"""
HashMap
Time: O(N)
Space: O(N)
"""
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        counts = collections.Counter(s)
        
        odd_used = False
        for ch in counts.keys():
            if counts[ch]%2:
                if len(s)%2 == 0 or odd_used:
                    return False
                odd_used = True
        return True

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = dict()
        for c in s:
            counts[c] = counts.get(c, 0) + 1
            
        n = len(s)
        
        if len(counts) > (n//2)+1:
            return False
        
        if n%2:
            two_odds = False
            for c in counts:
                if counts[c]%2:
                    if two_odds:
                        return False
                    two_odds = True
                    break
            return True
        else:
            for c in counts:
                if counts[c]%2:
                    return False
            return True
        
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = dict()
        for c in s:
            counts[c] = counts.get(c, 0) + 1
            
        res = 0
        for c in counts:
            res += counts[c]%2
        return res <= 1
    
"""
Use Set to keep track of odd elements and remove when necessary
Time: O(n)
Space: O(n)
"""
public class Solution {
    public boolean canPermutePalindrome(String s) {
        Set < Character > set = new HashSet < > ();
        for (int i = 0; i < s.length(); i++) {
            if (!set.add(s.charAt(i)))
                set.remove(s.charAt(i));
        }
        return set.size() <= 1;
    }
}



class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Only at most one character can appear odd number of times.
        charmap = dict()
        for c in s:
            if c not in charmap:
                charmap[c] = 1
            else:
                charmap[c] += 1
        oddcount = 0
        for c in charmap:
            if charmap[c]%2:
                oddcount += 1
            if oddcount >= 2:
                return False
        return True
