Heap solution
The intuition behind this solution is that earlier collisions have the potential to affect later collisions and not vice versa. Therefore we'd like to process collisions in the order they are happening. For this, we put each car that has a potential to collide with the next one in a heap and order it based on the expected collision time based on cars' positions and speed. A car that has collided is no longer interesting to us, since the previous car can now only collide with the car that follows it. To emulate this behavior we place cars in a linked list so we can easily remove the car after collision.

Complexity
Time: O(NlogN)
Space: O(N)
