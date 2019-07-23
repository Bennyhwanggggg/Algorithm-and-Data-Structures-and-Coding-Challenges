"""
Letter Tile Possibilities

You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.

Example 1:

Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: "AAABBC"
Output: 188
"""

"""
Generate all premutations

Time: O(n!)
"""
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        memo = set()
        def dfs(cur, eles):
            if cur in memo:
                return
            memo.add(cur)
            for i, e in enumerate(eles):    # 1
                dfs(cur + e, eles[:i] + eles[i+1:])  # 2
            return
        dfs("", tiles)
        return len(memo) - 1      # get rid of empty string

