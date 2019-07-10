class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = set([n for n in range(1, len(nums)+1)])
        for n in nums:
            if n in res:
                res.remove(n)
        return list(res)
	
	"""
	Below is java version of O(n) with no extra space
	"""

class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> result = new ArrayList<Integer>();
        if(nums==null || nums.length==0) return result;
        for(int i=0; i<nums.length; i++) {
            int index = Math.abs(nums[i])-1;
            if(nums[index]<0) continue;
            nums[index] = -nums[index];
        }
        for(int i=0; i<nums.length; i++) {
            if(nums[i]>0) {
                result.add(i+1);
            }
        }
        return result;
    }
}


    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = [0] + nums
        for i in range(len(nums)):
            index = abs(nums[i])
            nums[index] = -abs(nums[index])

        return [i for i in range(len(nums)) if nums[i] > 0]
