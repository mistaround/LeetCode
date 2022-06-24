class Solution {
    public int maxPoints(int[][] points) {
        if (points.length == 1) return 1;
        int maximum = 1;
        for (int idx1 = 0; idx1 < points.length; idx1 ++) {
            HashMap<String, Integer> used = new HashMap<>();
            for (int idx2 = 0; idx2 < points.length; idx2 ++) {
                if (idx1 == idx2) continue;
                int[] p1 = points[idx1];
                int[] p2 = points[idx2];
                double k = (double) (p1[1] - p2[1]) / (double) (p1[0] - p2[0]);
                double b = (double) p1[1] - (k * (double) p1[0]);
                
                String key = Double.toString(k) + "," + Double.toString(b);
                used.put(key, used.getOrDefault(key, 0) + 1);
            }
            for (Map.Entry ele: used.entrySet()) {
                maximum = Math.max((int)ele.getValue(), maximum);
            }
        }
        return maximum + 1;
    }
}