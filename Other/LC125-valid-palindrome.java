class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[^a-zA-Z0-9]","");
        int l = s.length();
        if (l == 0) return true;
        s = s.toLowerCase();
        for (int i = 0; i < (int)Math.floor(l/2); i++) {
            if (s.charAt(i) != s.charAt(l-1-i)) {
                return false;
            }
        }
        return true;
    }
}