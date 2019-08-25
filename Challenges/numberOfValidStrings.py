"""
Given an int n, output number of valid strings of length n consisting of letters A, B and C. Any continuous three letters containing all three letters A, B, C make the whole string invalid. For example, BACCA is not a valid string because of the first three characters, but CCCACCAABBB is a valid string.

Example 1:

Input: n = 0
Output: 0
Example 2:

Input: n = 1
Output: 3
Explanation: A, B, C
Example 3:

Input: n = 2
Output: 9
Explanation: AA, AB, AC, BA, BB, BC, CA, CB, CC
Example 4:

Input: n = 3
Output: 21
Explanation: 3^3 - 6 (ABC, ACB, BAC, BCA, CBA, CAB)
Example 5:

Input: n = 4
Output: 51
"""

"""
// from manually working out examples for n = 2, 3, and 4:
    // n = 2 gives us (3)*3 valid strings
    // ([AA AB AC] [BB BC BA] [CC CA CB])
    // n = 3 gives us (3+2+2)*3 valid strings
    // ([AAA AAB AAC][ABB ABA][ACC ACA] * 3)
    // n = 4 gives us ((3+2+2)+(3+2)+(3+2))*3 valid strings
    // the pattern is that each 3 from the previous equation
    // expands into (3+2+2), and each 2 expands into (3+2)

    // this can be modeled as the accumulation of two variables
    // so the number of 3s becomes the previous number of 3s
    // plus the previous number of 2s, while the 2s grow similarly
    // (number of 2s plus number of 3s * 2)

    // start with (3)*3 and n = 2
    // after 1 iteration it will have (3+2+2)*3, and so forth
"""
"""
First step for these explosive growth types of problems is to reduce the number of possible combinations for my poor brain.

A first attempt at length 2 might be [AA AB AC] [BA BB BC] [CA CB CC], but reordering it to be [AA AB AC] [BB BC BA] [CC CA CB] lets us think about each group as a letter followed by +0, +1, and +2 letters to the right (A -> B -> C -> A -> B). All three groups follow this pattern so we only need to think about the first group and can multiply the final answer by 3.

To expand to length 3, we can either add a letter to the start or the end. e.g. AA can become BAA or AAB. Thing is, adding a B before AA is the same as adding an A to BA, and the same holds true for all other cases of adding a letter to the start, so let's only ever add letters to the end of a group to expand them.

So we have AA AB AC from the second interval and need to expand each of them with an additional character to the end, then multiply that result by 3 to solve for the identical B and C groups. AB and AC can only be expanded twice each since AB[C] and AC[B] are invalid, but AA can expand with all three letters. That gives us (2+2+3)*3 = 21.

From there, we note that the last two letters of each group become the next string to expand (e.g. AAA expands using the rules for AA above, ABB expands using the rules for BB above which are identical to the rules for AA, etc.), and can simply repeat this process for each next length. Will try to devise an O(1) algorithm in a bit.
"""

def numValidStrings(n):
	if n == 0:
		return 0
	if n == 1:
		return 3
	count3 = 1
	count2 = 0
	for i in range(2, n):
		temp = count3 + count2
		count2 = count3*2 + count2
		count3 = temp
	return (count3 * 3 + count2 * 2) * 3

if __name__ == '__main__':
	assert numValidStrings(3) == 21
	assert numValidStrings(4) == 51


