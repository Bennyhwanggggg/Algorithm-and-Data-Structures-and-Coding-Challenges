# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# real iterator
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [[nestedList, 0]]

    def next(self):
        """
        :rtype: int
        """
        self.hasNext()
        nestedList, i = self.stack[-1]
        self.stack[-1][1] += 1
        return nestedList[i].getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            nestedList, i = self.stack[-1]
            if i == len(nestedList):
                self.stack.pop()
            else:
                x = nestedList[i]
                if x.isInteger():
                    return True
                self.stack[-1][1] += 1
                self.stack.append([x.getList(), 0])
        return False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())





"""
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.
"""
# recursively unpack nested list
def unpack(nestedList):
    l = []
    for el in nestedList:
        # simply concatenate if the element is an integer
        el_int = el.getInteger()
        if el_int is not None:
            l += [el_int]
        # recursively unpack if the element is a list
        el_list = el.getList()
        if el_list is not None:
            l += unpack(el_list)
    return l
        
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        """
        self.vals = unpack(nestedList)
        # at this point self.vals already holds the desired output from the iterator
        self.i = 0
        
    def next(self):
        """
        :rtype: int
        """
        self.i += 1
        return self.vals[self.i-1]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i != len(self.vals)
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
