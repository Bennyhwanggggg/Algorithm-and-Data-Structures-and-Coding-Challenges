/**
Given an array, rotate the array to the right by k steps, where k is non-negative.

Algorithm

We use an extra array in which we place every element of the array at its correct position i.e. the number at index ii in the original array is placed at the index (i+k)%(length of array)(i+k). Then, we copy the new array to the original one.
**/

class Solution {
    public void rotate(int[] nums, int k) {
        int[] a = new int[nums.length];
        for (int i=0; i<nums.length; i++) {
            a[(i+k)%nums.length] = nums[i];
        }
        for (int i=0; i<nums.length; i++) {
            nums[i] = a[i];
        }
    }
}
