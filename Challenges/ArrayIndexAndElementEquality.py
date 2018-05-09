def index_equals_value_search(arr):
    '''
    for i in range(len(arr)):
      if i == arr[i]:
        return i
    return -1
    '''

    if len(arr) == 1:
        if arr[0] == 0:
            return 0
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if mid == arr[mid]:
            return mid
        elif arr[mid] > mid:
            end = mid - 1
        elif arr[mid] < mid:
            start = mid + 1
    return -1