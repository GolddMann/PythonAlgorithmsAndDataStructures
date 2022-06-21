from stack import Stack

mystack = Stack(4)
mystack.push(4)


def test_back(mystack):
    assert mystack.back() == 4, "Should be 4"


def test_empty(mystack):
    assert mystack.isEmpty(), "Should be empty"


def test_pop(mystack):
    assert mystack.pop() == 4, "Should be 4"
    test_empty(mystack)


if __name__ == "__main__":
    stack = Stack(4)
    stack.push(4)
    test_back(stack)
    test_pop(stack)
    print("Everything passed")
