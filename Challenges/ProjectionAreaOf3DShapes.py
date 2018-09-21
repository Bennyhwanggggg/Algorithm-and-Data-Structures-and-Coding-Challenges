class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        shadow_xoy = sum([1 for i in grid for j in i if j != 0])
        shadow_xoz = sum([max(i) for i in grid])
        shadow_yoz = sum([max(i) for i in list(zip(*grid))])
        return shadow_xoy + shadow_xoz + shadow_yoz