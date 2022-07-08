# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if root.left == None and root.right == None:
            return root.val
        def dfs(root, prev):
            if root == None:
                return
            if root.left == None and root.right == None:
                self.ans += int(prev + str(root.val), 2)
                return
            val = prev + str(root.val)
            dfs(root.left, val)
            dfs(root.right, val)
        dfs(root, "")
        return self.ans