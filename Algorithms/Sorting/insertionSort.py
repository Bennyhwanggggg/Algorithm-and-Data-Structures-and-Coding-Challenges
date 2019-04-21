'''
Insertion Sort Algorithm

by Benny Hwang 29/12/2017
'''

# Input: array of numbers, if not numbers, function will return nothing
def insertionSort(data):
	if any(type(n)!=type(1) for n in data):
		return;

	for i in range(len(data)):
		element = data[i]
		j = i-1;
		while j>=0 and data[j]>element:
			data[j+1] = data[j]
			j -= 1
		data[j+1] = element

	return data



