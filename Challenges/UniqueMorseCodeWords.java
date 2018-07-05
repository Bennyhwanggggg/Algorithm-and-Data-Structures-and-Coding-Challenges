class Solution {
    public int uniqueMorseRepresentations(String[] words) {
        String[] letters = {".-","-...","-.-.","-..",".","..-.","--.",
                          "....","..",".---","-.-",".-..","--","-.",
                          "---",".--.","--.-",".-.","...","-","..-",
                          "...-",".--","-..-","-.--","--.."};
        
        Set<String> transformations = new HashSet<String>();
        
        for(String word:words){
            StringBuilder sb = new StringBuilder();
            for(int i=0; i<word.length(); i++){
                sb.append(letters[word.charAt(i) - 'a']);
            }
            transformations.add(sb.toString());
        }
        return transformations.size();
    }
}