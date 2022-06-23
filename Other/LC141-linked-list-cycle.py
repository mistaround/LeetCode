# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p, q = head, head
        while q != None and q.next != None:
            p = p.next
            q = q.next.next
            if p == q:
                return True
        return False