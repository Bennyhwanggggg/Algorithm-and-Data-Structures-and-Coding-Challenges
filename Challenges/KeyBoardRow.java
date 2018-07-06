class Solution {
    public String[] findWords(String[] words) {
        
        List<String> result = new ArrayList<>();

        for(String word: words){
            boolean isOneLine = false;
            if(word.toLowerCase().matches("^[qwertyuiop]+$")){
                isOneLine = true;
            }
            if(word.toLowerCase().matches("^[asdfghjkl]+$")){
                isOneLine = true;
            }
            if(word.toLowerCase().matches("^[zxcvbnm]+$")){
                isOneLine = true;
            }
            if(isOneLine){
                result.add(word);
            }
        }
        return result.toArray(new String[result.size()]);
        
    }
}