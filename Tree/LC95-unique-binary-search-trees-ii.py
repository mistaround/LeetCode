# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate_subtrees(start, end):
            if start > end:
                return [None]
            
            subtrees = []
            for i in range(start, end+1):
                left_trees = generate_subtrees(start, i-1)
                right_trees = generate_subtrees(i+1, end)
                
                for l in left_trees:
                    for r in right_trees:
                        cur = TreeNode(i, l, r)
                        subtrees.append(cur)
            return subtrees
        
        return generate_subtrees(1,n) if n else []