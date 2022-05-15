# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        mid = self.split(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
    
    def split(self, node):
        prev, result, later = node, node, node
        while later != None and later.next != None:
            prev = result
            result = result.next
            later = later.next.next
        prev.next = None
        return result
    
    def merge(self, left, right):
        dummy = ListNode()
        p = dummy
        while left != None and right != None:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        if left == None:
            p.next = right
        else:
            p.next = left
        return dummy.next