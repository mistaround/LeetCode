class Solution {
    public int maxProduct(int[] nums) {
        int max = nums[0];
        
        int cur = 1;
        for (int i = 0; i < nums.length; i ++) {
            cur = cur * nums[i];
            max = Math.max(cur, max);
            if (cur == 0) cur = 1;
        }
        
        cur = 1;
        for (int i = nums.length - 1; i >= 0; i --) {
            cur = cur * nums[i];
            max = Math.max(cur, max);
            if (cur == 0) cur = 1;
        }
        
        return max;
    }
}