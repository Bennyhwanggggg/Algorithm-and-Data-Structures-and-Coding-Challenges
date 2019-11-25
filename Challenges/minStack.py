"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minStack or self.minStack[-1] >= x:
            self.minStack.append(x)

    def pop(self) -> None:
        if self.stack:
            minVal = self.stack.pop()
            if minVal == self.minStack[-1]:
                self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None       

    def getMin(self) -> int:
        return self.minStack[-1] if self.minStack else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append((x, min(self.getMin(), x)))

    def pop(self):
        self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]

    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        return sys.maxint

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append((x, min(self.getMin(), x)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return float('inf')
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
