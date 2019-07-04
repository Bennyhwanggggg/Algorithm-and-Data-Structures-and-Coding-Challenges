/**
Given an input string, reverse the string word by word.
**/

class Solution {
    public String reverseWords(String s) {
        String[] words = s.split("\\s");
        StringBuilder sb = new StringBuilder();
        
        for (int i=words.length-1; i>=0; i--) {
            if(words[i].equals("")){
                continue;
            }
            if(i != words.length-1){
                sb.append(" ");
            }
            sb.append(words[i]);
        }
        return sb.toString();
    }
}
