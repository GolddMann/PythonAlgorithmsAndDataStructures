

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
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
            self.tail = Node(value)
            self.head.next = self.tail
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def pop_head(self):
        if self.head:
            data = self.head.data
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            return data

    def pop_tail(self):
        if not self.tail:
            return

        data = self.tail.data

        if self.tail == self.head:
            self.tail = None
            self.head = None

        else:
            cur = self.head
            while cur.next != self.tail:
                cur = cur.next
            cur.next = None

        return data

    def delete_value(self, value):
        if (self.head == self.tail and self.head.data != value) or not self.head:
            return False

        elif self.head == self.tail and self.head.data == value:
            self.head = None
            self.tail = None
            return True

        elif self.head.data == value:
            self.head = self.head.next
            return True

        node1 = self.head
        node2 = self.head.next

        while node2 and node2.data != value:
            node1 = node1.next
            node2 = node2.next

        if node2:
            if node2 == self.tail:
                node1.next = None
                self.tail = node1
            else:
                node1.next = node2.next
            return True

        return False

    def get_head(self):
        return self.head

    def __str__(self):
        nodes = []
        cur = self.head

        while cur:
            nodes.append(str(cur.data))
            cur = cur.next

        return " -> ".join(nodes)


llist = LinkedList()
llist.push_tail(2)
llist.push_tail(3)
llist.push_tail(4)
llist.delete_value(2)
llist.delete_value(3)

print(llist)  # Output: 4
