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


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        closing = {'}': '{', ']': '[', ')': '('}
        stack = []
        for b in s:
            if b not in closing:
                stack.append(b)
            else:
                if not stack:
                    return False
                opening = stack.pop()
                if closing[b] != opening:
                    return False
        return False if stack else True
