'''
Written by Benny Hwang 11/09/2017
 Say that two strings s_1 and s_2 can be merged into a third
 string s_3 if s_3 is obtained from s_1 by inserting
 arbitrarily in s_1 the characters in s_2, respecting their
 order. For instance, the two strings ab and cd can be merged
 into abcd, or cabd, or cdab, or acbd, or acdb..., but not into
 adbc nor into cbda.

 Prompts the user for 3 strings and displays the output as follows:
 - If no string can be obtained from the other two by merging,
 then the program outputs that there is no solution.
 - Otherwise, the program outputs which of the strings can be obtained
 from the other two by merging.
'''

# We know that string3 is our longer string
def can_merge(string_1, string_2, string_3):
    # if string_1 doesn't contain anything and string_2 is the same as string_3
    if not string_1 and string_2 == string_3:
        return True
    # if string_2 doesn't contain anything and string_1 is the same as string_3
    if not string_2 and string_1 == string_3:
        return True
    # if we have already emptied out everything in string 1 and string 2,
    # and no matcch with string 3 is found, then return false
    if not string_1 or not string_2:
        return False
    # If the first letter in string1 and string 3 is the same, put the remaining strings into can_merge recursively
    # This works since the order which the letters occur inside the strings are respected
    # The recursive call will keep removing the first letter until empty
    if string_1[0] == string_3[0] and can_merge(string_1[1: ], string_2, string_3[1: ]):
        return True
    # Same as the if above but with different combination
    if string_2[0] == string_3[0] and can_merge(string_1, string_2[1: ], string_3[1: ]):
        return True
    # Return false if true is not returned in any of the if statement before
    return False

    

ranks = ['first', 'second', 'third']
string_1 = input('Please input the first string: ')
string_2 = input('Please input the second string: ')
string_3 = input('Please input the third string: ')

strings = [string_1, string_2, string_3]

# Order the strings by their length. This is because only the two shorter strings can be merged into the longer one
# Initialize by setting string_1 as the last string
last = 0
# If the second string is longer than the first string, put it as last
if len(strings[1]) > len(strings[0]):
    last = 1
# If the third string is lnger than the current last string, set it to last
if len(strings[2]) > len(strings[last]):
    last = 2
# If the last string is the first string, set first and second as the string_2 and string_3
if last == 0:
    first, second = 1, 2
# If the last string is the second string, set first and second as the string_1 and string_3
elif last == 1:
    first, second = 0, 2
else:
# If the last string is the third string, set first and second as the string_1 and string_2
    first, second = 0, 1

# If the length of the first two string does not equal to the last, it cannot be verged, otherwise if function returns False, it cannot be merged as well
if len(strings[last]) != len(strings[first]) + len(strings[second]) or\
                                      not can_merge(strings[first], strings[second], strings[last]):
    print('No solution')
else:
    print(('The {} string can be obtained by merging the other two.').format(ranks[last]))


