class Solution {
    public int addDigits(int num) {
        while(Integer.toString(num).length() > 1){
            String n = Integer.toString(num);
            num = 0;
            for(int i=0; i<n.length(); i++){
                num += Character.getNumericValue(n.charAt(i));
            }
        }
        return num;
    }
}


class Solution2 {
    public int addDigits(int num) {
        int t=num;
        int sum=0;
        while(t>9)
        {
            sum=0;
            int r=t;
            while(r!=0)
            {
                int d=r%10;
                sum=sum+d;
                r=r/10;
            }
            t=sum;
        }
        return t;
    }
}