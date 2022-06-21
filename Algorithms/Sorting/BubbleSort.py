# Time complexity: O(n^2)

# Main idea is to compare two adjust elements, and reverse if current is greater than next


def BubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if(array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]


array = [4, 5, 1, 2, 3, 51, 2, 4, 15, 125, 215, 2]
BubbleSort(array)

print(array)

# Input:  [4, 5, 1, 2, 3, 51, 2, 4, 15, 125, 215, 2]
# Output: [1, 2, 2, 2, 3, 4, 4, 5, 15, 51, 125, 215]
