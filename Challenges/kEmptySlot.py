

def kEmptySlot(flowers, k):

    days = [0] * len(flowers)
    # Get an list that has position as index and day they bloom as value
    for day, pos in enumerate(flowers):
        days[pos-1] = day

    print(days)
    result = 20001
    # Go through the array and at each step, check if the elements between i and i+k+1 have bloomed or not
    left = 0
    right = k+1
    i = 0
    while right < len(flowers):
        if days[i] < days[left] or days[i] <= days[right]:
            if i == right:
                result = min(result, max(days[left], days[right]))
            left, right = i, k+1+i
        i += 1
    return -1 if result == 200001 else result + 1




flowers = [1,3,2]
print(kEmptySlot(flowers, 1))
flowers = [1,3,2,4,5,10,11,12,6,7,8,9]

print(kEmptySlot(flowers, 3))

flowers = [6,5,8,9,7,1,10,2,3,4]

print(kEmptySlot(flowers, 3))