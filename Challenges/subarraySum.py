"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

"""
Other approach, brute force O(n^3) by considering every possible subarray using a nested forloop

Antoerh is cumulative sum array and in order to calculate the sum of elements between two indices, we subtract the cumulative sum corresponding to the two indces to obtain the sum directly

public class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        int[] sum = new int[nums.length + 1];
        sum[0] = 0;
        for (int i = 1; i <= nums.length; i++)
            sum[i] = sum[i - 1] + nums[i - 1];
        for (int start = 0; start < nums.length; start++) {
            for (int end = start + 1; end <= nums.length; end++) {
                if (sum[end] - sum[start] == k)
                    count++;
            }
        }
        return count;
    }
}


public class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        for (int start = 0; start < nums.length; start++) {
            int sum=0;
            for (int end = start; end < nums.length; end++) {
                sum+=nums[end];
                if (sum == k)
                    count++;
            }
        }
        return count;
    }
}
"""

"""
Time: O(n)
Space: O(n)

if cumulative sum of two indices are the same, the sum of the elements between those indices is zero. Extending the same thought further, if the cumulative sum upto two indices, say ii and jj is at a difference of kk i.e. if sum[i] - sum[j] = ksum[i]−sum[j]=k, the sum of elements lying between indices i and j is k.

Based on these thoughts, we make use of a hashmap mapmap which is used to store the cumulative sum upto all the indices possible along with the number of times the same sum occurs
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, currSum = 0, 0
        seen = dict()
        seen[0] = 1
        for n in nums:
            currSum += n
            if currSum - k in seen:
                count += seen[currSum-k]
            if currSum not in seen:
                seen[currSum] = 0
            seen[currSum] += 1
        return count
                

"""
Keep a count of the number of previous prefix sums and so on every new sum, we check if we have seen
the value before and the number of times that value occured. this tells us there are that number of 
subarrays that made up that sum.
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, sum = 0, 0
        sum_map = {0: 1}
        for n in nums:
            sum += n
            if sum-k in sum_map.keys():
                count += sum_map[sum-k]
            if sum in sum_map.keys():
                sum_map[sum] += 1
            else:
                sum_map[sum] = 1
        return count

public class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        for (int start = 0; start < nums.length; start++) {
            int sum=0;
            for (int end = start; end < nums.length; end++) {
                sum+=nums[end];
                if (sum == k)
                    count++;
            }
        }
        return count;
    }
}
