"""
Given a coke machine with a series of buttons. If you press a button it will get you a certain range of coke. Find out if it's possible to get the target range of coke. You can press buttons any number of times.

Example 1:

Input: buttons = [[100, 120], [200, 240], [400, 410]], target = [100, 110]
Output: false
Explanation: if we press first button it might give us 120 volume of coke, not in the target range.
Example 2:

Input: buttons = [[100, 120], [200, 240], [400, 410]], target = [90, 120]
Output: true
Explanation: press first button and you will always get amount of coke in the target range.
Example 3:

Input: buttons = [[100, 120], [200, 240], [400, 410]], target = [300, 360]
Output: true
Explanation: press first and second button and you will always get amount of coke in the target range.
Example 4:

Input: buttons = [[100, 120], [200, 240], [400, 410]], target = [310, 360]
Output: false
Explanation: we can press 1st button 3 times or 1st and 2nd button but it's possible to get only 300, not in the target range.
Example 5:

Input: buttons = [[100, 120], [200, 240], [400, 410]], target = [1, 9999999999]
Output: true
Explanation: you can press any button.
"""

def coke_machine(buttons, target):
    level = set(tuple(button) for button in buttons)
    memo = level
    while level:
        next_level = set()
        for potential_sol in level:
            memo.add(potential_sol)
            if potential_sol[0] >= target[0] and potential_sol[1] <= target[1]:
                return True
            for button in buttons:
                potential_next_sol = (potential_sol[0] + button[0],
                                      potential_sol[1] + button[1])
                if potential_next_sol[1] <= target[1] and potential_next_sol not in memo:
                    next_level.add(potential_next_sol)
        level = next_level
    return False
