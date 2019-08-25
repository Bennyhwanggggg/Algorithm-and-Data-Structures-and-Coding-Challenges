"""
You are given a phone number as an array of n digits. To help you memorize the number, you want to divide it into groups of contiguous digits. Each group must contain exactly 2 or 3 digits. There are 3 kinds of groups:

Excellent: A group that contains only the same digits. For example, 000 or 77.
Good: A group of 3 digits, 2 of which are the same. For example, 030, 229 or 166.
Usual: A group in which all the digits are distinct. For example, 123 or 90.
The quality of a group assignment is defined as 2 × (number of excellent groups) + (number of good groups). Divide the phone number into groups such that the quality is maximized.
"""
def getQuality(nums, startIndex, groupLength):
    if startIndex + groupLength > len(nums):
        raise ValueError('startIndex + groupLength > len(nums)')
    if groupLength == 2:
        if nums[startIndex] == nums[startIndex+1]:
            return 2
        else:
            return 0
    elif groupLength == 3:
        if all(nums[i] == nums[i+1] for i in range(startIndex, startIndex + groupLength - 1)):
            return 2
        elif any(nums[i] == nums[j] for i in range(startIndex, startIndex + groupLength - 1) for j in range(i + 1, startIndex + groupLength)):
            return 1
        else:
            return 0
    else:
        raise ValueError('groupLength must equal 2 or 3')

def memorize(phoneNumber):
    # Returns the groups of a phone number such that the memorization quality is maximized.
    # Each group must contain exactly 2 or 3 digits. There are 3 kinds of groups:
    # Excellent: A group that contains only the same digits. For example, 000 or 77.
    # Good: A group of 3 digits, 2 of which are the same. For example, 030, 229 or 166.
    # Usual: A group in which all the digits are distinct. For example, 123 or 90.
    # The quality of a group assignment is defined as 2 × (number of excellent groups) + (number of good groups)
    # If the phone numbers were large or space was a concern we do not need to store whole array - just last three indexes
    if len(phoneNumber) < 3:
        return getQuality(phoneNumber, 0, len(phoneNumber)), [[n for n in phoneNumber]]
    maxQuality = [0 for num in phoneNumber]
    bestGroups = [None for num in phoneNumber]
    bestGroups[0] = [[phoneNumber[0]]]
    maxQuality[1] = getQuality(phoneNumber, 0, 2)
    bestGroups[1] = [[phoneNumber[i] for i in range(2)]]
    maxQuality[2] = getQuality(phoneNumber, 0, 3)
    bestGroups[2] = [[phoneNumber[i] for i in range(3)]]
    for i in range(3, len(phoneNumber)):
        firstOption = maxQuality[i-2] + getQuality(phoneNumber, i-1, 2)
        secondOption = maxQuality[i-3] + getQuality(phoneNumber, i-2, 3)
        if firstOption > secondOption:
            maxQuality[i] = firstOption
            bestGroups[i] = bestGroups[i-2] + [[phoneNumber[j] for j in range(i-1, i+1)]]
        else:
            maxQuality[i] = secondOption
            bestGroups[i] = bestGroups[i-3] + [[phoneNumber[j] for j in range(i-2, i+1)]]
    return maxQuality[len(phoneNumber) - 1], bestGroups[len(phoneNumber) - 1]

# https://leetcode.com/discuss/interview-question/363871/google-memorize-phone-number
from functools import lru_cache
def memorizePhoneNumber(s):
    n = len(s)
    score = lambda t: len(t) - len(set(t))
    
    # helper computes the largest score and the spliting indices of s[i:] 
    @lru_cache(n)
    def helper(i):
        val, bounds = (0, (n,)) if i == n else (-float('inf'), (n,))
        for step in [2, 3]:
            if i + step <= n:
                (v, b), r = helper(i + step), score(s[i:i + step])
                if r + v >= val:
                    val, bounds = r + v, (i,) + b
        return (val, bounds)
    
    val, bounds = helper(0)
    return ''.join([f'({s[i:j]})' for i, j in zip(bounds, bounds[1:])])

s = '1233445556'
print(s, '(12)(33)(445)(556)')
print(memorizePhoneNumber(s))

s = '12334455566'
print(s, '(12)(33)(44)(555)(66)')
print(memorizePhoneNumber(s))


if __name__ == '__main__':
    print(memorize([1,2,3,4,5,6,7,8]))
    print(memorize([3,3,3,0,0,2,1]))
    print(memorize('1233445556'))
    print(memorize('12334455566'))
    print(memorize('12'))
    print(memorize('122'))
      