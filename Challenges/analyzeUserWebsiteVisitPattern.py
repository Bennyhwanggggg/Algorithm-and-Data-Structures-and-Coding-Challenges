"""
Analyze User Website Visit Pattern

We are given some website visits: the user with name username[i] visited the website website[i] at time timestamp[i].

A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits.  (The websites in a 3-sequence are not necessarily distinct.)

Find the 3-sequence visited by the largest number of users. If there is more than one solution, return the lexicographically smallest such 3-sequence.

 

Example 1:

Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]
Explanation: 
The tuples in this example are:
["joe", 1, "home"]
["joe", 2, "about"]
["joe", 3, "career"]
["james", 4, "home"]
["james", 5, "cart"]
["james", 6, "maps"]
["james", 7, "home"]
["mary", 8, "home"]
["mary", 9, "about"]
["mary", 10, "career"]
The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.
 

Note:

3 <= N = username.length = timestamp.length = website.length <= 50
1 <= username[i].length <= 10
0 <= timestamp[i] <= 10^9
1 <= website[i].length <= 10
Both username[i] and website[i] contain only lowercase characters.
It is guaranteed that there is at least one user who visited at least 3 websites.
No user visits two websites at the same time.
"""

"""
for each list, generate their combinations of three and use Counter to keep count
"""
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        dp = collections.defaultdict(list)
        for time, user, web in sorted(zip(timestamp, username, website)):
            dp[user].append(web)
        
        cnt = collections.Counter()
        for x in dp.values():  
            cnt += collections.Counter(set(itertools.combinations(x, 3)))

        return min(cnt, key=lambda k: (-cnt[k], k))
    
# no api
from collections import *
class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        def helper(sol,idx,res,arr):
            if len(sol)==3:
                res.add(tuple(sol))
                return 
            for i in range(idx,len(arr)):
                helper(sol+[arr[i]],i+1,res,arr)
                
        def getseq3(arr):#get all unique 3 sequence tuple list from array of events
            res=set()
            helper([],0,res,arr)
            return res    
        
        people2weblis=collections.defaultdict(list)
        seq3Cnt=collections.Counter()
        for _,user,ws in sorted(zip(timestamp,username,website)):
            people2weblis[user].append(ws)
        for weblis in people2weblis.values():
            for seq3 in getseq3(weblis):
                seq3Cnt[seq3]+=1
        return min(seq3Cnt,key=lambda k:[-seq3Cnt[k],k])

