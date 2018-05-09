def merge_intervals(intervals):
	starts = []
	ends = []
	for start, end in intervals:
		starts.append(start)
		ends.append(end)

	starts.sort()
	ends.sort()
	result = []
	i = 0
	while i < len(intervals):
		st = starts[i]
		while i < len(intervals) -1 and starts[i+1] <= ends[i]:
			i += 1
		result.append((st, ends[i]))
		i += 1
	return result





intervals =   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
print(merge_intervals(intervals))
intervals =   [(1, 2), (2, 3)]
print(merge_intervals(intervals))
intervals =   [(1, 5), (2, 3)]
print(merge_intervals(intervals))
intervals =   [(1, 10), (2, 6), (3, 5), (7, 9)]
print(merge_intervals(intervals))