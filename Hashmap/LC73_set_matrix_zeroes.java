import java.util.Arrays;

class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        boolean isRow = false;
        boolean isCol = false;
        for (int i = 0; i < m; i ++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    if (i == 0 || j == 0) {
                        if (i == 0) isRow = true;
                        if (j == 0) isCol = true;
                    } else {
                        matrix[i][0] = 0;
                        matrix[0][j] = 0;
                    }
                }
            }
        }
        for (int i = 1; i < m; i ++) {
            if (matrix[i][0] == 0) {
                Arrays.fill(matrix[i], 0);
            }
        }
        for (int j = 1; j < n; j ++) {
            if (matrix[0][j] == 0) {
                for (int k = 0; k < m; k ++) {
                    matrix[k][j] = 0;
                }
            }
        }
        if (isRow) {
            Arrays.fill(matrix[0], 0);
        }
        if (isCol) {
            for (int k = 0; k < m; k ++) {
                matrix[k][0] = 0;
            }
        }
    }
}