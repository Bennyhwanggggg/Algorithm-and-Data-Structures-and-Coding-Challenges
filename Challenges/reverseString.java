class Solution {
    public void reverseString(char[] s) {
        int stringLength = s.length;
        for (int i=0; i<stringLength/2; i++) {
            char temp = s[i];
            s[i] = s[stringLength-i-1];
            s[stringLength-i-1] = temp;
        }
    }
}
