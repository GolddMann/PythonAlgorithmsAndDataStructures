# Time complexity: O(sqrt(n))

import math


def jumpSearch(arr, x):
    n = len(arr)
    step = math.sqrt(n)
    prev = 0

    while arr[int(min(step, n)-1)] < x:
        prev = step
        step += math.sqrt(n)  # In the beginning, we move fast
        if prev >= n:
            return -1

    while arr[int(prev)] < x:
        prev += 1       # Then, 1 element per step
        if prev == min(step, n):
            return -1

    if arr[int(prev)] == x:
        return int(prev)

    return -1


arr = [0, 1, 1, 2, 3, 5, 8, 13, 21,
       34, 55, 89, 144, 233, 377, 610]
x = 610

print(jumpSearch(arr, x))

# Output: 10
