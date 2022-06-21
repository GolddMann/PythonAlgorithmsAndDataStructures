import unittest
from queue import Queue


class QueueTest(unittest.TestCase):

    def test_isEmpty(self):
        myqueue = Queue()
        self.assertEqual(myqueue.isEmpty(), True, "Queue should be empty")

    def test_back(self):
        myqueue = Queue()
        myqueue.push(4)
        self.assertEqual(myqueue.back(), 4, "Should be 4")

    def test_front(self):
        myqueue = Queue()
        myqueue.push(2)
        myqueue.push(3)
        self.assertEqual(myqueue.front(), 2, "Should be 2")

    def test_pop_back(self):
        myqueue = Queue()
        myqueue.push(2)
        self.assertEqual(myqueue.pop_back(), 2, "Should be 2")
        self.assertEqual(myqueue.get_size(), 0, "Should be 0")

    def test_pop_front(self):
        myqueue = Queue()
        myqueue.push(3)
        myqueue.push(2)
        self.assertEqual(myqueue.pop_front(), 3, "Should be 3")
        self.assertEqual(myqueue.get_size(), 1, "Should be 1")

    def test_push(self):
        myqueue = Queue()
        myqueue.push(2)
        self.assertEqual(myqueue.get_size(), 1, "Should be 1")
        self.assertEqual(myqueue.back(), 2, "Should be 2")


if __name__ == "__main__":
    unittest.main()
