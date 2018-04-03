class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        def radixSort(a):
            r = 10
            maxLen = 11
            for x in range(maxLen):
                bins = [[] for i in range(r+9)]
                for y in a:
                    if(y>=0):
                        bins[(y/10**x)%r+9].append(y)
                    else:
                        bins[(y/10**x)%r].append(y)
                a=[]
                for section in bins:
                    a.extend(section)
            return a
        rex = []
        for i in nums:
            rex.append(a*(i**2) + (b * i) + c)
        rex = radixSort(rex)
        return rex