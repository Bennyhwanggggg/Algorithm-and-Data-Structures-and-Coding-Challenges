"""
Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""

"""
Boyer Majority Voting with two candidates
Time: O(N)
Space: O(1)
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        res = []
        candidate1, candidate2 = nums[0], nums[0]
        candidate1_counter, candidate2_counter = 0, 0

        for num in nums:
            if num == candidate1:
                candidate1_counter += 1
            elif num == candidate2:
                candidate2_counter += 1
            elif candidate1_counter == 0:
                candidate1 = num
                candidate1_counter = 1
            elif candidate2_counter == 0:
                candidate2 = num
                candidate2_counter = 1
            else:
                candidate1_counter -= 1
                candidate2_counter -= 1

        cnt1, cnt2 = 0, 0
        for num in nums:
            if candidate1 == num:
                cnt1 += 1
            elif candidate2 == num:
                cnt2 += 1

        if cnt1 > (len(nums) // 3):
            res.append(candidate1)
        if cnt2 > (len(nums) // 3):
            res.append(candidate2)
        return res

