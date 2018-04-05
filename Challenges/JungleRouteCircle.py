class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        directions = {'R': (0, 1), 'L': (0, -1), 'U': (1, 0), 'D': (-1, 0)}

        curr = (0, 0)
        for m in moves:
            x, y = directions[m]
            curr = (curr[0] + x, curr[1] + y)

        return True if curr == (0, 0) else False

def judgeCircle(self, moves):
    direct = {'U': 1, 'D': -1, 'L': 1j, 'R': -1j}
    return 0 == sum(direct[m] for m in moves)

def judgeCircle(self, moves):
    return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')