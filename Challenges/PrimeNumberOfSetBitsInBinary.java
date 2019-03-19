class Solution {
    public int countPrimeSetBits(int L, int R) {
        Set<Integer> primes = new HashSet<>(Arrays.asList(2, 3, 5, 7, 11, 13, 17, 19));
        int count = 0;
        for (int i = L; i <= R; i++)
            count += primes.contains(Integer.bitCount(i)) ? 1 : 0;
        return count;
    }
}