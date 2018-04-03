class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        pushable = '({['
        popable = ')}]'
        brackets = {'(': ')', '{': '}', '[': ']'}

        for c in s:
            if c in pushable:
                stack.append(c)
            elif c in popable:
                if not len(stack):
                    return False
                else:
                    top = stack.pop()
                    if brackets[top] != c:
                        return False
            else:
                return False

        if len(stack):
            return False
        return True
