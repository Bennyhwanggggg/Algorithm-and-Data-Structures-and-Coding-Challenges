"""
Valid Tic Tac Toe State

A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player always places "X" characters, while the second player always places "O" characters.
"X" and "O" characters are always placed into empty squares, never filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Example 1:
Input: board = ["O  ", "   ", "   "]
Output: false
Explanation: The first player always plays "X".

Example 2:
Input: board = ["XOX", " X ", "   "]
Output: false
Explanation: Players take turns making moves.

Example 3:
Input: board = ["XXX", "   ", "OOO"]
Output: false

Example 4:
Input: board = ["XOX", "O O", "XOX"]
Output: true
Note:

board is a length-3 array of strings, where each string board[i] has length 3.
Each board[i][j] is a character in the set {" ", "X", "O"}.
"""

"""
Let's try to think about the necessary conditions for a tic-tac-toe board to be valid.

Since players take turns, the number of 'X's must be equal to or one greater than the number of 'O's.

A player that wins has to win on the move that they make:

If the first player wins, the number of 'X's is one more than the number of 'O's
If the second player wins, the number of 'X's is equal to the number of 'O's.
The board can't simultaneously have three 'X's and three 'O's in a row: once one player has won (on their move), there are no subsequent moves.

It turns out these conditions are also sufficient to check the validity of all boards. This is because we can check these conditions in reverse: in any board, either no player, one player, or both players have won. In the first two cases, we should check the previously stated counting conditions (a relationship between xCount and oCount), and this is sufficient. In the last case, it is not allowed to have both players win simultaneously, so our check was also sufficient.

Time: O(1)
Space: O(1)
"""
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        FIRST = 'X'
        SECOND = 'O'
        
        x_count = sum(row.count(FIRST) for row in board)
        o_count = sum(row.count(SECOND) for row in board)
        
        def win(board, player):
            for i in range(3):
                if all(board[i][j] == player for j in range(3)):
                    return True
                if all(board[j][i] == player for j in range(3)):
                    return True
            return (player == board[1][1] == board[0][0] == board[2][2]) or (player == board[1][1] == board[0][2] == board[2][0])
        
        if x_count != o_count and x_count-1 != o_count:
            return False
        if win(board, FIRST) and x_count-1 != o_count:
            return False
        if win(board, SECOND) and x_count != o_count:
            return False
        return True

