class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        dp = [[0]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        if obstacleGrid[0][0] != 1:
            dp[0][0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i == 0 and j == 0:
                    continue
                if obstacleGrid[i][j] != 1:
                    if i != 0:
                        dp[i][j] += dp[i-1][j]
                    if j != 0:
                        dp[i][j] += dp[i][j-1]
        return dp[-1][-1]