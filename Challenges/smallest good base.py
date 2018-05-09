# https://leetcode.com/problems/smallest-good-base/discuss/96587/Python-solution-with-detailed-mathematical-explanation-and-derivation

import math


class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        n = int(n)
        max_m = int(math.log(n, 2))  # Refer [7]
        for m in range(max_m, 1, -1):
            k = int(n ** m ** -1)  # Refer [6]
            if (k ** (m + 1) - 1) // (k - 1) == n:
                # Refer [3]
                return str(k)

        return str(n - 1)

    import math
    class Solution:
        def smallestGoodBase(self, n):
            """
            :type n: str
            :rtype: str
            """

            # Naive solution
            # def checkBase(base, n):
            #     current = 1
            #     while current < n:
            #         current = current * base + 1
            #     return current == n
            # num = int(n)
            # for i in range(2, num):
            #     if checkBase(i, num):
            #         return str(i)
            # return str(num-1)

            # Better solution
            def getAnsofBase(length, base):
                '''
                Convert 11...11 (base 'base')
                '''
                ans = 1
                for i in range(length - 1):
                    ans = ans * base + 1
                return ans

            def findLengthBase(length, n):
                '''
                Check whether there exist a base such that n in base 'base' == 111...111 (length's 1s)
                '''
                start, end = 0, n // 2
                while start <= end:
                    mid = (start + end) // 2
                    target = getAnsofBase(length, mid)
                    if target == n:
                        return mid
                    elif target < n:
                        start = mid + 1
                    else:
                        end = mid - 1
                return -1

            num = int(n)
            length = int(math.log(num, 2)) + 1
            while length > 2:
                retVal = findLengthBase(length, num)
                if retVal != -1:
                    return str(retVal)
                length -= 1
            return str(num - 1)