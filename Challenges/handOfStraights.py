"""
Hand of Straights

Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
Example 2:

Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.
 

Note:

1 <= hand.length <= 10000
0 <= hand[i] <= 10^9
1 <= W <= hand.length
"""

"""
Priority Queue

Time: O(nlog(n) * W) as heap has O(log(n)) push and pop. There are N cards and at most we do the push and pop operations W times
Space: O(n)
"""
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        pq = []
        for n in hand:
            heapq.heappush(pq, n)
        
        while pq:
            current = []
            store = []
            while len(pq) > 0 and len(current) < W:
                smallest_card = heapq.heappop(pq)
                if len(current) == 0 or smallest_card == current[-1] + 1:
                    current.append(smallest_card)
                else:
                    store.append(smallest_card)
            
            if len(current) < W:
                return False
            else:
                for card in store:
                    heapq.heappush(pq, card)
        return True

