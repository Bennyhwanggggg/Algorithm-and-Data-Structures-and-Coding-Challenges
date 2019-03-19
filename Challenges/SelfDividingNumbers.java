class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> result = new ArrayList<>();
        for(int i=left; i<=right; i++){
            if(isSelfDividing(i)){
                result.add(i);
            }
        }
        return result;
    }
    
    public boolean isSelfDividing(int n){
        int original = n;
        while(n>0){
            int a = n%10;
            if(a==0 || original%a != 0){
                return false;
            }
            n /= 10;
        }
        return true;
    }
}