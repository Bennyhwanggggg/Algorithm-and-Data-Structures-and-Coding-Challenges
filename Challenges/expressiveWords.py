"""
Expressive Words/stretchy words

Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.

Given a list of query words, return the number of words that are stretchy. 

 

Example:
Input: 
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
 

Notes:

0 <= len(S) <= 100.
0 <= len(words) <= 100.
0 <= len(words[i]) <= 100.
S and all words in words consist only of lowercase letters

"""

"""
Two pointer solution
If a letter is not extendable,it means it appears less than 3 times consecutively. This kind of letter has to occur in the same pointer in S and word.
If extendable, the letter must appear more than twice. We just need to look at the previous and next or the two previous. If one condition satisfies, it means at least letters appears 3 times consecutively. Therefore, we just need to update S's pointer.
"""
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        return sum(self.check(S, word) for word in words) # loop through all words to check if word is stretchy to S
        
    def check(self, S, W):
        """
        In check function, use two pointer:

        If S[i] == W[j], i++, j++
        If S[i - 2] == S[i - 1] == S[i] or S[i - 1] == S[i] == S[i + 1], i++
        else return false
        """
        j = 0
        n, m = len(S), len(W)
        for i in range(n):
            if j < m and S[i] == W[j]:
                j += 1
            elif (S[i - 1:i + 2] != S[i] * 3) and (S[i] * 3 != S[i - 2:i + 1]):
                return False
        return j == m

