'''
Minimum Difference Between Largest and Smallest Value in Three Moves
Medium

618

79

Add to List

Share
Given an array nums, you are allowed to choose one element of nums and change it by any value in one move.

Return the minimum difference between the largest and smallest value of nums after perfoming at most 3 moves.

 

Example 1:

Input: nums = [5,3,2,4]
Output: 0
Explanation: Change the array [5,3,2,4] to [2,2,2,2].
The difference between the maximum and minimum is 2-2 = 0.
Example 2:

Input: nums = [1,5,0,10,14]
Output: 1
Explanation: Change the array [1,5,0,10,14] to [1,1,0,1,1]. 
The difference between the maximum and minimum is 1-0 = 1.
Example 3:

Input: nums = [6,6,0,1,1,4,6]
Output: 2
Example 4:

Input: nums = [1,5,6,14,15]
Output: 1
 

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9

'''

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        '''
        First, we eliminate the simple case of arrays with less than 5 elements. If an array has less than 5 elements, we can change all the elements to match. For example [1,2,3,4] could be changed to [1,1,1,1]. Thus any array with less than 5 elements will always return 0.

Next, we sort the array. With a sorted array, there are 4 distinct solution possibliltes.

The three highest numbers need to be changed changed. An example of this would be [2,3,4,35,46,78,88]. Assuming we remove the 3 highest, the solution of our minimum will be the 4th highest minus the lowest. In the code below, this is expressed as nums[l-4] - nums[0]
The second use case is elminating two high numbers and one low number. An example would be [1,33,34,35,65,67]. In this case, we change the two highest and the lowest, meaning we subtract the 3rd largest number from the second smallest number: nums[l-3] - nums[1
Th third case is removing the highest number and the two smallest numbers. Ex. [1,2,33,34,35,71]. Expressed as nums[l-2]-nums[2]
Finally, the fourth case involves elminating the three smallest numbers. Ex. [1,2,3,96,97,98,99]. Expressed as nums[l-1]-nums[3]

        '''
        l = len(nums)
        if l < 5:
            return 0
        nums.sort()
        
        return min(nums[l-4]-nums[0], nums[l-3]-nums[1], nums[l-2]-nums[2], nums[l-1]-nums[3])
