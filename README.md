# LeetCode

#### LC1 - Two Sum

<https://leetcode.com/problems/two-sum/>

- Classical HashMap

#### LC3 - Longest Substring Without Repeating Characters

<https://leetcode.com/problems/longest-substring-without-repeating-characters/>

- Use HashMap as sliding window
- ans = Math.max(ans, i - left);
- left = Math.max(left, window.get(cur) + 1);

#### LC5 - Longest Palindromic Substring

<https://leetcode.com/problems/longest-palindromic-substring/>

- Spread from idx
- Even condition can be treated as odd by adding a char into it

#### LC10 - Regular Expression Matching

<https://leetcode.com/problems/regular-expression-matching/>

- Dynamic Programming
- dp[i][j] stands for s[:i] matches p[:j]
- if i=0 which means s is empty, only if p = a*b*c*... can match
- when meet *, we should consider skip or once or multiple times:
  - dp[i][j-2] or dp[i][j-1] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == "."))

#### LC11 - Container With Most Water

<https://leetcode.com/problems/container-with-most-water/>

- Greedy from outside

#### LC15 - 3 Sum

<https://leetcode.com/problems/3sum/>

- Sort
- Loop with two pointers
- Skipping used nums

#### LC16 - 3 Sum Closest

<https://leetcode.com/problems/3sum-closest/>

- Sort
- Loop with two pointers
- Comparing based on abs(target - current) and abs(target - closet)

#### LC17 - Letter Combinations of a Phone Number

<https://leetcode.com/problems/letter-combinations-of-a-phone-number/>

- Recursive

#### LC18 - 4 Sum

<https://leetcode.com/problems/4sum/>

- Same as 3 Sum

#### LC25 - Reverse Nodes in k-Group

<https://leetcode.com/problems/reverse-nodes-in-k-group/>

- Iterations

#### LC30 - Substring with Concatenation of All Words

<https://leetcode.com/problems/substring-with-concatenation-of-all-words/>

- Two HashMap, one for wordsCount one for wordsFound
- Sliding window, loop each time across a wordLength
  - Need to judge whether the word in wordsCount and then whether there are excessed word...
- In a word, it's very complex and I think I can't handle it if it appears in an interview

#### LC31 - Next Permutation

<https://leetcode.com/problems/next-permutation/>

- Find first non-increasing number from back
- Then find the smallest number larger than this number towards end
- swap them and reverse the nums after the number

#### LC32 - Longest Valid Parentheses

<https://leetcode.com/problems/longest-valid-parentheses/>

- Use a stack and an boolean array use it's index to store matched index
- Find longest consecutive True

#### LC33 - Search in Rotated Sorted Array

<https://leetcode.com/problems/search-in-rotated-sorted-array/>

- Binary Search

#### LC34 - Find First and Last Position of Element in Sorted Array

<https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/>

- Binary Search

#### LC36 - Valid Sudoku

<https://leetcode.com/problems/valid-sudoku/>

- Brute-force

#### LC38 - Count and Say

<https://leetcode.com/problems/count-and-say/>

- Recursive

#### LC40 - Combination Sum II

<https://leetcode.com/problems/combination-sum-ii/>

- BackTrack

#### LC41 - First Missing Positive

<https://leetcode.com/problems/first-missing-positive/>

- Discard num non-positive by making them larger than array size
- Loop i from 0 to len(num), make each num[i] indicates whether i+1 inside the array

#### LC42 - Trapping Rain Water

<https://leetcode.com/problems/trapping-rain-water/>

- Dynamic Programming
- Note that rain water is determined by min(maxLeft,maxRight)

#### LC43 - Multiply Strings

<https://leetcode.com/problems/multiply-strings/>

- Easy

#### LC44 - Wildcard Matching

<https://leetcode.com/problems/wildcard-matching/>

- Dynamic Programming
- Using dp[i][j] to represent whether s[:i] matches p[:j]
- init if s is empty, only p = ***... will match

#### LC49 - Group Anagrams

<https://leetcode.com/problems/group-anagrams/>

- Sort each string and store in hashmap to group them
- "".join(sorted(string))

#### LC50 - Pow(x,n)

<https://leetcode.com/problems/powx-n/>

- pow(x,n) = pow(x,n/2) * pow(x, n/2) ...
- Recursively

#### LC54 - Spiral Matrix

<https://leetcode.com/problems/spiral-matrix/>

- Corner cases is killing me
- Spiral and smaller matrix

#### LC55 - Jump Game

<https://leetcode.com/problems/jump-game/>

- dp[i] stands for how long we can go from dp[:i]

#### LC56 - Merge Intervals

<https://leetcode.com/problems/merge-intervals/>

- Sort based on first element
  - sorted(intervals, key=lambda intervals: intervals[0])
- Use a cache to update current merged interval
  - cache = [cache[0], max(cache[1], intervals[i][1])]

#### LC59 - Spiral Matrix II

<https://leetcode.com/problems/spiral-matrix-ii/>

- I hate this silly problem
- Loop on layer

#### LC62 - Unique Paths

<https://leetcode.com/problems/unique-paths/>

- (m+n-2)!/((m-1)!(n-1)!)

#### LC69 - Sqrt(x)

<https://leetcode.com/problems/sqrtx/submissions/>

- Binary Search
- Use division to speed up

#### LC73 - Set Matrix Zeroes

<https://leetcode.com/problems/set-matrix-zeroes/>

- First ignore zeros in first col and row, record whether need to fill them
- Use zeros in first col and row to indicate whether to fill the row or col
- At last fill the first row and col

#### LC75 - Sort Colors

<https://leetcode.com/problems/sort-colors/>

- Three pointer
  - Make sure nums before zero are all 0
  - nums after two are all 2
  - thus 1 will be in the middle

#### LC76 - Minimum Window Substring

<https://leetcode.com/problems/minimum-window-substring/>

- Two pointer sliding window and two hashmap
- When requirement is fulfilled, move left to smaller window
- To judge whether requirement is fulfilled, if the increment this time not exceed needed, one char matched.

#### LC78 - Subsets

<https://leetcode.com/problems/subsets/>

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

<https://leetcode.com/problems/word-search/>

- Backtrace
- Modify pre-used element to avoid using again

#### LC84 - Largest Rectangle in Histogram

<https://leetcode.com/problems/largest-rectangle-in-histogram/>

- Append -1 to finally clear the stack
- Stack stores increasing height index
- Whenver meet a value smaller than stack top, calculate area

#### LC88 - Merge Sorted Array

<https://leetcode.com/problems/merge-sorted-array/>

- Nothing special

#### LC95 - Unique Binary Search Trees II

<https://leetcode.com/problems/unique-binary-search-trees-ii/>

- Build large trees from small subtrees
- Smallest subtree is a None
- recursion

#### LC96 - Unique Binary Search Trees

<https://leetcode.com/problems/unique-binary-search-trees/>

- G(n): the number of unique BST for a sequence of length n.
- F(i,n): the number of unique BST, where the number i is served as the root of BST (1 \leq i \leq n1≤i≤n).
- Dynamic Programming

#### LC98 - Validate Binary Search Tree

<https://leetcode.com/problems/validate-binary-search-tree/>

- A valid BST node on the left should smaller than its parent, node on the right should larger than its parent
- Use +- inf as dummy left and right value

#### LC99 - Recover Binary Search Tree

<https://leetcode.com/problems/recover-binary-search-tree/>

- Inorder traversal of BST is a increasing sorted list
- So we can find the two wrong node in the list
- At last, use the val to find the two node and swap

#### LC100 - Same Tree

<https://leetcode.com/problems/same-tree/>

- isSameTree(p,q) = isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

#### LC101 - Symmetric Tree

<https://leetcode.com/problems/symmetric-tree/>

- Recursion

#### LC102 - Binary Tree Level Order Traversal

<https://leetcode.com/problems/binary-tree-level-order-traversal/>

- Queue

#### LC103 - Binary Tree Zigzag Level Order Traversal

<https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/>

- Just reverse when odd in LC102

#### LC104 - Maximum Depth of Binary Tree

<https://leetcode.com/problems/maximum-depth-of-binary-tree/>

- Same as LC102,103

#### LC105 - Construct Binary Tree from Preorder and Inorder Traversal

<https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/>

- Preorder traversal gives the information of root
- Inorder traversal gives theh information of left and right sub tree
- Step on by the index of preorder and recursively construct left and right subtree by inorder

#### LC106 - Construct Binary Tree from Inorder and Postorder Traversal

<https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/>

- Similar with LC105
- Postorder traversal gives the information of root too if inversed

#### LC108 - Convert Sorted Array to Binary Search Tree

<https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/>

- Just half and half

#### LC116 - Populating Next Right Pointers in Each Node

<https://leetcode.com/problems/populating-next-right-pointers-in-each-node/>

- BFS

#### LC118 - Pascal's Triangle

<https://leetcode.com/problems/pascals-triangle/>

- Easy

#### LC121 - Best Time to Buy and Sell Stock

<https://leetcode.com/problems/best-time-to-buy-and-sell-stock/>

- Use a stack to store prev minimum

#### LC122 - Best Time to Buy and Sell Stock II

<https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/>

- It's a brain teaser
- Since you can buy and sell on same day, if tommorrow will make profit, just buy today. Since if it's higher the day after tomorrow, we can just buy tomorrow and sell the day after tommorrow.

#### LC124 - Binary Tree Maximum Path Sum

<https://leetcode.com/problems/binary-tree-maximum-path-sum/>

- Think clearly, coding will be easy
- DFS, for largest value we need to concern whether it's left or right or l+r+m, for traverse we need to return max(l,r) + m since m cannot be used twice.

  ```Java
  private int helper(TreeNode root) {
          if (root == null) return 0;
          int cur = root.val;
          int left = Math.max(0, helper(root.left));
          int right = Math.max(0, helper(root.right));
          maximum = Math.max(maximum, left + right + cur);
          return Math.max(left, right) + cur;
      }
  ```

#### LC125 - Valid Palindrome

<https://leetcode.com/problems/valid-palindrome/>

- s.replaceAll("[^a-zA-Z0-9]","")

#### LC127 - Word Ladder

<https://leetcode.com/problems/word-ladder/>

- BFS so we can get result from same level to find the shortest
- Use two hashset to find both from begin and from end to speed up

#### LC128 - Longest Consecutive Sequence

<https://leetcode.com/problems/longest-consecutive-sequence/>

- Use a hashset to store, every first time the prev num is not contained, find the longest consecutive sequence from here and compare with the stored longest.

#### LC130 - Surrounded Regions

<https://leetcode.com/problems/surrounded-regions/>

- Only "O" in border will not be change, so
  - we can dfs search "O" region on border and mark them
  - traverse through whole board
    - if marked, change to "O"
    - elif unmarked "O", change to "X"

#### LC131 - Palindrome Partitioning

<https://leetcode.com/problems/palindrome-partitioning/>

- DP to make dp[i][j] represents whether s[i:j] is palindrome
- DFS to enumerate palindrome

#### LC134 - Gas Station

<https://leetcode.com/problems/gas-station/>

- If i to j cannot make it, any k in [i,j], k to j will not make it too
- So wo should then find from j+1, so finish in O(N)

#### LC136 - Single Number

<https://leetcode.com/problems/single-number/>

- XOR

#### LC138 - Copy List with Random Pointer

<https://leetcode.com/problems/copy-list-with-random-pointer/>

- HashMap

#### LC139 - Word Break

<https://leetcode.com/problems/word-break/>

- Store previous success index and loop on them

#### LC140 - Word Break II

<https://leetcode.com/problems/word-break-ii/>

- Idea from LC139 with DFS
- Store current word in current length in an array
  - Finally use dfs to generate the answer

#### LC141 - Linked List Cycle

<https://leetcode.com/problems/linked-list-cycle/>

- Two pointer, one faster, if met, True

#### LC146 - LRU Cache

<https://leetcode.com/problems/lru-cache/>

- Use double list with head and tail node
  - the node after the head node is mru
  - the node before the tail node is lru
  - use two internal function insert and delete to maintain the double list

#### LC147 - Insertion Sort List

<https://leetcode.com/problems/insertion-sort-list/>

- Just insertion sort on a linked list

#### LC148 - Sort List

<https://leetcode.com/problems/sort-list/>

- Merge sort of a linked list
  - Recursively split and merge left and right part

#### LC149 - Max Points on a Line

<https://leetcode.com/problems/max-points-on-a-line/>

- O(N^2) stupid method without optimization, just use a hash map to store (k-b, occurrence) pairs

#### LC150 - Evaluate Reverse Polish Notation

<https://leetcode.com/problems/evaluate-reverse-polish-notation/>

- Use a stack

#### LC152 - Maximum Product Subarray

<https://leetcode.com/problems/maximum-product-subarray/>

- Find max from head to tail and then tail to head to get rid of the sign problems

#### LC155 - Min Stack

<https://leetcode.com/problems/min-stack/>

- Stack entry save both val and minval

#### LC160 - Intersection of Two Linked Lists

<https://leetcode.com/problems/intersection-of-two-linked-lists/>

- HashSet

#### LC162 - Find Peak Element

<https://leetcode.com/problems/find-peak-element/>

- If num[i] > num[i+1], peak point must exist at x <= i
- Else, peak point must exist at x >= i + 1
- So we can do binary search

#### LC163 - Missing Ranges

<https://leetcode.com/problems/missing-ranges/>

- Nothing to say, a boring problem

#### LC164 - Maximum Gap

<https://leetcode.com/problems/maximum-gap/>

- Linear time sort algorithm
  - Radix Sort

#### LC166 - Fraction to Recurring Decimal

<https://leetcode.com/problems/fraction-to-recurring-decimal/>

- Long division

#### LC169 - Majority Element

<https://leetcode.com/problems/majority-element/>

- Use Counter
  - return Counter(nums).most_common[1][0](0)

#### LC171 - Excel Sheet Column Number

<https://leetcode.com/problems/excel-sheet-column-number/>

- 26-base

#### LC172 - Factorial Trailing Zeroes

<https://leetcode.com/problems/factorial-trailing-zeroes/>

- Hardcode....

#### LC179 - Largest Number

<https://leetcode.com/problems/largest-number/>

- Sort
- Use comparator and greedy algorihtm
  - extend two num string a and b to same length
  - if int a' > int b' return 1 else -1
  - if int a' = int b', if int(a + b) > int(b + a) return 1 else -1
- Sort again, sorted(strings, key=cmp_to_key(comparator), reverse=True)

#### LC189 - Rotate Array

<https://leetcode.com/problems/rotate-array/>

- System.arraycopy(src, srcIdx, tar, tarIdx, length)

#### LC190 - Reverse Bits

<https://leetcode.com/problems/reverse-bits/>

- Bit manipulation
- & to get last bit
- | to change 31 - i th bit

#### LC191 - Number of 1 Bits

<https://leetcode.com/problems/number-of-1-bits/>

- Bit manipulation

#### LC198 - House Robber

<https://leetcode.com/problems/house-robber/>

- DP, use a variable to store the max dp value before ith

#### LC200 - Number of Islands

<https://leetcode.com/problems/number-of-islands/>

- DFS to modify in place on visted node

#### LC202 - Happy Number

<https://leetcode.com/problems/happy-number/>

- Nothing to say, easy in python

#### LC204 - Count Primes

<https://leetcode.com/problems/count-primes/>

- Sieve of Eratosthenes, O(N) space complexity

#### LC206 - Reverse Linked List

<https://leetcode.com/problems/reverse-linked-list/>

- Recursion

#### LC207 - Course Schedule

<https://leetcode.com/problems/course-schedule/>

- Use two array to store finished conditions and current path for DFS
- If node on current path is revisited, there should be a circle
- Else if node is finished, just ingnore

#### LC208 - Implement Trie (Prefix Tree)

<https://leetcode.com/problems/implement-trie-prefix-tree/>

- Use a dictonary tree

#### LC210 - Course Schedule II

<https://leetcode.com/problems/course-schedule-ii/>

- Similar to LC207, add to answer when all child return True

#### LC212 - Word Search II

<https://leetcode.com/problems/word-search-ii/>

- Use Trie with DFS

#### LC215 - Kth Largest Element in an Array

<https://leetcode.com/problems/kth-largest-element-in-an-array/>

- Maintain a queue of size k

#### LC217 - Contains Duplicate

<https://leetcode.com/problems/contains-duplicate/>

- Simple HashMap

#### LC218 - The Skyline Problem

<https://leetcode.com/problems/the-skyline-problem/>

- Use priority queue, heapq
- Distinguish start and end point by different sign of height
- Sort based on point and height to make start beyond end

#### LC220 - Contains Duplicate III

<https://leetcode.com/problems/contains-duplicate-iii/>\

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

#### LC227 - Basic Calculator II

<https://leetcode.com/problems/basic-calculator-ii/>

- Use stack to store + - operations

#### LC229 - Majority Element II

<https://leetcode.com/problems/majority-element-ii/>

- Simple HashMap

#### LC230 - Kth Smallest Element in a BST

<https://leetcode.com/problems/kth-smallest-element-in-a-bst/>

- Inorder Traversal

#### LC234 - Palindrome Linked List

<https://leetcode.com/problems/palindrome-linked-list/>

- Turn to array

#### LC236 - Lowest Common Ancestor of a Binary Tree

<https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/>

- Use Two HashSet to store ancestors

#### LC237 - Delete Node in a Linked List

<https://leetcode.com/problems/delete-node-in-a-linked-list/>

- Brain Teaser

#### LC238 - Product of Array Except Self

<https://leetcode.com/problems/product-of-array-except-self/>

- [1 1 12 123]
- [234 34 4 1].reverse
- Multiply

#### LC239 - Sliding Window Maximum

<https://leetcode.com/problems/sliding-window-maximum/>

- Use a hashmap as sliding window

#### LC242 - Valid Anagram

<https://leetcode.com/problems/valid-anagram/>

- Use two Counter and subtract, if all zero True

#### LC274 - H-Index

<https://leetcode.com/problems/h-index/>

- First remove all zeros
- Sort and Loop:
  - if length - i <= citations[i]:
        break
- return length - i

#### LC295 - Find Median from Data Stream

<https://leetcode.com/problems/find-median-from-data-stream/>

- Use two heaps: minHeap maxHeap
- Maintain the two heap to make the top of the two heaps can make median

#### LC324 - Wiggle Sort II

<https://leetcode.com/problems/wiggle-sort-ii/>

- Sort
- Two pass, insert with stride of 1 each time

#### LC540 - Single Element in a Sorted Array

<https://leetcode.com/problems/single-element-in-a-sorted-array/>

- 1,1,2,2,3,4,4,8,8
- 0,1,2,3,4,5,6,7,8
- Notice singular num will change the index and num relations on both side
- So we can binary search based on this

#### LC560 - Subarray Sum Equals K

<https://leetcode.com/problems/subarray-sum-equals-k/>

- Prefix Sum with hashmap

#### LC572 - Subtree of Another Tree

<https://leetcode.com/problems/subtree-of-another-tree/>

- BFS and DFS

#### LC675 - Cut Off Trees for Golf Event

<https://leetcode.com/problems/cut-off-trees-for-golf-event/>

- A Star!

#### LC763 - Partition Labels

<https://leetcode.com/problems/partition-labels/>

- Notice that only if it can be binary divided it can be further divided

#### LC819 - Most Common Word

<https://leetcode.com/problems/most-common-word/>

- Hashmap

#### LC836 - Rectangle Overlap

<https://leetcode.com/problems/rectangle-overlap/>

- (rec2[2] - rec1[0]) *(rec2[0] - rec1[2]) < 0 and (rec2[3] - rec1[1])* (rec2[1] - rec1[3]) < 0

#### LC895 - Maximum Frequency Stack

<https://leetcode.com/problems/maximum-frequency-stack/>

- Heap sort by (frequency, index)

#### LC994 - Rotting Oranges

<https://leetcode.com/problems/rotting-oranges/>

- BFS

#### LC1022 - Sum of Root To Leaf Binary Numbers

<https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/>

- DFS

#### LC1122 - Relative Sort Array

<https://leetcode.com/problems/relative-sort-array/>

- HashMap

#### LC1155 - Number of Dice Rolls With Target Sum

<https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/>

- DP on n and target

#### LC1176 - Diet Plan Performance

<https://leetcode.com/problems/diet-plan-performance/>

- Easy sliding window

#### LC1214 - Two Sum BSTs

<https://leetcode.com/problems/two-sum-bsts/>

- DFS

#### LC1258 - Synonymous Sentences

<https://leetcode.com/problems/synonymous-sentences/>

- DFS with DFS

#### LC1331 - Rank Transform of an Array

<https://leetcode.com/problems/rank-transform-of-an-array/>

- HashMap

#### LC1689 - Partitioning Into Minimum Number Of Deci-Binary Numbers

<https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/>

- Brain teaser

#### LC2315 - Count Asterisks

<https://leetcode.com/problems/count-asterisks/>

- One pass

#### LC2316 - Count Unreachable Pairs of Nodes in an Undirected Graph

<https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/>

- Turn edges in to dictionary
- dfs to find each connections of each node
- calculate unreachable num at last

#### LC2317 - Maximum XOR After Operations

<https://leetcode.com/problems/maximum-xor-after-operations/>

- Emmmmm, just remember

#### LC2318 - Number of Distinct Roll Sequences

<https://leetcode.com/problems/number-of-distinct-roll-sequences/>

- We can get all possible combinations if given previous dice and previous-previous dice
- So we can use dp with dfs
- Use a 3D dp array to store the no of combionations given previous roll, previous-previous roll and current length

```python
class Solution:
    dp = [[[0 for _ in range(7)] for _ in range(7)] for _ in range(10001)]
    
    def distinctSequences(self, n: int) -> int:
        
        def helper(n, p, pp):
            if n == 0:
                return 1
            if self.dp[n][p][pp] == 0:
                for d in range(1, 7):
                    if d != p and d != pp and (p == 0 or math.gcd(d, p) == 1):
                        self.dp[n][p][pp] = (self.dp[n][p][pp] + helper(n-1, d, p)) % ((10 ** 9) + 7)
            return self.dp[n][p][pp]
        
        return helper(n, 0, 0)
```

#### LC2319 - Check if Matrix Is X-Matrix

<https://leetcode.com/problems/check-if-matrix-is-x-matrix/>

- Nothing to say

#### LC2320 - Count Number of Ways to Place Houses

<https://leetcode.com/problems/count-number-of-ways-to-place-houses/>

- Use 2D dp

#### LC2321 - Maximum Score Of Spliced Array

<https://leetcode.com/problems/maximum-score-of-spliced-array/>

- Kadane Algo: longest subarray sum
- So the answer can be changed to: max(sum(A) + kadane(B-A), sum(B) + kadane(A-B))

#### LC2325 - Decode the Message

<https://leetcode.com/problems/decode-the-message/>

- Nothing

#### LC2326 - Spiral Matrix IV

<https://leetcode.com/problems/spiral-matrix-iv/>

- Boring

#### LC2327 - Number of People Aware of a Secret

<https://leetcode.com/problems/number-of-people-aware-of-a-secret/>

- DP, 2 dp arrays

#### LC2328 - Number of Increasing Paths in a Grid

<https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/>

- DP with dfs

#### LC2335 - Minimum Amount of Time to Fill Cups

<https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/>

- Brain Teaser

#### LC2336 - Smallest Number in Infinite Set

<https://leetcode.com/problems/smallest-number-in-infinite-set/>

- Heap

#### LC2337 - Move Pieces to Obtain a String

<https://leetcode.com/problems/move-pieces-to-obtain-a-string/>

- One Pass compare left and right count until current char