"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""
# function int[] grep(string haystack, string needle)
# haystack = "aaabcdddbbddddabcdefghi"
# needle = "abc"       abcde
# [2,14]

# (ord('a')*256+ord('a') )*256 + ord('b')
# For O(N) update the comparison function to use ord hash

def grep(haystack, needle):
    res = []
    if len(needle) > len(haystack):
        return res
    if needle == '':
        return res
    for i in range(len(haystack)-len(needle)+1): # 5-2 = 3
        if checkSame(haystack, i, needle):
            res.append(i)
    return res


def checkSame(a, start, b):  # start = 3
    i = 0
    while i < len(b):
        if a[start+i] != b[i]: 
            return False
        i += 1
    return True

print(grep("aaabcdddbbddddabcdefghi", "abc"))
print(grep("abcde", "de"))
print(grep("abcde", "gde"))
print(grep("abcde", "gasdfade"))
print(grep("abcde", "ab"))
print(grep("aaaaa", "aa"))
print(grep("aaaaa", "a"))
print(grep("aaaaa", ""))
print(grep("", "aa"))
