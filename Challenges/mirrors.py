'''
Python version: 3.6
Author: Benny Hwang

Problem description here: https://github.com/Bennyhwanggggg/Practices/blob/master/Challenges/mirrors.md
'''

import os, sys
from collections import defaultdict
from binary_search_tree import BST
from heapq import heappush, heappop

# Constraints as given in the task description
MAX_SIZE = 1000000
MIN_SIZE = 1
MAX_MIRRORS = 200000
MIN_MIRRORS = 0


# Definintion for mirrors:
# M1 = /
# M2 = \

'''
	Class for horizontal lines and vertical lines
	end1 = left end for horizontal lines, upper end for vertical end
	end2 = right end for horizontal lines, bottom end for vertical end
	level = row the line is on for horizontal lines, column the line is on for vertical line
	src = we need to store whether its from emitter or detector so we can use it to prevent
				the sweep line algorithm counting intersection from same source
'''
class Line():
	def __init__(self, end1, end2, level, src):
		self.end1 = end1 if end1 < end2 else end2
		self.end2 = end2 if end2 > end1 else end1
		self.level = level
		self.src = src

	def show(self):
		return "[{}, {}], level={}, from={}".format(self.end1, self.end2, self.level, self.src)

'''
	Class for Safe
	vMirrors: Contains all the column position of all mirrors in row. Type: defaultdict(list)
	hMirrors: Contains all the row position of all mirrors in column. Type: defaultdict(list)
	r, c: boundary of the safe's 0 and r+1, c+1
	horizontals, verticals: contains all horizontal lines and vertical lines. Contains class Line()
'''
class Safe:
	def __init__(self, vMirrors, hMirrors, r, c, horizontals=[], verticals=[], source=(1, 0), dest=None):
		self.vMirrors = vMirrors # y coordinates
		self.hMirrors = hMirrors # x coordinates
		self.horizontals = horizontals
		self.verticals = verticals
		self.source = source
		self.row = r
		self.col = c
		self.dest = (self.row, self.col+1) if dest is None else dest
			
	def checkIfPossible(self):
		return self.vMirrors and self.hMirrors	# impossible if no mirrors

	def shootLaserRecursive(self, start, direction, src):
		'''
		Shoot laser from the start point in the given direction
		stores the end points of each rays
		'''
		v, h = start
		# if we have hit the boundary, exit. The condition for h and direction is
		# to handle edge case when starting from emitter or detector.
		if v == 0 or (h == 0 and direction is None) or \
			v == self.row+1 or (h == self.col+1 and direction is None):
			return (v, h)

		newPos, newDirection = self.goToMirror(start, direction)
		# Store the laser rays information
		if direction == 'R' or direction == 'L':
			newHorizontalLine = Line(h, newPos[1], v, src)
			self.horizontals.append(newHorizontalLine)
		if direction == 'U' or direction == 'D':
			newVerticalLine = Line(v, newPos[0], h, src)
			self.verticals.append(newVerticalLine)
		return self.shootLaserRecursive(newPos, newDirection, src)

	def shootLaserIterative(self, start, direction, src):
		'''
		Shoot laser from the start point in the given direction until destination reached or out of bound,
		stores the end points of each rays
		Iterative approach - better especially for large inputs, less memory on stack
		'''
		v, h = start
		# if we have hit the boundary, exit. First and last condition is for from emitter and detector,
		while not(v == 0 or (h == 0 and direction is None) or \
							v == self.row+1 or (h == self.col+1 and direction is None)):

			newPos, newDirection = self.goToMirror(start, direction)
			# Store the laser rays information
			if direction == 'R' or direction == 'L':
				newHorizontalLine = Line(h, newPos[1], v, src)
				self.horizontals.append(newHorizontalLine)
			if direction == 'U' or direction == 'D':
				newVerticalLine = Line(v, newPos[0], h, src)
				self.verticals.append(newVerticalLine)
			start = newPos
			v, h = start
			direction = newDirection

		return (v, h)


	def goToMirror(self, start, direction):
		'''
		Go to the closest mirror from start in the given direction.
		Return the new position and direction
		'''

		v, h = start
		newV, newH = None, None
		# In left, right direction, the h value must be the same, so we find
		# the closest x there is in the given direction
		if direction == 'R':				
			closest = self._findClosest(self.vMirrors[v], h, 'LARGER')
			if closest == -1: # no value is larger then the current h
				return (v, self.col+1), None
			newH, mirror = closest
		elif direction == 'L':
			closest = self._findClosest(self.vMirrors[v], h, 'SMALLER')
			if closest == -1: # no value is larger then the current h
				return (v, 0), None
			newH, mirror = closest

		# Similar idea with up, down direction except we deal with v this time
		elif direction == 'U':
			closest = self._findClosest(self.hMirrors[h], v, 'SMALLER')
			if closest == -1:
				return (0, h), None
			newV, mirror = closest
		elif direction == 'D':
			closest = self._findClosest(self.hMirrors[h], v, 'LARGER')
			if closest == -1:
				return (self.row+1, h), None
			newV, mirror = closest

		# update position
		newV = newV if newV is not None else v
		newH = newH if newH is not None else h

		# update direction
		if (direction == 'R' and mirror == 'M1') or \
			 (direction == 'L' and mirror == 'M2'):
			newDirection = 'U'
		elif (direction == 'R' and mirror == 'M2') or \
				 (direction == 'L' and mirror == 'M1'):
			newDirection = 'D'
		elif (direction == 'U' and mirror == 'M1') or \
				 (direction == 'D' and mirror == 'M2'):
			newDirection = 'R'
		elif (direction == 'U' and mirror == 'M2') or \
				 (direction == 'D' and mirror == 'M1'):
			newDirection = 'L'
		else:
			newDirection = None
		return (newV, newH), newDirection

				
	def isSafe(self):
		'''
		Check if the safe can be opened without inserting mirror
		'''
		endPos = self.shootLaserIterative(self.source, 'R', 'EMITTER') # assume emitter always on left side
		return endPos != self.dest

	def findInsertion(self, forward=False):
		# don't need to run emitting laser from emitter if already done
		if forward:
			if not self.isSafe:
				return 0
		self.shootLaserIterative(self.dest, 'L', 'DETECTOR')
		return self._sweepLines()


	def _findClosest(self, coordinates, target, mode):
		'''
		Find the smallest number larger than target or 
		largest number smaller than target depending on mode
		'''
		closest = None
		for pos in coordinates:
			val, _ = pos
			if mode == 'LARGER' and val > target:
				closest = pos if closest is None or val < closest[0] else closest
			elif mode == 'SMALLER' and val < target:
				closest = pos if closest is None or val > closest[0] else closest
		return closest if closest is not None else -1

	def _sweepLines(self):
		'''
		Run sweep line algorithm to find all the intersections
		'''
		nSolutions = 0
		bst = BST()
		# sort lines by left end and upper end
		events = []
		for line in self.horizontals:
			heappush(events, (line.end1, ['L', line.level, line.src]))
			heappush(events, (line.end2, ['R', line.level, line.src]))
		for line in self.verticals:
			heappush(events, (line.level, ['V', (line.end1, line.end2), line.src]))

		minRow, minCol = self.row+1, self.col+1

		while events:
			colPos, info = heappop(events)
			event, rowPos, source = info
			if event == 'L':
				bst.insert(rowPos, source)
			elif event == 'R':
				bst.delete(rowPos)
			elif event == 'V':
				rowUpper, rowLower = rowPos
				intersections = bst.search_in_range(rowUpper, rowLower, source)
				nSolutions += len(intersections)
				if intersections:
					# sort by row first then column to check if lexicographic smaller
					if min(intersections) <= minRow:
						minRow = min(intersections)
						minCol = min(minCol, colPos)

		return "{} {} {}".format(nSolutions, minRow, minCol) if nSolutions else "impossible"


def main(vMirrors, hMirrors, r, c):
	safe = Safe(vMirrors=vMirrors, hMirrors=hMirrors, r=r, c=c, horizontals=[], verticals=[])
	if not safe.checkIfPossible():
		return "impossible"
	if not safe.isSafe():
		return 0
	return safe.findInsertion()


if __name__ == "__main__":

	if len(sys.argv) != 2:
		print("Usage: python3 {} <input file>".format(sys.argv[0]))
		sys.exit(1)

	input_file = sys.argv[1]

	# assume input files are of correct format and 
	# same format as the task description
	lines = [line.rstrip('\n') for line in open(input_file, 'r')]
	current_line = 0
	case_number = 0
	while current_line < len(lines):

		line = lines[current_line].split(' ')
		current_line += 1

		# start new test case if it has 4 variables on that line
		if len(line) == 4:
			case_number += 1
			r, c, m, n = map(int, line)
			# init for the test case
			vMirrors = defaultdict(list)
			hMirrors = defaultdict(list)
			
			# check if inputs are valid
			if r > MAX_SIZE or r < MIN_SIZE or c > MAX_SIZE or c < MIN_SIZE:
				print("Invalid input: row or column size invalid")
				sys.exit(1)

			if m > MAX_MIRRORS or m < MIN_MIRRORS or n > MAX_MIRRORS or n < MIN_MIRRORS:
				print("Invalid input: number of mirrors is too large or too small")
				sys.exit(1)

			# Get the inputs of the mirror's row, col
			# assume all inputs are in valid range
			for i in range(m):
				ri, ci = map(int, lines[current_line].split(' '))
				vMirrors[ri].append((ci, "M1"))
				hMirrors[ci].append((ri, "M1"))
				current_line += 1

			for i in range(n):
				ri, ci = map(int, lines[current_line].split(' '))
				vMirrors[ri].append((ci, "M2"))
				hMirrors[ci].append((ri, "M2"))
				current_line += 1
			print("Case {}: {}".format(case_number, main(vMirrors=vMirrors, hMirrors=hMirrors, r=r, c=c)))


