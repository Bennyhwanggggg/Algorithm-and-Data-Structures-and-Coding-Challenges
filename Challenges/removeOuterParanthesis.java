class Solution {
    public String removeOuterParentheses(String S) {
        List<Integer> l = new ArrayList<>();
        Stack<Character> stack = new Stack<>();
        char[] arr = S.toCharArray();
        for (int i=0; i < arr.length; i++) {
            if (stack.size() == 0) {
                l.add(i);
                stack.push(arr[i]);
                continue;
            }
            if (stack.peek() == '(' && arr[i] == ')') {
                stack.pop();
                if (stack.size() == 0) {
                    l.add(i);
                } 
            } else if (stack.peek() == ')' && arr[i] == '(') {
                stack.pop();
                if (stack.size() == 0) {
                    l.add(i);
                }
            } else {
                stack.push(arr[i]);
            }
        }
        
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<l.size(); i+=2) {
            sb.append(S.substring(l.get(i)+1, l.get(i+1)));
        }
        return sb.toString();
    }
}
