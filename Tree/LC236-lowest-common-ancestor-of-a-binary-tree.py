# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ancestor = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        check1 = set()
        check2 = set()
        def dfs(root):
            if root == None:
                return
            if root == p:
                check1.add(root)
            if root == q:
                check2.add(root)
            dfs(root.left)
            if root.left in check1:
                check1.add(root)
            if root.left in check2:
                check2.add(root)
            dfs(root.right)
            if root.right in check1:
                check1.add(root)
            if root.right in check2:
                check2.add(root)
            if root in check1 and root in check2:
                if self.ancestor == None:
                    self.ancestor = root
        dfs(root)
        return self.ancestor