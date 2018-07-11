class Solution {
    public boolean isToeplitzMatrix(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        for(int i=0; i<n; i++){
            if(!checkDiagonal(matrix, 0, i)){
                return false;
            }
        }
        for(int i=0; i<m; i++){
            if(!checkDiagonal(matrix, i, 0)){
                return false;
            }
        }
        return true;
    }
    
    public static boolean checkDiagonal(int[][] matrix, int x, int y){
        int m = matrix.length;
        int n = matrix[0].length;
        int original = matrix[x][y];
        for(int i=x, j=y; i<m && j<n; i++, j++){
            if(original != matrix[i][j]){
                return false;
            }
        }
        return true;
    }
}