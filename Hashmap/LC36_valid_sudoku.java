class Solution {
    public boolean isValidSudoku(char[][] board) {
        for (int i=0; i<9; i++)
        {
            int[] dict = new int[9];
            for (int j=0; j<9; j++)
            {
                if(board[i][j] != '.')
                {
                    if (dict[board[i][j]-'0'-1] == 1)
                        return false;
                    else
                        dict[board[i][j]-'0'-1] = 1;
                }
            }
        }
        for (int i=0; i<9; i++)
        {
            int[] dict = new int[9];
            for (int j=0; j<9; j++)
            {
                if(board[j][i] != '.')
                {
                    if (dict[board[j][i]-'0'-1] == 1)
                        return false;
                    else
                        dict[board[j][i]-'0'-1] = 1;
                }
            }
        }
        for (int i=0; i<9; i+=3)
        {
            for (int j=0; j<9; j+=3)
            {
                int[] dict = new int[9];
                for (int x=0; x<3; x++)
                {
                    for (int y=0; y<3; y++)
                    {
                        if(board[i+x][j+y] != '.')
                        {
                            if (dict[board[i+x][j+y]-'0'-1] == 1)
                                return false;
                            else
                                dict[board[i+x][j+y]-'0'-1] = 1;
                        }
                    }
                }              
            }
        }
        return true;
    }
}