/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

/**
Solution

Recursive Solution
The current solution is very simple. We make use of a function construct(nums, l, r), which returns the maximum binary tree consisting of numbers within the indices ll and rr in the given numsnums array(excluding the r^{th}rth element).

The algorithm consists of the following steps:

Start with the function call construct(nums, 0, n). Here, nn refers to the number of elements in the given numsnums array.

Find the index, max_imax
​	
 , of the largest element in the current range of indices (l:r-1)(l:r−1). Make this largest element, nums[max\_i]nums[max_i] as the local root node.

Determine the left child using construct(nums, l, max_i). Doing this recursively finds the largest element in the subarray left to the current largest element.

Similarly, determine the right child using construct(nums, max_i + 1, r).

Return the root node to the calling function.
**/
class Solution {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        return construct(nums, 0, nums.length);
    }
    
    public TreeNode construct(int[] nums, int l, int r) {
        if (l==r) {
            return null;
        }
        int max_index = maxInArray(nums, l, r);
        TreeNode root = new TreeNode(nums[max_index]);
        root.left = construct(nums, l, max_index);
        root.right = construct(nums, max_index+1, r);
        return root;
    }
    
    public int maxInArray(int[] nums, int l, int r) {
        int max_index = l;
        for (int i=l; i<r; i++) {
            if (nums[max_index] < nums[i]) {
                max_index = i;
            }
        }
        return max_index;
    }
}
