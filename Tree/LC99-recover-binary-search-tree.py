# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    node1, node2 = None, None
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(root, arr):
            if root == None:
                return
            inorder(root.left, arr)
            arr.append(root.val)
            inorder(root.right, arr)
            
        def find_swap(arr):
            x, y = None, None
            for i in range(len(arr)-1):
                if arr[i+1] < arr[i]:
                    y = arr[i+1]
                    if x == None:
                        x = arr[i]
                    else:
                        break
            return x, y
        
        def find_traversal(root, x, y):
            if self.node1 != None and self.node2 != None:
                return
            if root == None:
                return
            if root.val == x:
                self.node1 = root
            if root.val == y:
                self.node2 = root
            find_traversal(root.left, x, y)
            find_traversal(root.right, x, y)
        
        arr = []
        inorder(root, arr)
        x, y = find_swap(arr)
        find_traversal(root, x, y)
        self.node1.val, self.node2.val = self.node2.val, self.node1.val
        