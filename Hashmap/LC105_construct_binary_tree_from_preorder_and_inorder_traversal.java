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
    HashMap<Integer, Integer> inorderIdx;
    int preIdx = 0;
    
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        inorderIdx = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            inorderIdx.put(inorder[i], i);
        }
        return helper(preorder, 0, preorder.length - 1);
    }
    
    private TreeNode helper(int[] preorder, int left, int right) {
        if (left > right) return null;
        
        int cur = preorder[preIdx];
        TreeNode root = new TreeNode(cur);
        preIdx ++;
        
        root.left = helper(preorder, left, inorderIdx.get(cur) - 1);
        root.right = helper(preorder, inorderIdx.get(cur) +  1, right);
        return root;
    }
}