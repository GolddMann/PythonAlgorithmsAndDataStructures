# Time complexity: O(n*log(n))

# Main idea is to sort array by parts
# We devide array in two equal parts
# Devide theese parts (until part is 1 length array)
# Sort them
# Unite them

def merge_sort(array):
    if len(array) > 1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


array = [3, 1, 2]

merge_sort(array)

print(array)

# Input: [3,1,2]
# Output: [1,2,3]
