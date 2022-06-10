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