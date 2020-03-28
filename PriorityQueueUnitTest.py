# File: PriorityQueueUnitTest.py

"""
This file implements a simple test of the queue functionality.
"""

from unittest import UnitTest
from PriorityQueue import PriorityQueue

def PriorityQueueUnitTest():
    #test enqueue and dequeue
    UnitTest.resetErrorCount()
    q = PriorityQueue()
    UnitTest.assertTrue("q.isEmpty() -> " + str(q.isEmpty()), q.isEmpty())
    q.enqueue(1,2);
    q.enqueue(2,3);
    UnitTest.assertFalse("q.isEmpty() -> " + str(q.isEmpty()), q.isEmpty())
    v = q.dequeue();
    UnitTest.assertEquals("q.dequeue() -> " + str(v), v, 1)
    q.enqueue(3,4);
    v = q.dequeue();
    UnitTest.assertEquals("q.dequeue() -> " + str(v), v, 2)
    v = q.dequeue();
    UnitTest.assertEquals("q.dequeue() -> " + str(v), v, 3)
    UnitTest.assertTrue("q.isEmpty() -> " + str(q.isEmpty()), q.isEmpty())
    
    j = 0
    for ch in "ABCDEFGHIJKLMNOPQRSTUVXYZ":
        q.enqueue(ch,j)
        j += 1
    line = ""
    while not q.isEmpty():
        line += q.dequeue()
    UnitTest.assertEquals("line -> \"" + line + "\"", line,
                          "ABCDEFGHIJKLMNOPQRSTUVXYZ")

    #test clear
    q.clear()
    UnitTest.assertTrue("q.isEmpty() -> " + str(q.isEmpty()), q.isEmpty())


    #test len
    j = 0
    for ch in "ABCDEFGHIJKLMNOPQRSTUVXYZ":
        q.enqueue(ch,j)
        j += 1
    length = q.len()
    UnitTest.assertEquals("length -> " + str(length),length,26)
    q.clear()


    if (UnitTest.getErrorCount() == 0):
        print("QueueUnitTest succeeded")
    else:
        print("QueueUnitTest failed")
