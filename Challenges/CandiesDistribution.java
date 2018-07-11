class Solution {
    public int distributeCandies(int[] candies) {
        HashSet<Integer> seen = new HashSet<Integer>();
        for(int i=0; i<candies.length; i++){
            seen.add(candies[i]);
        }
        return Math.min(seen.size(), candies.length/2);
    }
}