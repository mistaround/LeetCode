"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        ans = Node(head.val)
        p = head
        q = ans
        PQmap = {}
        while p != None:
            PQmap[p] = q
            p = p.next
            if p != None:
                q.next = Node(p.val)
                q = q.next
            else:
                q.next = None
            
        p = head
        q = ans
        while p != None:
            if p.random == None:
                q.random = None
            else:
                q.random = PQmap[p.random]
            p = p.next
            q = q.next
        return ans
        