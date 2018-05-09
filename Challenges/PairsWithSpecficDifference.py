def find_pairs_with_given_difference(arr, k):
    nums = set(arr)
    result = []
    for y in arr:
        target = y + k
        if target in nums:
            result.append([target, y])

    return result
