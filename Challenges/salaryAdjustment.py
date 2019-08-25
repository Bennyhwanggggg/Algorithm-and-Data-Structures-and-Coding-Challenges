"""
Give an array of salaries. The total salary has a budget. At the beginning, the total salary of employees is larger than the budget. It is required to find the number k, and reduce all the salaries larger than k to k, such that the total salary is exactly equal to the budget.

Example 1:

Input: salaries = [100, 300, 200, 400], budget = 800
Output: 250
Explanation: k should be 250, so the total salary after the reduction 100 + 250 + 200 + 250 is exactly equal to 800.
You can assume that solution always exists.
"""

def budgetize(sals, budget):
    i = len(sals) - 1
    count = 1 # counts how many high salaries we are converting to k
    while i >= 0:
        # sort salaries so you can cherrypick highest sals and start replacing them with k
        sorted_sals = sorted(sals)
        # find the sum of all the salaries except the highest one(s)
        # as i decreases, this array will reduce in size i.e. we will exclude highest and second highest sal in
        # next iteration, then highest , second highest and third highest in next and so on..
        sum_of_sals_excluding_highest = sum(sorted_sals[:i])
        # find k by substracting this sum from the budget..
        k = (budget - sum_of_sals_excluding_highest)/count
        if max(sorted_sals[:i]) > k: # this means there are still salries higher than k...
            i -= 1 # reduce i to now convert the next highest salary..
            count += 1 # increase by one since now another high salary will be converted to k..
        else:
            return k

if __name__ == '__main__':
    assert budgetize([100,200,300,400], 800) == 250