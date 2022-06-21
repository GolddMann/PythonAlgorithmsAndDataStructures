
def insertion_sort(array):
    for i in range(len(array)-1):
        if(array[i] > array[i+1]):
            j = i + 1
            while j > 0 and array[j - 1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
                j -= 1


array = [4, 1, 5, 1, 2]
insertion_sort(array)
print(array)
# Output: [1,1,2,4,5]
