"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
"""

class Solution:
    def decodeString(self, s: str) -> str:
        """
        Start decoding from each most inner square bracket
        """
        stack = []
        
        for character in s:
            if character == ']':
                n, string = '', ''
                while stack[-1] != '[': # every most inner bracket will be enclosed, so pop the characters inside it
                    string = stack.pop() + string
                
                stack.pop() # get rid of '['
                
                # the square bracket will then have a leading digit
                while stack and stack[-1].isdigit():
                    n = stack.pop() + n
                
                # add back to the stack to decode and expand
                stack.append(int(n)*string)
            else:
                stack.append(character)
        return ''.join(stack)
                
