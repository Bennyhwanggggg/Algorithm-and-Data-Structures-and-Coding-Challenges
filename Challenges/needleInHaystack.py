# function int[] grep(string haystack, string needle)
# haystack = "aaabcdddbbddddabcdefghi"
# needle = "abc"       abcde
# [2,14]

# (ord('a')*256+ord('a') )*256 + ord('b')


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