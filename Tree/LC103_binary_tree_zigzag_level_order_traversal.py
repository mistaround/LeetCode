# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Definition for a binary tree node.
        ans = []
        queue =  [root]
        count = 1
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
                if count % 2 == 0:
                    tmp.reverse()
                ans.append(tmp)
            count += 1
        return ans
            
            