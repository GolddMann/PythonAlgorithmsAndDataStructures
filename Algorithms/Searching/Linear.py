# Time complexity: O(n)

# Main idea is to go through the array from left to right until we hit a desired element


def LinearSearch(array, key):
    for index, element in enumerate(array):
        if element == key:
            return index
    return None


array = [4, 5, 1, 2, 3, 51, 2, 4, 15, 125, 215, 2]

value = 1

index = LinearSearch(array, value)

if index is not None:
    print('%d is founded at index %d' % (value, index))
else:
    print('%d is not founded' % value)

# Input: 1
# Output: 1 is founded at index 2 (first 1 from left to right is at second index)

#Input: 0
#Output: 0 is not founded
