'''
Heap solution
The intuition behind this solution is that earlier collisions have the potential to affect later collisions and not vice versa. 
Therefore we'd like to process collisions in the order they are happening. For this, we put each car that has a potential to collide 
with the next one in a heap and order it based on the expected collision time based on cars' positions and speed. A car that has 
collided is no longer interesting to us, since the previous car can now only collide with the car that follows it. To emulate this 
behavior we place cars in a linked list so we can easily remove the car after collision.

Complexity
Time: O(NlogN)
Space: O(N)
'''

class Car:
    def __init__(self, pos, speed, idx, prev=None, next=None):
        self.pos = pos
        self.speed = speed
        self.idx = idx
        self.prev = prev
        self.next = next

class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        colis_times = [-1] * len(cars)
        cars = [Car(pos, sp, i) for i, (pos, sp) in enumerate(cars)]
        for i in range(len(cars)-1): 
          cars[i].next = cars[i+1]
        for i in range(1, len(cars)): 
          cars[i].prev = cars[i-1]
        
        catchup_order = [((b.pos-a.pos)/(a.speed-b.speed), a.idx, a)
                        for i, (a, b) 
                        in enumerate(zip(cars, cars[1:])) if a.speed > b.speed]
        heapify(catchup_order)
        
        while catchup_order:
            catchup_time, idx, car = heappop(catchup_order)
            if colis_times[idx] > -1: continue # ith car has already caught up
            colis_times[idx] = catchup_time
            if not car.prev: continue # no car is following us
            car.prev.next, car.next.prev = car.next, car.prev
            if car.next.speed >= car.prev.speed: continue # the follower is too slow to catch up
            new_catchup_time = (car.next.pos-car.prev.pos)/(car.prev.speed-car.next.speed)
            heappush(catchup_order, (new_catchup_time, car.prev.idx, car.prev))
        
        return colis_times
    
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        result = []
        # cars that might collide with current car
        stack = []
        for position, speed in cars[::-1]:
            # if current car speed is less than the head of the stack then there won't be a collision
            # or if c1 collides with c2 after c2 collides with c3, we can ignore c2 and find collision time of c1 and c3 instead
            # (where c1 is current car, c2 is the head of the stack and c3 is the car that c2 will collide with)
            # (if we have [[x1, s1], [x2, s2]], then collision time is (x2 - x1) / (s1 - s2))
            while stack and (speed <= stack[-1][1] or (stack[-1][0] - position) / (speed - stack[-1][1]) >= stack[-1][2]):
                stack.pop()
            # if stack is empty, then current car will never collide with the next car
            if not stack:
                stack.append((position, speed, math.inf))
                result.append(-1)
            # find collision time and add the car to the stack
            else:
                collideTime = (stack[-1][0] - position) / (speed - stack[-1][1])
                stack.append((position, speed, collideTime))
                result.append(collideTime)
        result.reverse()
        return result
