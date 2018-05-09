class Solution:
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        L = {}
        def minipay(needs, L):
            if str(needs) in L:
                return L[str(needs)]
            mp = 0
            for i in range(len(needs)):
                mp = mp + needs[i]*price[i]
            for i in range(len(special)):
                dontskip = True
                for j in range(len(needs)):
                    if needs[j] - special[i][j] < 0:
                        dontskip = False
                        break
                if dontskip:
                    leftneeds = []
                    for j in range(len(needs)):
                        leftneeds.append(needs[j] - special[i][j])
                    mp = min(mp, special[i][-1] + minipay(leftneeds, L))
            L[str(needs)] = mp
            return mp
        return minipay(needs, L)