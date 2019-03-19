class Solution {
    public char findTheDifference(String s, String t) {
        ArrayList<Character> list = new ArrayList<Character>();
        for(char c : t.toCharArray())
            list.add(c);
        for(char c : s.toCharArray())
            list.remove(Character.valueOf(c));
        return list.get(0);
    }
}

class Solution2 {
    public char findTheDifference(String s, String t) {
        HashMap<Character, Integer> seen = new HashMap<>();
        for(int i=0; i<s.length(); i++){
            if (!seen.containsKey(s.charAt(i))) {
                seen.put(s.charAt(i), 1);
            } else {
                seen.put(s.charAt(i), seen.get(s.charAt(i))+1);
            }
        }
        for(int i=0; i<t.length(); i++){
            if (!seen.containsKey(t.charAt(i)) || seen.get(t.charAt(i)) <= 0){
                return t.charAt(i);
            } else {
                seen.put(t.charAt(i), seen.get(t.charAt(i)) - 1);
            }
        }
        return '0';
    }
}