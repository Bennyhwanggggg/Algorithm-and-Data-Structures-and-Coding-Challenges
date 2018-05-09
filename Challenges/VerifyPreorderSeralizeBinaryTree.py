class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        count = 1

        if preorder.split(',')[0] == '#' and preorder != '#':
            return False
        if preorder == '#':
            return True
        for pos, val in enumerate(preorder.split(',')):
            count -= 1
            if count < 0:
                return False
            if val != '#':
                count += 2
            print(val, count)
        return count == 0