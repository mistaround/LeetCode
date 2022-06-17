# LeetCode

## Sorting (Python)
#### LC15 - 3 Sum 
https://leetcode.com/problems/3sum/
- Sort
- Loop with two pointers
- Skipping used nums

#### LC16 - 3 Sum Closest 
https://leetcode.com/problems/3sum-closest/
- Sort
- Loop with two pointers 
- Comparing based on abs(target - current) and abs(target - closet)

#### LC18 - 4 Sum 
https://leetcode.com/problems/4sum/
- Same as 3 Sum

#### LC33 - Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/
- Binary Search

#### LC34 - Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
- Binary Search

#### LC49 - Group Anagrams 
https://leetcode.com/problems/group-anagrams/
- Sort each string and store in hashmap to group them
- "".join(sorted(string))

#### LC56 - Merge Intervals
https://leetcode.com/problems/merge-intervals/
- Sort based on first element 
  - sorted(intervals, key=lambda intervals: intervals[0])
- Use a cache to update current merged interval
  - cache = [cache[0], max(cache[1], intervals[i][1])]

#### LC75 - Sort Colors
https://leetcode.com/problems/sort-colors/
- Three pointer
  - Make sure nums before zero are all 0
  - nums after two are all 2
  - thus 1 will be in the middle

#### LC88 - Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/
- Nothing special

#### LC147 - Insertion Sort List
https://leetcode.com/problems/insertion-sort-list/
- Just insertion sort on a linked list

#### LC148 - Sort List
https://leetcode.com/problems/sort-list/
- Merge sort of a linked list
  - Recursively split and merge left and right part

#### LC164 - Maximum Gap
https://leetcode.com/problems/maximum-gap/
- Linear time sort algorithm
  - Radix Sort

#### LC169 - Majority Element
https://leetcode.com/problems/majority-element/
- Use Counter
  - return Counter(nums).most_common(1)[0][0]

#### LC179 - Largest Number
https://leetcode.com/problems/largest-number/
- Sort
- Use comparator and greedy algorihtm
  - extend two num string a and b to same length
  - if int a' > int b' return 1 else -1
  - if int a' = int b', if int(a + b) > int(b + a) return 1 else -1
- Sort again, sorted(strings, key=cmp_to_key(comparator), reverse=True)

#### LC215 - Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/
- Maintain a queue of size k

#### LC217 - Contains Duplicate
https://leetcode.com/problems/contains-duplicate/
- Simple HashMap

#### LC220 - Contains Duplicate III
https://leetcode.com/problems/contains-duplicate-iii/\
```python:
def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        window = SortedList()
        for i in range(len(nums)):
            if i > k:
                window.remove(nums[i-k-1])
            idx1 = window.bisect_left(nums[i] - t)
            idx2 = window.bisect_right(nums[i] + t)
            
            if idx1 != idx2:
                return True
            window.add(nums[i])
            
        return False
```
- Use SortedList as sliding window
- Use interval of [num - t, num + t] to judge

#### LC229 - Majority Element II
https://leetcode.com/problems/majority-element-ii/
- Simple HashMap

#### LC242 - Valid Anagram
https://leetcode.com/problems/valid-anagram/
- Use two Counter and subtract, if all zero True

#### LC274 - H-Index
https://leetcode.com/problems/h-index/
- First remove all zeros
- Sort and Loop:
  - if length - i <= citations[i]:
        break
- return length - i

#### LC295 - Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/
- Use two heaps: minHeap maxHeap
- Maintain the two heap to make the top of the two heaps can make median

#### LC324 - Wiggle Sort II
https://leetcode.com/problems/wiggle-sort-ii/
- Sort
- Two pass, insert with stride of 1 each time

---
## Hash Table (Java)
#### LC1 - Two Sum
https://leetcode.com/problems/two-sum/
- Classical HashMap

#### LC3 - Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
- Use HashMap as sliding window
- ans = Math.max(ans, i - left);
- left = Math.max(left, window.get(cur) + 1);

#### LC17 - Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
- Recursive

#### LC30 - Substring with Concatenation of All Words
https://leetcode.com/problems/substring-with-concatenation-of-all-words/
- Two HashMap, one for wordsCount one for wordsFound
- Sliding window, loop each time across a wordLength
  - Need to judge whether the word in wordsCount and then whether there are excessed word...
- In a word, it's very complex and I think I can't handle it if it appears in an interview

#### LC36 - Valid Sudoku
https://leetcode.com/problems/valid-sudoku/
- Brute-force

#### LC38 - Count and Say
https://leetcode.com/problems/count-and-say/
- Recursive

#### LC41 - First Missing Positive
https://leetcode.com/problems/first-missing-positive/
- Discard num non-positive by making them larger than array size
- Loop i from 0 to len(num), make each num[i] indicates whether i+1 inside the array

#### LC42 - Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/
- Dynamic Programming
- Note that rain water is determined by min(maxLeft,maxRight)

#### LC73 - Set Matrix Zeroes
https://leetcode.com/problems/set-matrix-zeroes/
- First ignore zeros in first col and row, record whether need to fill them 
- Use zeros in first col and row to indicate whether to fill the row or col
- At last fill the first row and col

#### LC76 - Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/
- Two pointer sliding window and two hashmap
- When requirement is fulfilled, move left to smaller window
- To judge whether requirement is fulfilled, if the increment this time not exceed needed, one char matched. 

#### LC105 - Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
- Preorder traversal gives the information of root
- Inorder traversal gives theh information of left and right sub tree
- Step on by the index of preorder and recursively construct left and right subtree by inorder

#### LC106 - Construct Binary Tree from Inorder and Postorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
- Similar with LC105
- Postorder traversal gives the information of root too if inversed

#### LC128 - Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/
- Use a hashset to store, every first time the prev num is not contained, find the longest consecutive sequence from here and compare with the stored longest.