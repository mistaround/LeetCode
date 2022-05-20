import java.util.HashMap;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> window = new HashMap<>();
        int ans = 0;
        int left = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (window.containsKey(c)) {
                int idx = window.get(c);
                left = Math.max(left, idx + 1);
            }
            ans = Math.max(ans, i - left + 1);
            window.put(c, i);
        }
        return ans;
    }
}