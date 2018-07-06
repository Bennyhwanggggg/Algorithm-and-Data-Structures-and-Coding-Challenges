class Solution {
    public int arrayPairSum(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);
        int sum = 0;
        for(int i=0; i<n/2; i++){
            sum+=Math.min(nums[2*i], nums[(2*i)+1]);
        }
        return sum;
    }
}