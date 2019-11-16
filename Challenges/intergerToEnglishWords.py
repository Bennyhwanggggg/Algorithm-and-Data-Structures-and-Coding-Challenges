class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        units = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        tens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens1 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        
        
        def interpretNumber(num):
            if num < 10: # 0 - 9
                return units[num]
            elif num < 20: # 10 - 19
                return tens[num-10]
            elif num < 100: # 20 - 99
                div, mod = divmod(num, 10)
                if mod != 0:
                    return tens1[div-2] + " " + interpretNumber(mod)
                return tens1[div-2]
            elif num < 1000: # 100 - 999
                div, mod = divmod(num, 100)
                if mod != 0:
                    return interpretNumber(div) + " Hundred " + interpretNumber(mod)
                return interpretNumber(div) + " Hundred"
            elif num < 1000000: # 1,000 - 999,999
                div, mod = divmod(num, 1000)
                if mod != 0:
                    return interpretNumber(div) + " Thousand " + interpretNumber(mod)
                return interpretNumber(div) + " Thousand"
            elif num < 1000000000: # 1,000,000 - 999,999,999
                div, mod = divmod(num, 1000000)
                if mod != 0:
                    return interpretNumber(div) + " Million " + interpretNumber(mod)
                return interpretNumber(div) + " Million"
            else:
                div, mod = divmod(num, 1000000000)
                if mod != 0:
                    return interpretNumber(div) + " Billion " + interpretNumber(mod)
                return interpretNumber(div) + " Billion"

        return interpretNumber(num)


"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""
class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return 'Zero'
        q = collections.deque()
        while num:
            q.append(num%1000)
            num //= 1000
        suffix = ['', 'Thousand', 'Million', 'Billion', 'Trillion', 'Gazillion', 'Megamillion']
        suffixIndex = 0
        res = []
        while q:
            lowest = q.popleft()
            lowestString = self.getHundreds(lowest)
            if lowest:
                res.append(suffix[suffixIndex])
                print(lowestString)
                res += lowestString[::-1]
            suffixIndex += 1
        return ' '.join([e for e in res[::-1] if e])
        
        
    def getHundreds(self, n):
        """
        return the list for numbers less than a thousand
        """
        print(n)
        if n >= 100:
            return self.getHundreds(n//100) + ['Hundred'] + (self.getHundreds(n%100) if n%100 else [])
        if n > 20:
            tenths = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
            return [tenths[n//10]] + (self.getHundreds(n%10) if n%10 else [])
        
        n = 0 if n < 1 else n
        belowTwenty = {0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty'}
        return [belowTwenty[n]]
       
 
