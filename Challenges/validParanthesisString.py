"""
Valid Paranthesis String

Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].
"""

"""
Intuition

When checking whether the string is valid, we only cared about the "balance": the number of extra, open left brackets as we parsed through the string. For example, when checking whether '(()())' is valid, we had a balance of 1, 2, 1, 2, 1, 0 as we parse through the string: '(' has 1 left bracket, '((' has 2, '(()' has 1, and so on. This means that after parsing the first i symbols, (which may include asterisks,) we only need to keep track of what the balance could be.

For example, if we have string '(***)', then as we parse each symbol, the set of possible values for the balance is [1] for '('; [0, 1, 2] for '(*'; [0, 1, 2, 3] for '(**'; [0, 1, 2, 3, 4] for '(***', and [0, 1, 2, 3] for '(***)'.

Furthermore, we can prove these states always form a contiguous interval. Thus, we only need to know the left and right bounds of this interval. That is, we would keep those intermediate states described above as [lo, hi] = [1, 1], [0, 2], [0, 3], [0, 4], [0, 3].

Algorithm

Let lo, hi respectively be the smallest and largest possible number of open left brackets after processing the current character in the string.

If we encounter a left bracket (c == '('), then lo++, otherwise we could write a right bracket, so lo--. If we encounter what can be a left bracket (c != ')'), then hi++, otherwise we must write a right bracket, so hi--. If hi < 0, then the current prefix can't be made valid no matter what our choices are. Also, we can never have less than 0 open left brackets. At the end, we should check that we can have exactly 0 open left brackets.
"""

"""
Greedy

Time Complexity: O(N), where NN is the length of the string. We iterate through the string once.

Space Complexity: O(1)

Let diff be count of left parenthesis minus count of right parenthesis.

When we meet:

(, we increment diff.
), we decrement diff.
*, we have three choices which makes the diff become a range -- [diff - 1, diff + 1].
So we use maxDiff/minDiff to record the maximum/minimum diff we can get.

When we meet:

(, ++maxDiff and ++minDiff.
), --maxDiff and --minDiff.
*, ++maxDiff and --minDiff.
If maxDiff become negative, it means it's already invalid, we should return false.

Whenever minDiff falls below 0, we should force it to be 0 because we never accept negative diff during the process.

After scanning through string s, as long as minDiff is 0, this string can be a valid one.
"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True
        
        l, r = 0, 0
        for c in s:
            if c == '(':
                l += 1
            else:
                l -= 1
            if c != ')':
                r += 1
            else:
                r -= 1
            if r < 0:
                break
            l = max(l, 0)
        return l == 0

