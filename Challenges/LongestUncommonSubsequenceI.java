class Solution {
    public int findLUSlength(String a, String b) {
        return b.equals(a) ? -1 : Math.max(a.length(), b.length());
    }
}