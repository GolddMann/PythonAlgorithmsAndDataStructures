
class MinHeap:
    def __init__(self, array=[]):
        self.array = array
        self.size = len(array)
        self.buildHeap()

    def isEmpty(self):
        return self.size == 0

    def buildHeap(self):
        for i in range(self.size//2, -1, -1):
            self.minHeapify(i)

    def minHeapify(self, i):
        left = 2*i + 1
        right = 2*i + 2
        minimum = i

        if left < self.size and self.array[minimum] > self.array[left]:
            minimum = left

        if right < self.size and self.array[minimum] > self.array[right]:
            minimum = right

        if minimum != i:
            self.array[minimum], self.array[i] = self.array[i], self.array[minimum]
            self.minHeapify(minimum)

    def top(self):
        if self.size > 0:
            return self.array[0]

    def push(self, value):
        self.array[self.size - 1] = self.array[0]
        self.array[0] = value
        self.minHeapify(0)
        self.array[0], self.array[self.size -
                                  1] = self.array[self.size - 1], self.array[0]
        self.size += 1

    def delete(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                self.array[i], self.array[self.size -
                                          1] = self.array[self.size - 1], self.array[i]
                self.array = self.array[:-1]
                self.size -= 1
                self.minHeapify(i)
                break

    def pop_top(self):
        if self.size > 0:
            val = self.array[0]
            self.delete(val)
            return val


minheap = MinHeap([5, 4, 3, 2, 1, 0])
while not minheap.isEmpty():
    print(minheap.pop_top())
