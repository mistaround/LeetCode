class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Maintain a queue of k
        queue = []
        for num in nums:
            length = len(queue)
            if length == 0:
                queue.append(num)
                continue
            if length < k:
                i = 0
                while i < length and queue[i] >= num:
                    i += 1
                queue.insert(i, num)
            else:
                for i in range(k):
                    if queue[i] >= num:
                        continue
                    else:
                        queue.insert(i, num)
                        break
        return(queue[k-1])