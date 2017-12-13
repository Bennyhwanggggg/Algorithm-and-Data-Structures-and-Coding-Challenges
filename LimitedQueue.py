'''
Problem
You want to keep a limited history of the last few items seen during iteration or during
some other kind of processing.
'''

from collections import deque

# Use deque(maxlen=N)

q = deque(maxlen=4)

for i in range(1,10):
    q.append(i)

print(q) # deque([6, 7, 8, 9], maxlen=4)

'''
This method is much more efficent than manually deleting and adding off a list
'''

# To simply pop and add elements from either side:
q.appendleft(1)
print(q) # deque([1, 6, 7, 8], maxlen=4)
q.append(2)
print(q) # deque([6, 7, 8, 2], maxlen=4)
q.pop()
print(q) # deque([6, 7, 8], maxlen=4)
q.popleft()
print(q) # deque([7, 8], maxlen=4)
