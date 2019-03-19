class Solution {
    public boolean detectCapitalUse(String word) {
        if (word == null || word.length() <= 1){
            return true;
        }
        boolean isFirstCapital = Character.isUpperCase(word.charAt(0));
        boolean isPrevCaptial = Character.isUpperCase(word.charAt(1));
        if (!isFirstCapital && isPrevCaptial){
            return false;
        }
        for (int i=2; i<word.length(); i++){
            boolean isCurrentCaptial = Character.isUpperCase(word.charAt(i));
            if ((!isFirstCapital && isCurrentCaptial) || (!isPrevCaptial && isCurrentCaptial)){
                return false;
            }
            if(isFirstCapital && (isPrevCaptial && !isCurrentCaptial)){
                return false;
            }
            isPrevCaptial = isCurrentCaptial;
        }
        return true;                                                        
    }
}

class Solution2 {
    public boolean detectCapitalUse(String word) {
        int cap=0;
        for(int i=0;i<word.length();i++){
            if(word.charAt(i)>='A' && word.charAt(i)<='Z')
                cap++;
        }
        
        if(cap==word.length() || (cap==1 && word.charAt(0)>='A' && word.charAt(0)<='Z') || cap==0 )
            return true;
        
        return false;
    }
}