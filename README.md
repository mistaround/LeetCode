# LeetCode

#### LC1 - Two Sum
https://leetcode.com/problems/two-sum/
- Classical HashMap

#### LC3 - Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
- Use HashMap as sliding window
- ans = Math.max(ans, i - left);
- left = Math.max(left, window.get(cur) + 1);

#### LC10 - Regular Expression Matching
https://leetcode.com/problems/regular-expression-matching/
- Dynamic Programming
- dp[i][j] stands for s[:i] matches p[:j]
- if i=0 which means s is empty, only if p = a*b*c*... can match
- when meet *, we should consider skip or once or multiple times:
  - dp[i][j-2] or dp[i][j-1] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == "."))

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

#### LC17 - Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
- Recursive

#### LC18 - 4 Sum 
https://leetcode.com/problems/4sum/
- Same as 3 Sum

#### LC30 - Substring with Concatenation of All Words
https://leetcode.com/problems/substring-with-concatenation-of-all-words/
- Two HashMap, one for wordsCount one for wordsFound
- Sliding window, loop each time across a wordLength
  - Need to judge whether the word in wordsCount and then whether there are excessed word...
- In a word, it's very complex and I think I can't handle it if it appears in an interview

#### LC33 - Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/
- Binary Search

#### LC34 - Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
- Binary Search

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

#### LC44 - Wildcard Matching
https://leetcode.com/problems/wildcard-matching/
- Dynamic Programming
- Using dp[i][j] to represent whether s[:i] matches p[:j]
- init if s is empty, only p = ***... will match

#### LC49 - Group Anagrams 
https://leetcode.com/problems/group-anagrams/
- Sort each string and store in hashmap to group them
- "".join(sorted(string))

#### LC50 - Pow(x,n)
https://leetcode.com/problems/powx-n/
- pow(x,n) = pow(x,n/2) * pow(x, n/2) ...
- Recursively

#### LC54 - Spiral Matrix
https://leetcode.com/problems/spiral-matrix/
- Corner cases is killing me
- Spiral and smaller matrix

#### LC55 - Jump Game
https://leetcode.com/problems/jump-game/
- dp[i] stands for how long we can go from dp[:i]

#### LC56 - Merge Intervals
https://leetcode.com/problems/merge-intervals/
- Sort based on first element 
  - sorted(intervals, key=lambda intervals: intervals[0])
- Use a cache to update current merged interval
  - cache = [cache[0], max(cache[1], intervals[i][1])]

#### LC62 - Unique Paths
https://leetcode.com/problems/unique-paths/
- (m+n-2)!/((m-1)!(n-1)!)

#### LC69 - Sqrt(x)
https://leetcode.com/problems/sqrtx/submissions/
- Binary Search
- Use division to speed up

#### LC73 - Set Matrix Zeroes
https://leetcode.com/problems/set-matrix-zeroes/
- First ignore zeros in first col and row, record whether need to fill them 
- Use zeros in first col and row to indicate whether to fill the row or col
- At last fill the first row and col

#### LC75 - Sort Colors
https://leetcode.com/problems/sort-colors/
- Three pointer
  - Make sure nums before zero are all 0
  - nums after two are all 2
  - thus 1 will be in the middle

#### LC76 - Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/
- Two pointer sliding window and two hashmap
- When requirement is fulfilled, move left to smaller window
- To judge whether requirement is fulfilled, if the increment this time not exceed needed, one char matched. 

#### LC78 - Subsets
https://leetcode.com/problems/subsets/
- loop on length of subsets
  - use recursion to enumerate one by one
```python
  def helper(first, cur, k):
        if len(cur) == k:
            ans.append(cur[:])
            return
        for i in range(first, length):
            cur.append(nums[i])
            helper(i+1, cur, k)
            cur.pop()
```

#### LC79 - Word Search
https://leetcode.com/problems/word-search/
- Backtrace
- Modify pre-used element to avoid using again

#### LC84 - Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram/
- Append -1 to finally clear the stack
- Stack stores increasing height index
- Whenver meet a value smaller than stack top, calculate area

#### LC88 - Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/
- Nothing special

#### LC101 - Symmetric Tree
https://leetcode.com/problems/symmetric-tree/
- Recursion

#### LC102 - Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
- Queue

#### LC103 - Binary Tree Zigzag Level Order Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
- Just reverse when odd in LC102

#### LC104 - Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/
- Same as LC102,103

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
