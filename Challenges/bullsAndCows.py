"""
Bulls and Cows

You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.
"""

"""
Brute force search
"""
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = 0
        
        s = list(secret)
        g = list(guess)
        
        for i in range(len(s)):
            if s[i] == g[i]:
                bull += 1
                s[i] = -1
                g[i] = -1
        
        for i in range(len(s)):
            if g[i] == -1:
                continue
            else:
                p1 = i-1
                p2 = i+1
                found = False
                while p1 >= 0:
                    if s[p1] == g[i]:
                        cow += 1
                        found = True
                        s[p1] = -1
                        break
                    p1 -= 1
                if not found:
                    while p2 < len(s):
                        if s[p2] == g[i]:
                            cow += 1
                            s[p2] = -1
                            break
                        p2 += 1
                    
        return '{}A{}B'.format(bull, cow)

"""
More efficient solution using dict
Time: O(n)
Space: O(n)
"""
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s = dict()
        g = dict()
        
        A, B = 0, 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                s[secret[i]] = s.get(secret[i], 0) + 1
                g[guess[i]] = g.get(guess[i], 0) + 1
                
        print(s, g)
        for ele in g:
            if ele in s:
                B += min(s[ele], g[ele])
            
        return '{}A{}B'.format(A, B)
        
                            
                
