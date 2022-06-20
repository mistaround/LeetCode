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
    int postIdx = 0;
    HashMap<Integer, Integer> inorderIdx = new HashMap<>();
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        int length = inorder.length;
        int[] inversedorder = new int[length];
        for (int i = 0; i < length; i ++) {
            inorderIdx.put(inorder[i], i);
            inversedorder[i] = postorder[length - i - 1];
        }
        return helper(inversedorder, 0 , length - 1);
    }
    
    private TreeNode helper(int[] inversedorder, int left, int right) {
        if (left > right) return null;
        
        int cur = inversedorder[postIdx];
        postIdx ++;
        TreeNode root = new TreeNode(cur);
        
        root.right = helper(inversedorder, inorderIdx.get(cur) + 1, right);
        root.left = helper(inversedorder, left, inorderIdx.get(cur) - 1);
        return root;
    }
}