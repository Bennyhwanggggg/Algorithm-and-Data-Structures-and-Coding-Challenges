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
