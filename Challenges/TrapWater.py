class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        arr, left, right, water = [], 0, 0, 0
        for h in height:
            left = max(left, h)
            arr.append(left)

        arr.reverse()
        print(arr)
        for n, h in enumerate(reversed(height)):
            print(right, h)
            right = max(right, h)
            water += min(arr[n], right) - h
            print(water)

        return water