# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-53216351, head)
        dummy.next = ListNode(head.val, None)
        head = head.next
        while head != None:
            p = dummy
            q = p.next
            while q != None and q.val < head.val:
                p = p.next
                q = q.next
            p.next = ListNode(head.val, q)
            head = head.next
        return dummy.next