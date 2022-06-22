
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, value):
        if self.head == None:
            self.head = self.tail = Node(value)
        elif self.head == self.tail:
            self.head = Node(value, self.tail)
        else:
            newnode = Node(value, self.head)
            self.head = newnode

    def push_tail(self, value):
        if self.head == None:
            self.head = self.tail = Node(value)
        elif self.head == self.tail:
            self.tail = Node(value, None, self.head)
            self.head.next = self.tail
        else:
            self.tail.next = Node(value, None, self.tail)
            self.tail = self.tail.next

    def pop_head(self):
        if not self.head:
            return None

        data = self.head.data

        if self.head == self.tail:
            self.tail = None
            self.head = None

        else:
            self.head = self.head.next

        return data

    def pop_tail(self):
        if not self.tail:
            return None

        data = self.tail.data

        if self.head == self.tail:
            self.head = None
            self.tail = None

        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return data

    def delete(self, value):
        if (self.head == self.tail and self.head.data != value) or not self.head:
            return

        elif self.head == self.tail and self.head.data == value:
            self.head = None
            self.tail = None
            return True

        elif self.head.data == value:
            self.head = self.head.next
            return True

        cur = self.head.next

        while cur and cur.data != value:
            cur = cur.next

        if cur:
            cur.prev = cur.next
            return True

        return False

    def __str__(self):
        nodes = []
        cur = self.head
        while cur:
            nodes.append(str(cur.data))
            cur = cur.next
        return " -> ".join(nodes)


dllist = DoublyLinkedList()
dllist.push_head(2)
dllist.push_tail(3)
dllist.push_tail(4)
dllist.push_tail(5)
dh = dllist.pop_head()
dt = dllist.pop_tail()
dllist.delete(3)
print(dh)       # Output: 2
print(dllist)   # Output: 4
print(dt)       # Output: 5
