class Queue():

    def __init__(self):
        self.size = 0
        self.queue = []

    def isEmpty(self):
        return self.size == 0

    def push(self, value):
        self.queue.append(value)
        self.size += 1

    def back(self):
        if self.isEmpty():
            raise 'Queue is empty!'
        return self.queue[-1]

    def front(self):
        if self.isEmpty():
            raise 'Queue is empty!'
        return self.queue[0]

    def get_size(self):
        return self.size

    def pop_front(self):
        if self.isEmpty():
            raise 'Queue is empty!'
        value = self.queue[0]
        self.queue = self.queue[1:]
        self.size -= 1
        return value

    def pop_back(self):
        if self.isEmpty():
            raise 'Queue is empty!'
        value = self.queue[-1]
        self.queue = self.queue[0:len(self.queue)-1]
        self.size -= 1
        return value
