# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue =  [root]
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
        return ans
            