public class ValidSodoku_36 {
    public static void main(String[] args) {
        char[][] board = { { '.', '.', '.', '.', '5', '.', '.', '1', '.' },
                { '.', '4', '.', '3', '.', '.', '.', '.', '.' },
                { '.', '.', '.', '.', '.', '3', '.', '.', '1' },
                { '8', '.', '.', '.', '.', '.', '.', '2', '.' },
                { '.', '.', '2', '.', '7', '.', '.', '.', '.' },
                { '.', '1', '5', '.', '.', '.', '.', '.', '.' },
                { '.', '.', '.', '.', '.', '2', '.', '.', '.' },
                { '.', '2', '.', '9', '.', '.', '.', '.', '.' },
                { '.', '.', '4', '.', '.', '.', '.', '.', '.' } };
        System.out.println(isValidSudoku(board));
    }

    public static boolean isValidSudoku(char[][] board) {
        /**
         * Each row must contain the digits 1-9 without repetition.
         * Each column must contain the digits 1-9 without repetition.
         * Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
         * without repetition.
         */

        for (char[] row : board) {
            int[] freqRow = new int[10];
            for (char ch : row) {
                if (ch != '.') {
                    freqRow[ch - '0'] = freqRow[ch - '0'] + 1;
                }
            }

            for (int num : freqRow) {
                if (num > 1) {
                    return false;
                }
            }
        }

        for (int i = 0; i < board.length; i++) {
            int[] freqCol = new int[10];
            for (int j = 0; j < board.length; j++) {
                if (board[j][i] != '.') {
                    freqCol[board[j][i] - '0'] = freqCol[board[j][i] - '0'] + 1;
                }
            }

            for (int num : freqCol) {
                if (num > 1) {
                    return false;
                }
            }
        }

        for (int i = 0; i < 9; i++) {
            int[] freqBox = new int[10];
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    char ch = board[j + 3 * i%3][k + 3 * i/3]; // USE BRACKETS
                    if (ch != '.') {
                        freqBox[ch - '0'] = freqBox[ch - '0'] + 1;
                    }
                }
            }

            for (int num : freqBox) {
                if (num > 1) {
                    return false;
                }
            }
        }

        return true;
    }
}
