class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        To calculate 
        number of trailing zeros w/o the need to first calculate 
        the factorial, use this understanding: the number of 
        trailing zeros can be derived by "summing how many 
        fives and powers of five are in the input 'n'.  Ex.
        num_of_zeros = n//5 + n//5^2 + n//5^3 + n//5^N ... break when 5^N < n (the input)
        4! => 0 
        5! => 1 
        10! => 2
        24! => 4
        25! => 5 + 1
        50! => 10 + 2
        125! => 25 + 5 + 1
         ...
        """
        if n < 1:
            return 0
						
        num_zeros = 0
        pow_of_5 = 5
				
        while pow_of_5 <= n:
            num_zeros += n // pow_of_5
            pow_of_5 *= 5 
						
        return num_zeros