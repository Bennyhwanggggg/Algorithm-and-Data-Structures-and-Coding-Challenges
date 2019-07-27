"""
Palindrome Permutation II

Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

Example 1:

Input: "aabb"
Output: ["abba", "baab"]
Example 2:

Input: "abc"
Output: []
"""

"""
Algorithm

It might be possible that no palindromic permutation could be possible for the given string ss. Thus, it is useless to generate the permutations in such a case. Taking this idea, firstly we check if a palindromic permutation is possible for ss. If yes, then only we proceed further with generating the permutations. To check this, we make use of a hashmap mapmap which stores the number of occurences of each character(out of 128 ASCII characters possible). If the number of characters with odd number of occurences exceeds 1, it indicates that no palindromic permutation is possible for s.

Once we are sure that a palindromic permutation is possible for s, we go for the generation of the required permutations. But, instead of wildly generating all the permutations, we can include some smartness in the generation of permutations i.e. we can generate only those permutations which are already palindromes.

One idea to to do so is to generate only the first half of the palindromic string and to append its reverse string to itself to generate the full length palindromic string.

Based on this idea, by making use of the number of occurences of the characters in s stored in map, we create a string st which contains all the characters of ss but with the number of occurences of these characters in st reduced to half their original number of occurences in s.

Thus, now we can generate all the permutations of this string st and append the reverse of this permuted string to itself to create the palindromic permutations of s.

In case of a string s with odd length, whose palindromic permutations are possible, one of the characters in s must be occuring an odd number of times. We keep a track of this character, ch, and it is kept separte from the string st. We again generate the permutations for stst similarly and append the reverse of the generated permutation to itself, but we also place the character chch at the middle of the generated string.

In this way, only the required palindromic permutations will be generated. Even if we go with the above idea, a lot of duplicate strings will be generated.

In order to avoid generating duplicate palindromic permutations in the first place itself, as much as possible, we can make use of this idea. As discussed in the last approach, we swap the current element with all the elements lying towards its right to generate the permutations. Before swapping, we can check if the elements being swapped are equal. If so, the permutations generated even after swapping the two will be duplicates(redundant). Thus, we need not proceed further in such a case.

Time: O((n/2+1)!) since almost (n/2)! permuatations need to be generated
Space: O(N), depth of recursion can go uptp n/2 in the worst case
"""
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        seen = collections.Counter(s)
        ans = []
        mid = [k for k, v in seen.items() if v%2]
        n = len(s)
        if len(mid) > 1:
            return ans
        
        def helper(tmp):
            if len(tmp) == n:
                ans.append(tmp)
                return 
            for k, v in seen.items():
                if v > 0:
                    seen[k] -= 2
                    helper(k + tmp + k)
                    seen[k] += 2

        if len(mid) > 1:
            return []
        if len(mid) == 1:
            seen[mid[0]] -= 1
            helper(mid[0])
        else:
            helper('')
        return ans
        
        
        
        
        
        
        
        
        
        

