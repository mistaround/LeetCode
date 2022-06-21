class Solution {
    public int maxProfit(int[] prices) {
        int l = prices.length;
        if (l == 0 || l == 1) {
            return 0;
        }
        int profit = 0;
        for (int i = 0; i < l - 1; i ++) {
            int p = prices[i + 1] - prices[i];
            if (p > 0) {
                profit += p;
            }
        }
        return profit;
    }
}