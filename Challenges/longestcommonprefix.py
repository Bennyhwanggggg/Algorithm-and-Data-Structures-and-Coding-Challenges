class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        minlen = min([len(s) for s in strs])
        res = ''
        for i in range(minlen):
            test = strs[0][i]
            if all([test == string[i] for string in strs]):
                res += test
            else:
                break
        return res
