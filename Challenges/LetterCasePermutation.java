class Solution {
    public List<String> letterCasePermutation(String S) {
        List<String> result = new ArrayList<>();
        backTrackPremutation(S.toLowerCase(), 0, result, new String());
        return result;
    }
    
    public void backTrackPremutation(String S, int index, List<String> permutations, String curr){
        if(index == S.length()){
            permutations.add(curr);
            return;
        }
        char currChar = S.charAt(index);
        if(Character.isDigit(currChar)){
            backTrackPremutation(S, index+1, permutations, curr+currChar);
        } else {
            backTrackPremutation(S, index+1, permutations, curr+currChar);
            backTrackPremutation(S, index+1, permutations, curr+Character.toUpperCase(currChar));
        }
    }
}