"""
Given an Iterator with methods:

interface Iterator<E> {
	/**
	* Returns true if the iteration has more elements.
	*/
    boolean hasNext();

	/**
	* Returns the next element in the iteration.
	*/
    E next();
}
Design and implement a SkipIterator that support the skip(int num) operation:

class SkipIterator implements Iterator<Integer> {
	// if there's no iterators in your language the input can be just an array
	public SkipIterator(Iterator<Integer> it) {
	}

	public boolean hasNext() {
	}

	public Integer next() {
	}

	/**
	* The input parameter is an int, indicating that the next element equals 'num' needs to be skipped.
	* This method can be called multiple times in a row. skip(5), skip(5) means that the next two 5s should be skipped.
	*/ 
	public void skip(int num) {
	}
}
Example:

SkipIterator itr = new SkipIterator([2, 3, 5, 6, 5, 7, 5, -1, 5, 10]);
itr.hasNext(); // true
itr.next(); // returns 2
itr.skip(5);
itr.next(); // returns 3
itr.next(); // returns 6 because 5 should be skipped
itr.next(); // returns 5
itr.skip(5);
itr.skip(5);
itr.next(); // returns 7
itr.next(); // returns -1
itr.next(); // returns 10
itr.hasNext(); // false
"""

from collections import defaultdict, deque

class SkipIterator:
    def __init__(self, nums):
        self.nums = deque(nums)
        self.cnt = defaultdict(int)

    def hasNext(self):
      self._skip()
      return len(self.nums) > 0
    
    def skip(self, i):
      self.cnt[i] += 1

    def next(self):
      if not self.hasNext():
        return None

      return self.nums.popleft()

    def _skip(self):
      while len(self.nums) > 0 and self.nums[0] in self.cnt:
        self.cnt[self.nums[0]] -= 1

        if self.cnt[self.nums[0]] == 0:
          del self.cnt[self.nums[0]]

        self.nums.popleft()