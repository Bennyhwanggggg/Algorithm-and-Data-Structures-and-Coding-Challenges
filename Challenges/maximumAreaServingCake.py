"""
Given an array containing the radii of circular cakes and the number of guests, determine the largest piece that can be cut from the cakes such that every guest gets a piece of the cake with the same area. It is not possible that a single piece has some part of one cake and some part of another cake and each guest is served only one piece of cake.

Example 1.
Radii = [ 1, 1, 1, 2, 2, 3]  numberOfGuests = 6.
Output: 7.0686

Reason being you can take the area of the cake with a radius of 3, and divide by 4. (Area  28.743 / 4  = 7.0686)
Use a similary sized piece from the remaining cakes of radius 2 because total area of cakes with radius 2 are > 7.0686

Example 2.
Radii [4, 3, 3] numberOfGuests = 3
Output: 28.2743

Example 3.
Radi [6, 7] numberOfGuests = 12
Output: 21.9911
"""
import math

# https://leetcode.com/discuss/interview-question/348510/google-online-assessment-maximum-area-serving-cake
def maximumAreaServingCake(radii, numberOfGuests):
    areas = [math.pi * r * r for r in radii]
    def possible(x):
        k = 0
        for a in areas:
            k += a // x
            if k >= numberOfGuests:
                return True
        return False
    
    l, r = 0, max(areas)
    while l + 1e-5 <= r:
        x = (l + r) / 2
        if possible(x):
            l = x
        else:
            r = x
    return round(l, 4)

if __name__ == '__main__':
	# Example 1.
	radii = [ 1, 1, 1, 2, 2, 3]  
	numberOfGuests = 6
	assert maximumAreaServingCake(radii, numberOfGuests) == 7.0686
	# Output: 7.0686

	# Example 2.
	radii = [4, 3, 3] 
	numberOfGuests = 3
	assert maximumAreaServingCake(radii, numberOfGuests) == 28.2743
	# Output: 28.2743

	# Example 3.
	radii = [6, 7] 
	numberOfGuests = 12
	assert maximumAreaServingCake(radii, numberOfGuests) == 21.9911
	# Output: 21.9911