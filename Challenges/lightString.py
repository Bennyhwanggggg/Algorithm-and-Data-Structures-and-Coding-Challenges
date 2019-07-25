class LightString:
	def __init__(self, numOfLights):
		self.lights = [False]*numOfLights

	def isOn(self, i):
		return self.lights[i]

	def toggle(self, start, end):
		for i in range(start, end+1):
			self.lights[i] = not self.lights[i]

# Using Segment Tree
class SegmentTreeNode(object):
    def __init__(self, start, end, val):
        self.start = start
        self.end = end
        self.sum = val
        self.left = None
        self.right = None

    def updateTree(self, index, val):
        if self.start == self.end == index:
            self.sum += val
            return

        mid = (self.start + self.end) // 2

        if index <= mid:
            self.left.updateTree(index, val)
        else:
            self.right.updateTree(index, val)

        self.sum = self.left.sum + self.right.sum


class LightString:

    def __init__(self, num):
        self.root = self.buildTree(0, num, [0] * (num + 1))

    def buildTree(self, start, end, vals):
        if start == end:
            return SegmentTreeNode(start, end, vals[start])

        mid = (start + end) // 2
        left = self.buildTree(start, mid, vals)
        right = self.buildTree(mid + 1, end, vals)

        cur = SegmentTreeNode(start, end, left.sum + right.sum)
        cur.left = left
        cur.right = right

        return cur

    def query(self, root, i, j):

        if root.start == i and root.end == j:
            return root.sum

        mid = (root.start + root.end) // 2

        if j <= mid:
            return self.query(root.left, i, j)
        elif i > mid:
            return self.query(root.right, i, j)
        else:
            return self.query(root.left, i, mid) + self.query(root.right, mid + 1, j)

    def toggle(self, start, end):
        self.root.updateTree(start, 1)
        self.root.updateTree(end + 1, -1)

    def isOn(self, x):
        return self.query(self.root, 0, x) % 2 != 0


if __name__ == '__main__':
	lightString = LightString(5)
	assert lightString.isOn(0) == False
	assert lightString.isOn(1) == False
	assert lightString.isOn(2) == False
	lightString.toggle(0, 2)
	assert lightString.isOn(0) == True
	assert lightString.isOn(1) == True
	assert lightString.isOn(2) == True
	assert lightString.isOn(3) == False
	lightString.toggle(1, 3)
	assert lightString.isOn(1) == False
	assert lightString.isOn(2) == False
	assert lightString.isOn(3) == True