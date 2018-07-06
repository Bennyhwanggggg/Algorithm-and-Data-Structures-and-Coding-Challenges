class Solution {
    public int findComplement(int num) {
        String result = Integer.toBinaryString(num);
        String str = "";
        for(int i=0; i<result.length(); i++){
            str += result.charAt(i) == '1' ? "0" : "1";
        }
        return Integer.parseInt(str, 2);
    }
}