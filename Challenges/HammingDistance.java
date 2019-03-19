// "corresponding bits are different"? Yes, XOR! Also, do not forget there is a decent function Java provided: Integer.bitCount()


class Solution {
    public int hammingDistance(int x, int y) {
        return Integer.bitCount(x ^ y);
    }
}