import java.util.HashMap;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> window = new HashMap<>();
        int ans = 0;
        int left = 0;
        int i = 0;
        for (; i < s.length(); i++) {
            char cur = s.charAt(i);
            if (window.containsKey(cur)) {
                ans = Math.max(ans, i - left);
                left = Math.max(left, window.get(cur) + 1);
            }
            window.put(cur, i);
        }
        ans = Math.max(ans, i - left);
        return ans;
    }
}