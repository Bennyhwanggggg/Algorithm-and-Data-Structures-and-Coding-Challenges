"""
Total Rectangle Area

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
Note:

Assume that the total area is never beyond the maximum possible value of int.
"""

"""
Time: O(1)
Space: O(1)
"""
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        total = (D-B)*(C-A) + (H-F)*(G-E)
        
        width = max(0, min(C, G) - max(A, E))
        height = max(0, min(D, H) - max(B, F))
        
        return total - width*height
        
        
