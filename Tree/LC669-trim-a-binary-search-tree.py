# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def dfs(root):
            if root == None:
                return None
            root.left = dfs(root.left)
            if root.val < low:
                return dfs(root.right)
            root.right = dfs(root.right)
            if root.val > high:
                return dfs(root.left)
            return root
        return dfs(root)