
class Stack():
    def __init__(self, capacity):
        if capacity <= 0:
            raise BaseException('Capacity should be greater than 0')

        self.capacity = capacity
        self.size = 0
        self.stack = []

    def push(self, value):
        if self.size + 1 > self.capacity:
            raise BaseException('Unable to push, stack is full')
        self.stack.append(value)
        self.size += 1

    def isEmpty(self):
        return self.size == 0

    def pop(self):
        if self.isEmpty():
            raise BaseException('Stack is empty!')
        element = self.stack[-1]
        self.stack = self.stack[0:len(self.stack)-1]
        self.size -= 1
        return element

    def back(self):
        if self.isEmpty():
            raise BaseException('Stack is empty!')
        return self.stack[-1]
