class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<Integer>();
        for (int num: nums) set.add(num);
        int longest = 0;
        
        for (int num: set) {
            if (!set.contains(num - 1)) {
                int cur = num;
                int count = 1;
                
                while (set.contains(++cur)) {
                    count ++;
                }
                
                longest = Math.max(longest, count);
            }
        }
        
        return longest;
    }
}