class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        closing = {')': '(', ']': '[', '}': '{'}
        opening = {'(', '{', '['}
        stack = []
        for i in s:
            if i in opening:
                stack.append(i)
            elif i in closing.keys():
                if not stack:
                    return False
                else:
                    close = stack.pop()
                    if closing[i] != close:
                        return False
        if not stack:
            return True
        return False