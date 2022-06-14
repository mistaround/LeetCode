class Solution {
    public String minWindow(String s, String t) {
        Map<Character, Integer> charCount = new HashMap<>();
        Map<Character, Integer> charWindow = new HashMap<>();
        int sLen = s.length();
        int tLen = t.length();
        int minimum = sLen + 1;
        int left = 0;
        int right = 0;
        int used = sLen + 1;
        String ans = "";
        boolean formed = true;

        for (int i = 0; i < tLen; i ++) {
            char c = t.charAt(i);
            charCount.put(c, charCount.getOrDefault(c, 0) + 1);
        }
        
        while (left < sLen) {
            while (right < sLen) {
                char cur = s.charAt(right);
                if (charCount.containsKey(cur)) {
                    charWindow.put(cur, charWindow.getOrDefault(cur, 0) + 1);
                }

                formed = true;
                for (int j = 0; j < tLen; j ++) {
                    char tmp = t.charAt(j);
                    if (charCount.getOrDefault(tmp, 0) > charWindow.getOrDefault(tmp, 0)) {
                        formed = false;
                        break;
                    }
                }
                right ++;
                
                if (formed) {
                    break;
                }
            }
            
            while (formed) {
                char leftMost = s.charAt(left);
                if (charWindow.containsKey(leftMost)) {
                    charWindow.put(leftMost, charWindow.get(leftMost) - 1);
                }
                left += 1;
                for (int j = 0; j < tLen; j ++) {
                    char tmp = t.charAt(j);
                    if (charCount.getOrDefault(tmp, 0) > charWindow.getOrDefault(tmp, 0)) {
                        formed = false;
                        break;
                    }
                }
            }
            
            used = right - left + 1;
            if (used < minimum) {
                minimum = used;
                ans = s.substring(left - 1, right);
            }
            
            if (left + used - 1 == sLen) {
                break;
            }
        }
        return ans;
    }
}