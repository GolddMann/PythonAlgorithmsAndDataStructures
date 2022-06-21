# Time complexity: O(log(n))

# Binary is working right only for sorted arrays
# Main idea is to devide range of finding

def BinarySearch(array, key):
    left = 0
    right = len(array) - 1
    while(left <= right):
        mid = left + (right - left)//2  # get middle of finding range
        if(array[mid] == key):
            return mid
        elif(array[mid] > key):
            right = mid - 1     # now range of finding is from left to mid - 1
        else:
            left = mid + 1      # now range of finding is from mid + 1 to right
    return None


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
key = 10

print(BinarySearch(array, key))
