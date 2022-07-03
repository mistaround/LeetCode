# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = [[-1 for _ in range(n)] for _ in range(m)]
        times = 0
        direction = "right"
        p = head
        i, j = 0, 0
        while p != None:
            if i == -1 or i == m or j == -1 or j == n or ans[i][j] != -1:
                times += 1
                if times % 4 == 1:
                    direction = "down"
                    j -= 1
                    i += 1
                if times % 4 == 2:
                    direction = "left"
                    i -= 1
                    j -= 1
                if times % 4 == 3:
                    direction = "up"
                    j += 1
                    i -= 1
                if times % 4 == 0:
                    direction = "right"
                    i += 1
                    j += 1
                    
            ans[i][j] = p.val
            
            if direction == "right":
                j += 1
            if direction == "down":
                i += 1
            if direction == "left":
                j -= 1
            if direction == "up":
                i -= 1
                
            p = p.next
            
        return ans