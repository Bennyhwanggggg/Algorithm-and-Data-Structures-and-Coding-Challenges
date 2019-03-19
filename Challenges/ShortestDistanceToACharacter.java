class Solution {
    public int[] shortestToChar(String S, char C) {
        int n = S.length();
        int[] res = new int[n];
        int pos = -n;
        for(int i=0; i<n; i++){
            if(S.charAt(i) == C){
                pos = i;
            }
            res[i] = pos != -n ? i-pos : Integer.MAX_VALUE;
        }
        pos = -n;
        for(int i=n-1; i>=0; i--){
            if(S.charAt(i) == C){
                pos = i;
            }
            if(pos != -n){
                res[i] = Math.min(res[i], pos-i);
            }
        }
        return res;
        
    }
}