class Solution {
    public int firstMissingPositive(int[] nums) {
        int len = nums.length;
        int i;
        for (i = 0; i < len; i++) {
            if (nums[i] <= 0) {
                nums[i] = len + 2;
            }
        }
        for (i = 0; i < len; i++) {
            int idx = Math.abs(nums[i]) - 1;
            if (idx >= 0 && idx < len && nums[idx] > 0) {
                nums[idx] *= -1;
            }
        }
        for (i = 1; i < len + 1; i ++) {
            if (nums[i-1] > 0) {
                return i;
            }
        }
        return len + 1;
    }
}