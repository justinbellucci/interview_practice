# Implement a queue ↴ with 2 stacks. Your queue should have an enqueue and 
# a dequeue method and it should be "first in first out" (FIFO).

import unittest

class Stack(object):
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()
            
class QueueTwoStacks(object):
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()
    
    def size(self):
        return self.in_stack.size() + self.out_stack.size()
    
    def is_empty(self):
        return self.size() == 0
        
    def enqueue(self, item):
        return self.in_stack.push(item) # push the item on the in_stack

    def dequeue(self):
        # if len(self.out_stack.items) == 0: # if nothing in out_stack
        if not self.out_stack.items:
            while self.in_stack.items: # while items are in in_stack
                self.out_stack.push(self.in_stack.pop()) # pop items off in_stack and push to out_stack
        
            if len(self.out_stack.items) == 0:
                raise IndexError("Can't dequeue from empty queue!")
            
        return self.out_stack.pop() 


## ------ Testing ------
class Test(unittest.TestCase):

    def test_basic_queue_operations(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        queue.enqueue(4)

        actual = queue.dequeue()
        expected = 3
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 4
        self.assertEqual(actual, expected)

    def test_error_when_dequeue_from_new_queue(self):
        queue = QueueTwoStacks()

        with self.assertRaises(Exception):
            queue.dequeue()

    def test_error_when_dequeue_from_empty_queue(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        with self.assertRaises(Exception):
            queue.dequeue()

def main():
    unittest.main(verbosity=2)

if __name__ == "__main__":
    main()