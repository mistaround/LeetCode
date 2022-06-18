class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int matRow = matrix[0].length;
        int matCol = matrix.length;
        int times = (int) Math.min(Math.ceil(matCol/2.), Math.ceil(matRow/2.));
        List<Integer> ans = new ArrayList<Integer>();

        for (int i = 0; i < times; i ++){
            spiral(matrix, i, ans, matRow, matCol);
        }   
        return ans;
    }
    
    private void spiral(int[][] matrix, int time, List<Integer> ans, int matRow, int matCol) {
        int rowSize = matRow - time * 2;
        int colSize = matCol - time * 2;

        if (rowSize == 1 || colSize == 1) {
            if (rowSize == 1) {
                for (int i = time; i < time + colSize; i ++) {
                    ans.add(matrix[i][time]);
                }
            } else {
                for (int i = time; i < time + rowSize; i ++) {
                    ans.add(matrix[time][i]);
                }
            }
            return;
        }

        for (int i = time; i < time + rowSize - 1; i ++) {
            ans.add(matrix[time][i]);
        }
        for (int i = time; i < time + colSize - 1; i ++) {
            ans.add(matrix[i][matRow - 1 - time]);
        }
        for (int i = time + rowSize - 1; i > time; i --) {
            ans.add(matrix[matCol - 1 - time][i]);
        }
        for (int i = time + colSize - 1; i > time; i --) {
            ans.add(matrix[i][time]);
        }
        
    }
}
  