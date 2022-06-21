/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int maximum = -Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        helper(root);
        return maximum;
    }
    
    private int helper(TreeNode root) {
        if (root == null) return 0;
        int cur = root.val;
        int left = Math.max(0, helper(root.left));
        int right = Math.max(0, helper(root.right));
        maximum = Math.max(maximum, left + right + cur);
        return Math.max(left, right) + cur;
    }
}