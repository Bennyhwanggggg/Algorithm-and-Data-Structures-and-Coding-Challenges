"""
Given an array of roses. roses[i] means rose i will bloom on day roses[i]. Also given an int k, which is the minimum number of adjacent bloom roses required for a bouquet, and an int n, which is the number of bouquets we need. Return the earliest day that we can get n bouquets of roses.

Example:
Input: roses = [1, 2, 4, 9, 3, 4, 1], k = 2, n = 2
Output: 4
Explanation:
day 1: [b, n, n, n, n, n, b]
The first and the last rose bloom.

day 2: [b, b, n, n, n, n, b]
The second rose blooms. Here the first two bloom roses make a bouquet.

day 3: [b, b, n, n, b, n, b]

day 4: [b, b, b, n, b, b, b]
Here the last three bloom roses make a bouquet, meeting the required n = 2 bouquets of bloom roses. So return day 4.
"""

"""
The problem can be restated as:
From all subarrays of size >= k, take n of these with the lowest maximum values, and return the highest of these maximums.

To optimize, I'd start by building my first subarray by expanding it, from the minimum value in the array, to k adjacent neighbors. I'd then build the next subarray from the next minimum and so on, till I get my n subarrays. This is a greedy algorithm. Would require a heap...
"""
def minDaysBloom(roses, k, n):
	if k*n > len(roses):
		return -1

	bouquets = 0
	days = -float('inf')
	daysSeen = set()
	i = 0
	while i < len(roses):
		adjacent = False
		day = -float('inf')
		j = i
		while j < len(roses) and j < i+k:
			day = max(day, roses[j])
			if j < i+k-1:
				adjacent = abs(roses[j] - roses[j+1]) == 1
			j += 1

		if adjacent:
			bouquets += 1
			days = max(days, day)
			if bouquets >= n:
				return days
			i += k
		else:
			daysSeen.add(day)
			i += 1

"""
//DP
    int minDaysBloomByDp(int[] roses, int k, int n) {
        int[] windowKmax = new int[roses.length - k + 1];
        fillMax(windowKmax,roses,k);
        int[][] dp = new int[n+1][roses.length + 1];
        for (int i = 1; i <= n; i++) {
            Arrays.fill(dp[i],Integer.MAX_VALUE);
            for (int j = k; j <= roses.length; j++) {
                dp[i][j] = Math.min(dp[i][j - 1], Math.max(dp[i - 1][j - k],windowKmax[j - k]));
            }
        }
        return dp[n][roses.length];
    }
    void fillMax(int[] windowKmax, int[] r, int k) {
        Deque<Integer> dq = new ArrayDeque<>();
        for (int i = 0; i < r.length; i++) {
            if (i >= k && r[i - k] == dq.peekFirst()) dq.pollFirst();
            while (!dq.isEmpty() && r[i] > dq.peekLast()) dq.pollLast();
            dq.offerLast(r[i]);
            if (i >= k - 1) windowKmax[i - k + 1] = dq.peekFirst();
        }
    }
//BS    

It can be solved using binary search approach.
1: take lo=1 and hi= max. days a rose needs to bloom
2: mid = (lo+hi)/2
3: calculate the no. of bouquets (= x) which we can make when 'mid' no. of days are passed.
4. if(x<n) lo = mid+1
else hi = mid
5. go to step 2

    int minDaysBloomByBS(int[] roses, int k, int n) {
        int min = Integer.MAX_VALUE, max = -1;
        for (int r : roses) {
            max = Math.max(r,max);
            min = Math.min(r,min);
        }
        int[] windowKmax = new int[roses.length - k + 1];
        fillMax(windowKmax,roses,k);
        int s = min, e = max;
        while (s <= e) {
            int mid = (e - s)/2 + s;
            if (search(windowKmax,n,k,mid)) {
                e = mid - 1;
            } else {
                s = mid + 1;
            }
        }
        return e + 1;
    }
    
    boolean search(int[] win,int n,int k,int day) {
        for (int i = 0; i < win.length; ) {
            if (day >= win[i]) {
                n--;
                i+=k;
            } else {
                i++;
            }
        }
        return n <= 0;
    }
"""

	print(sorted(list(daysSeen), reverse=True)[n-1])
	return sorted(list(daysSeen), reverse=True)[n-1]

if __name__ == '__main__':
	assert minDaysBloom(roses=[1, 2, 4, 9, 3, 4, 1], k=2, n=2) == 4
