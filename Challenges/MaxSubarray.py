def maxsubarray(A):
    if not A:
        return []
    dp = [0]*len(A)
    dp[0] = A[0]
    T = [0]*len(A)
    max_sum = dp[0]
    max_start, max_end = 0, 0
    for i in range(1, len(A)):
        if dp[i-1] > 0:
            dp[i] = dp[i-1] + A[i]
            T[i] = T[i-1]
        else:
            dp[i] = A[i]
            T[i] = i
        if dp[i] > max_sum:
            max_start = T[i]
            max_end = i
            max_sum = dp[i]
    return A[max_start:max_end+1]


A = [5, 2, 3, -5, -7, 6, 7, 10, 13, 18, -3, 9]
print(maxsubarray(A), sum(maxsubarray(A)))

A = [5]
print(maxsubarray(A), sum(maxsubarray(A)))

A = [5, -2, 57, -5, -7, 6, 7, 10, 13, 18, -3, 9]
print(maxsubarray(A), sum(maxsubarray(A)))

A = [5, -2, 57, -5, -7, 6, 17, -10, 13, 2, -3, 99]
print(maxsubarray(A), sum(maxsubarray(A)))

A = [15, -2, 57, 45, -7, 6, 17, -10, 13, 2, -3, 99, -10, 2, 3, 40, 30, 11, 30, 40, 21]
print(maxsubarray(A), sum(maxsubarray(A)))

A = [-15, -2, -57, -45, -7, -6, -2]
print(maxsubarray(A), sum(maxsubarray(A)))