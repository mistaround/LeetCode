# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    found = False
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def inorder_search(root, s):
            if root == None:
                return
            inorder_search(root.left, s)
            if target - root.val in s:
                self.found = True
                return
            inorder_search(root.right, s)
            
        def inorder_traversal(root, s):
            if root == None:
                return
            inorder_traversal(root.left, s)
            s.add(root.val)
            inorder_traversal(root.right, s)
        
        set1 = set()
        inorder_traversal(root1, set1)
        inorder_search(root2, set1)
        return self.found