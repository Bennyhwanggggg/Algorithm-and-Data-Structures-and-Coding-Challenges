class Solution {
    public int[] numberOfLines(int[] widths, String S) {
        int[] result = {1, 0};
        int end = 100;
        for(char c: S.toCharArray()){
            int value = widths[c-'a'];
            if((end-value) >= 0){
                end -= value;
            } else {
                end = 100 - value;
                result[0] ++;
            }
        }
        result[1] = 100-end;
        return result;
    }
}