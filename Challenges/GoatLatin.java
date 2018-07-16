class Solution {
    public String toGoatLatin(String S) {
        int len = S.length();
        HashSet<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));
        String[] words = S.split(" ");
        String addition = "a";
        String result = "";
        for(String word: words){
            if(!vowels.contains(Character.toLowerCase(word.charAt(0)))){
                String first = Character.toString(word.charAt(0));
                result += word.substring(1) + first + "ma";
            } else {
                result += word + "ma";
            }
            result += addition;
            addition += "a";
            result += " ";
        }
        return result.trim();
    }
}