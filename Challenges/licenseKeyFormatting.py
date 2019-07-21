"""
You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.

Given a non-empty string S and a number K, format the string according to the rules described above.

Example 1:
Input: S = "5F3Z-2e-9-w", K = 4

Output: "5F3Z-2E9W"

Explanation: The string S has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
Example 2:
Input: S = "2-5g-3-J", K = 2

Output: "2-5G-3J"

Explanation: The string S has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
Note:
The length of string S will not exceed 12,000, and K is a positive integer.
String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
String S is non-empty.
"""
"""
Time: O(N)
Space: O(N)
"""
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        if not S:
            return S
        
        S = ''.join(S.split('-'))
        
        i = len(S)-1
        count = 0
        res = ''
        while i >= 0:
            if count != 0 and not count%K:
                res = '-' + res
            res = S[i].upper() + res
            i-= 1
            count += 1
        return res



# Regex version
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        formatted = S.replace("-","",len(S)).upper()[::-1]
        formatted = re.sub(r'(\w{' + str(K) + r'})', r'\1-', formatted)
        formatted = formatted[::-1]
        formatted = re.sub(r'^-',r'', formatted)
        return formatted


def licenseKeyFormatting(S, K):
    # Convert all to upper case first
    S = S.upper()

    temp = ""

    pos = 0
    for i in range(len(S)-1, -1, -1):
        if S[i] != "-":
            if pos and not pos%K:
                temp = "-"+temp
            temp = S[i]+temp
            pos += 1

    return temp

class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace('-', '')[::-1]
        S = ''.join(map(lambda x: x.upper(), S))
        return '-'.join(reversed([S[i:i+K][::-1] for i in range(0, len(S), K)]))
S = "5F3Z-2e-9-w"
K = 4



print(licenseKeyFormatting(S, K))

S = "2-5g-3-J"
K = 2
print(licenseKeyFormatting(S, K))

S = "2Ac-5g-3-J"
K = 3
print(licenseKeyFormatting(S, K))
