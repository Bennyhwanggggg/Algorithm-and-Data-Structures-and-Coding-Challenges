"""
Shortest Way to Form String

From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.
"""


"""
Binary Search

Create mapping from each source char to the indices in source of that char.
Iterate over target, searching for the next index in source of each char. Return -1 if not found.
Search is by binary search of the list of indices in source of char.
If the next index in source requires wrapping around to the start of source, increment result count.
Time: O(n log m) for source of length m and target of length n.
Space: O(m) 

The idea is to create an inverted index that saves the offsets of where each character occurs in source. The index data structure is represented as a hashmap, where the Key is the character, and the Value is the (sorted) list of offsets where this character appears. To run the algorithm, for each character in target, use the index to get the list of possible offsets for this character. Then search this list for next offset which appears after the offset of the previous character. We can use binary search to efficiently search for the next offset in our index.

Example with source = "abcab", target = "aabbaac"
The inverted index data structure for this example would be:
inverted_index = {
a: [0, 3] # 'a' appears at index 0, 3 in source
b: [1, 4], # 'b' appears at index 1, 4 in source
c: [2], # 'c' appears at index 2 in source
}
Initialize i = -1 (i represents the smallest valid next offset) and loop_cnt = 1 (number of passes through source).
Iterate through the target string "aabbaac"
a => get the offsets of character 'a' which is [0, 3]. Set i to 1.
a => get the offsets of character 'a' which is [0, 3]. Set i to 4.
b => get the offsets of character 'b' which is [1, 4]. Set i to 5.
b => get the offsets of character 'b' which is [1, 4]. Increment loop_cnt to 2, and Set i to 2.
a => get the offsets of character 'a' which is [0, 3]. Set i to 4.
a => get the offsets of character 'a' which is [0, 3]. Increment loop_cnt to 3, and Set i to 1.
c => get the offsets of character 'c' which is [2]. Set i to 3.
We're done iterating through target so return the number of loops (3).

The runtime is O(M) to build the index, and O(logM) for each query. There are N queries, so the total runtime is O(M + N*logM). M is the length of source and N is the length of target. The space complexity is O(M), which is the space needed to store the index.
"""
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        
        index = collections.defaultdict(list)
        
        for i, s in enumerate(source):
            index[s].append(i)
            
        res = 0
        i = 0  # next index of source to check
        
        for t in target:
            if t not in index:
                return -1  # cannot make target if char not in source
            
            indices = index[t]
            j = bisect.bisect_left(indices, i)
            if j == len(indices):  # index in char_indices[c] that is >= i
                res += 1  # wrap around to beginning of source
                j = 0
            i = indices[j] + 1  # next index in source
        
        return res if i == 0 else res + 1  # add 1 for partial source
    

"""
DP

The main idea behind this code is also to build up an inverted index data structure for the source string and then to greedily use characters from source to build up the target. In this code, it's the dict array. Each character is mapped to an index where it is found at in source. In this code, dict[i][c - 'a'] represents the earliest index >= i where character c occurs in source.

For example, if source = "xyzy", then dict[0]['y' - 'a'] = 1 but dict[2]['y'-'a'] = 3.

Also a value of -1, means that there are no occurrences of character c after the index i.

So, after this inverted data structure is built (which took O(|Σ|*M) time). We iterate through the characters of our target String. The idxOfS represents the current index we are at in source.
For each character c in target, we look for the earliest occurrence of c in source using dict via dict[idxOfS][c - 'a']. If this is -1, then we have not found any other occurrences and hence we need to use a new subsequence of S.

Otherwise, we update idxOfS to be dict[idxOfS][c - 'a'] + 1 since we can only choose characters of source that occur after this character if we wish to use the same current subsequence to build the target.

dict[idxOfS][c-'a'] = N - 1 is used as a marker value to represent that we have finished consuming the entire source and hence need to use a new subsequence to continue.

(I would highly recommend reading @Twohu's examples of how to use the inverted index data structure to greedily build target using the indexes. They go into much more detail).

At the end, the check for (idxOfS == 0? 0 : 1) represents whether or not we were in the middle of matching another subsequence. If we were in the middle of matching it, then we would need an extra subsequence count of 1 since it was never accounted for.


"""
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        if len(set(target) - set(source)) > 0:
            return -1
        
        m = len(source)
        move = [[-1]*26 for _ in range(m)]
        move[0] = [source.find(chr(c)) + 1 for c in range(ord('a'), ord('a') + 26)]
        
        for i in range(-1, -m, -1):
            move[i] = list(map(lambda x: x+1, move[i+1]))
            move[i][ord(source[i]) - 97] = 1
        
        i = 0
        for c in target:
            i += move[i%m][ord(c)-ord('a')]
        return i//m + (i%m > 0)
        

