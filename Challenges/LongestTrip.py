from collections import defaultdict
class Distance:
	def __init__(self):
		self.map = []

	def calculate(self, input):
		p1, p2, dist = input.split(':')
		if min(p1, p2) == p2:
			p1, p2 = p2, p1
		self.map.append(('{}@@{}'.format(p1, p2), int(dist)))
		self.map.sort(key=lambda x: x[1])
		
		if len(self.map) < 2:
			return None

		route, longest_trip = set(), 0

		longest, second_longest = 0, 1
		while longest != len(self.map):
			first = self.map[longest]
			first_edge, first_distance = first[0].split('@@'), first[1]
			while second_longest < len(self.map) and \
						((first_edge[0] not in self.map[second_longest][0].split('@@') and \
						first_edge[1] not in self.map[second_longest][0].split('@@')) or \
						first_edge == self.map[second_longest][0].split('@@')):
						second_longest += 1
			if second_longest == len(self.map):
				longest += 1
				continue

			second_edge, second_distance = self.map[second_longest][0].split('@@'), self.map[second_longest][1]

			connection = first_edge[0] if first_edge[0] in second_edge else first_edge[1]
			if first_distance + second_distance > longest_trip:
				longest_trip = first_distance + second_distance
				route = set(first_edge + second_edge)
			longest += 1

		return (route, longest_trip)





if __name__ == '__main__':
	
	map = Distance()
	print(map.calculate('CHI:NYC:719'))
	print(map.calculate('NYC:LA:2414'))
	print(map.calculate('NYC:SEATTLE:2448'))
	print(map.calculate('NYC:HAWAII:4924'))
