# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = [root]
        
        def compare(root, sub):
            if (root == None and sub != None) or (root != None and sub == None):
                return False
            if root == None and sub == None:
                return True
            res = (root.val == sub.val)
            return (res and compare(root.left, sub.left) and compare(root.right, sub.right))
        
        while queue:
            p = subRoot
            while queue:
                cur = queue.pop(0)
                if cur.val == p.val:
                    if compare(cur, p):
                        return True
                if cur.left != None:
                    queue.append(cur.left)
                if cur.right != None:
                    queue.append(cur.right)
        
        return False