def deletion_distance(str1, str2):
    if str1 == str2:
        return 0
    if not len(str1):
        return len(str2)
    if not len(str2):
        return len(str1)

    dp = [0] * (len(str2) + 1)
    for c1 in str1:
        newdp = dp[:]
        for i, c2 in enumerate(str2):
            if c1 == c2:
                newdp[i + 1] = 1 + dp[i]
            else:
                newdp[i + 1] = max(dp[i + 1], newdp[i])
        dp = newdp
    return len(str1) + len(str2) - dp[-1] * 2


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        if not m and not n:
            return 0
        elif not m:
            return n
        elif not n:
            return m
        memo = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if not i:
                    memo[i][j] = j
                elif not j:
                    memo[i][j] = i
                elif word1[i - 1] == word2[j - 1]:
                    memo[i][j] = memo[i - 1][j - 1]
                else:
                    memo[i][j] = 1 + min(memo[i - 1][j], memo[i][j - 1])
        return memo[m][n]

def deletion_distance(str1, str2):
  if not str1:
    return len(str2)
  if not str2:
    return len(str1)
  if str1[len(str1)- 1] == str2[len(str2)-1]:
    return deletion_distance(str1[:-1], str2[:-1])
  else:
    return 1 + min(deletion_distance(str1[:-1], str2), deletion_distance(str1, str2[:-1]))