O(N) Time

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack=[None]
        balance=0
        for p in S:
            if p=='(':
                stack.append('(')
                
            elif stack[-1]=='(':
                stack.pop()
            else:
                balance+=1
        return len(stack)-1+balance
O(1) Time

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        balance=0
		extra=0
        for p in S:
            if p=='(':
                balance+=1
			else:
				balance-=1
			if balacne==-1:
				balance+=1
				extra+=1
		return balance+extra
