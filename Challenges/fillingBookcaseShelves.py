"""
Filling Bookcase Shelves

We have a sequence of books: the i-th book has thickness books[i][0] and height books[i][1].

We want to place these books in order onto bookcase shelves that have total width shelf_width.

We choose some of the books to place on this shelf (such that the sum of their thickness is <= shelf_width), then build another level of shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down.  We repeat this process until there are no more books to place.

Note again that at each step of the above process, the order of the books we place is the same order as the given sequence of books.  For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.

Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.

Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4
Output: 6
Explanation:
The sum of the heights of the 3 shelves are 1 + 3 + 2 = 6.
Notice that book number 2 does not have to be on the first shelf.
 

Constraints:

1 <= books.length <= 1000
1 <= books[i][0] <= shelf_width <= 1000
1 <= books[i][1] <= 1000

"""

"""
For each book, go back in the same shelf to find max height or put it in next shelf
Time: O(N^2)
Space: O(N)
"""
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        n = len(books)
        dp = [float('inf')]*(n+1)  # dp[i] indicates min height for books 0 to i - 1
        dp[0] = 0   # no book, no height
        for i in range(1, n+1):
            curr_width, curr_height = shelf_width, 0
            j = i - 1
            while j >= 0 and curr_width - books[j][0] >= 0:
                # put book j into this row & update info
                curr_width -= books[j][0]
                curr_height = max(curr_height, books[j][1])
                dp[i] = min(dp[i], dp[j] + curr_height)
                j -= 1
        return dp[-1]
        

