# Time complexity: O(n*log(n))

# Main is idea is like in merge sort, but it devides array in two arrays of random length

def quickSort(array):
    if(len(array) < 2):
        return

    last_elem = array[-1]
    j = 0

    for i in range(len(array)):
        if array[i] < last_elem:
            array[i], array[j] = array[j], array[i]
            j += 1

    array[-1], array[j] = array[j], array[-1]

    # j - intersection point

    left = array[:j]
    right = array[j:]

    quickSort(left)
    quickSort(right)

    i = j = k = 0

    while i < len(left):
        array[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


array = [3, 1, 2, 4, 12]
quickSort(array)
print(array)

# Input:  [3, 1, 2, 4, 12]
# Output: [1, 2, 3, 4, 12]
