"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = [root]
        while len(queue) != 0:
            cur_level = []
            next_level = []
            while len(queue) != 0:
                node = queue.pop(0)
                if node != None:
                    cur_level.append(node)
                    next_level.append(node.left)
                    next_level.append(node.right)
            cur_level.append(None)
            for i in range(len(cur_level)-1):
                cur_level[i].next = cur_level[i+1]
            queue = next_level[:]
        return root
            