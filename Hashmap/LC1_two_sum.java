import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> lookup = new HashMap<>();
        int[] ans = new int[2];
        for (int i = 0; i < nums.length; i++) {
            int remain = target - nums[i];
            if (lookup.containsKey(remain)) {
                ans[0] = lookup.get(remain);
                ans[1] = i;
                return ans;
            } else {
                lookup.put(nums[i], i);
            }
        }
        return ans;
    }
}