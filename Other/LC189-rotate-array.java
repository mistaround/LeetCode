class Solution {
    public void rotate(int[] nums, int k) {
        int length = k % nums.length;
        int offset = nums.length - length;
        int[] cpy = new int[nums.length];
        System.arraycopy(nums, offset, cpy, 0, length);
        System.arraycopy(nums, 0, cpy, length, offset);
        System.arraycopy(cpy, 0, nums, 0, nums.length);
    }
}