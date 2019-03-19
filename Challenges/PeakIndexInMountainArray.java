class Solution {
    public int peakIndexInMountainArray(int[] A) {
        int start = 0;
        int end = A.length - 1;
        while(start<end){
            int mid = start + (end-start)/2;
            if(A[mid] < A[mid+1]){
                start = mid+1;
            } else {
                end = mid;
            }
        }
        return start;
    }

    public int peakIndexInMountainArrayComplex(int[] A) {
        int lo = 0;
        int hi = A.length - 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (A[mid] < A[mid + 1]) { // peak index is after mid.
                lo = mid + 1;
            }else if (A[mid -1] > A[mid]) { // peak index is before mid.
                hi = mid;
            }else { // peak index is mid.
                return mid;
            }
        }
        return -1; // no peak.
    }

    public int peakIndexInMountainArrayOn(int[] A) {
        for (int i = 1; i < A.length; ++i) {
            if (A[i - 1] < A[i] && A[i] > A[i + 1]) { return i; }
        }
        return -1; // no peak.
    }
}



