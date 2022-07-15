# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseNode(root, link):
            c = k
            p = root
            while p != None and c != 0:
                p = p.next
                c -= 1
            if c != 0:
                if link:
                    link.next = root
                return root
            c = k
            prev = root
            p = root
            while c != 0:
                if c == k:
                    p = p.next
                else:
                    next = p.next
                    p.next = prev
                    prev = p
                    p = next
                c -= 1
                if c == 0:
                    root.next = p
                    if link:
                        link.next = prev
                    return prev
        
        ans = None
        prev = None
        p = head
        while True:
            res = reverseNode(p, prev)
            if ans == None:
                ans = res
            if res == p:
                return ans
            prev = p
            p = p.next

        return ans