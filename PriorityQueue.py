#File: PriorityQueue.py

# This file implements a PriorityQueue class, which employs an array-based heap to organise
# data by priority in a binary tree.

from array import Array

_INITIAL_CAPACITY_ = 10

class PriorityQueue:

    def __init__(self):
        self._capacity = _INITIAL_CAPACITY_
        self._head = None
        self._tail = None
        self._array = Array(_INITIAL_CAPACITY_)

    #enters a new node into the queue. nodes with higher priority go earlier into the queue
    def enqueue(self, value, priority):
        #expand if we intend to go beyond capacity
        if self._tail == self._capacity:
            self._expand()
        newNode = Node(value,priority)
        if self._head == None:
            self._head = 0
            self._tail = 1
            self.array[0] = newNode
        else:
            #check if the node we want to add is a higher priority than its parent
            child = self._tail
            parent = (self._tail - 1) // 2
            self._array[child] = newNode
            while (newNode._priority < self._array[parent]._priority) and (parent >= 0):
                self._array[child],self._array[parent] = self._array[parent],self._array[child]
                child = parent
                parent = (parent - 1 // 2)
            self._tail += 1

    #removes the value at the head of the queue and returns it
    def dequeue(self):
        if self._head == None:
            raise IndexError("Queue is empty")
        else:
            ret = self._array[self._head]._value
            self._array[self._head] = self._array[self._tail]
            self._array[self._tail] = None
            parent = self._head
            child1 = 2 * parent + 1
            child2 = 2 * parent + 2
            while (self._array[parent]._priority > self._array[child1]._priority) or (self._array[parent]._priority > self._array[child2].priority):
                if (self._array[parent]._priority > self._array[child1]._priority):
                    switch = child1
                else:
                    switch = child2
                self._array._parent,self._array._switch = self._array._switch, self._array._parent
            self._tail -= 1
        return ret



    #returns True if the priority queue is empty
    def isEmpty(self):
        return self._head == None

    #returns the number of elements in the queue
    def __len__(self):
        return self._tail

    #
    def clear(self):
        self._head == None
        self._tail == None
        for element in range(0,len(self._array)):
            self._array[element] = None

    def _expand(self):
        oldCapacity = self._capacity
        oldIndex = self._head
        self._capacity *= 2
        newQueue = PriorityQueue(self._capacity)
        newIndex = 0
        while oldIndex != self._tail:
            newArray[newIndex] = self._array[oldIndex]
            oldIndex = (oldIndex + 1) % oldCapacity
            newIndex += 1
        self._array = newArray
        self._head = 0
        self._tail = newIndex


class Node:

    '''a node class to be used with a priority queue. each node carries a priority for placement in a queue'''

    def __init__(self, value, priority):
        self._value = value
        self._priority = priority

# Startup code

if __name__ == "__main__":
    import PriorityQueueUnitTest
    PriorityQueueUnitTest.PriorityQueueUnitTest()