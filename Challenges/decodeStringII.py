"""
Given an encoded string in form of "ab[cd]{2}def"
You have to return decoded string "abcdcddef"

Notice that if there is a number inside curly braces, then it means preceding string in square brackets has to be repeated the same number of times. It becomes tricky where you have nested braces.

Example 1:

Input: "ab[cd]{2}"
Output: "abcdcd"
Example 2:

Input: "def[ab[cd]{2}]{3}ghi"
Output: "defabcdcdabcdcdabcdcdghi"
"""


class Solution:
	def decodeString(self, s):
		stack = []
		    i=0
    while i< len(s):
        if s[i]=='[':
            stack.append(s[i])
        elif s[i]==']':
            temp = ''
            while stack[len(stack)-1]!='[':
                temp = stack.pop() + temp
            stack.pop()
            stack.append(temp)
            
        elif s[i]=='{':
            i+=1
            val=''
            while i<len(s) and s[i]!='}':
                val+=s[i]
                i+=1
            pre = stack.pop()
            stack.append(pre*int(val)) .  #notice int conversion directly without multiplying by 10 for each digit. this looks handy
        else:
            stack.append(s[i])
        i+=1
        
    return ''.join(stack) . # make use of join to print out elements sequentially as a string
