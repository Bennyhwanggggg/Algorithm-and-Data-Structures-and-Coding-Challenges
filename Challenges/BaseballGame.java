class Solution {
    public int calPoints(String[] ops) {
        int sum = 0;
        Stack<Integer> stack = new Stack<Integer>();
        for(String op: ops){
            switch(op){
                case "+": {
                    int t = stack.pop();
                    int r = t + stack.peek();
                    sum += r;
                    stack.push(t);
                    stack.push(r);
                    break;
                }
                case "D": {
                    int r = stack.peek()*2;
                    sum += r;
                    stack.push(r);
                    break;
                }
                case "C":
                    sum -= stack.pop();
                    break;
                default: {
                    int r = Integer.parseInt(op);
                    sum += r;
                    stack.push(r);
                }
            }
        }
        return sum;
    }
}