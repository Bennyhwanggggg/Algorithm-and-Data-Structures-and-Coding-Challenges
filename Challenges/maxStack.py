"""
Max Stack
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.
"""

"""
A regular stack already supports the first 3 operations and max heap can take care of the last two. But the main issue is when popping an element form the top of one data structure how can we efficiently remove that element from the other. We can use lazy removal (similar to Approach #2 from 480. Sliding Window Median) to achieve this is in average O(log N) time.
"""
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.maxHeap = []
        self.toPop_heap = {} #to keep track of things to remove from the heap
        self.toPop_stack = set() #to keep track of things to remove from the stack

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        heapq.heappush(self.maxHeap, (-x,-len(self.stack)))
        self.stack.append(x)
        
    def pop(self):
        """
        :rtype: int
        """             
        self.top()
        x = self.stack.pop()
        key = (-x,-len(self.stack))
        self.toPop_heap[key] = self.toPop_heap.get(key,0) + 1
        return x

    def top(self):
        """
        :rtype: int
        """
        while self.stack and len(self.stack)-1 in self.toPop_stack:
            x = self.stack.pop()
            self.toPop_stack.remove(len(self.stack))
        return self.stack[-1]
        
    def peekMax(self):
        """
        :rtype: int
        """
        while self.maxHeap and self.toPop_heap.get(self.maxHeap[0],0):
            x = heapq.heappop(self.maxHeap)
            self.toPop_heap[x] -= 1
        return -self.maxHeap[0][0]

    def popMax(self):
        """
        :rtype: int
        """
        self.peekMax()
        x,idx = heapq.heappop(self.maxHeap)
        x,idx = -x,-idx
        self.toPop_stack.add(idx)
        return x


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

