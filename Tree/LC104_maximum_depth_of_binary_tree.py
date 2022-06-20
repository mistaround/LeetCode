# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = []
        queue =  [root]
        level = 1
        while len(queue) != 0:
            next = []
            tmp = []
            while len(queue) != 0:
                node = queue.pop(0)
                if node != None:
                    tmp.append(node.val)
                    next.append(node.left)
                    next.append(node.right)
            for n in next:
                queue.append(n)
            if len(tmp) != 0:
                ans.append(tmp)
        return len(ans)