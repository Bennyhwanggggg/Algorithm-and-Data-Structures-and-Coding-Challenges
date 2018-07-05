class Solution {
    public int[][] flipAndInvertImage(int[][] A) {
        if(A == null || A.length == 0){
            return null;
        }
        int size = A[0].length - 1;
        for(int i=0; i<A.length; i++){
            for(int j=0; j<=size/2; j++){
                int x = A[i][j];
                A[i][j] = (A[i][size-j] == 1) ? 0:1;
                A[i][size-j] = (x == 1) ? 0:1;
            }
        }
        return A;
    }
}