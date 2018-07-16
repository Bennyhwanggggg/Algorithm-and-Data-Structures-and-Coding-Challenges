/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<Double> averageOfLevels(TreeNode root) {
        List<Double> result = new ArrayList<Double>();
        
        if (root == null){
            return result;
        }
        int currentLv = 1;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while(q.peek() != null){
            int size = q.size();
            Double sum = 0.0;
            for(int i=0; i<size; i++){
                TreeNode curr = q.poll();
                if (curr.left != null){
                    q.add(curr.left);
                }
                if (curr.right != null){
                    q.add(curr.right);
                }
                sum += curr.val;
            }
            result.add(sum/size);
        }
        return result;
    }
}