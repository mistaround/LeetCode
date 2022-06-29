# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node, prev):
            if node == None:
                return prev
            next = node.next
            node.next = prev
            return helper(next, node)
            
        return helper(head, None)
                