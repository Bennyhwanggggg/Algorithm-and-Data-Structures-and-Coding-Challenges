import collections
class Solution:
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        count = 0
        for row in picture:
            rowcollection = collections.Counter(row)
            if 'B' in rowcollection and rowcollection['B'] == 1:
                col = row.index('B')
                colcollection = collections.Counter([picture[r][col] for r in range(len(picture))])
                if colcollection['B'] == 1:
                    count += 1
        return count