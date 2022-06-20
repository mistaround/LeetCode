import java.util.ArrayList;
import java.util.List;

class Solution {
    String lookup[] = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    ArrayList<String> ans = new ArrayList<>();

    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0) 
            return this.ans;
        helper("", digits);
        return this.ans;
    }

    private void helper(String prev, String digits) {
        if (digits.length() == 0) {
            ans.add(prev);
            return;
        }
        int bit = Integer.parseInt(String.valueOf(digits.charAt(0)));
        String cur = lookup[bit];
        for (int i = 0; i < cur.length(); i++) {
            helper(prev + String.valueOf(cur.charAt(i)), digits.substring(1));
        }
    }

}