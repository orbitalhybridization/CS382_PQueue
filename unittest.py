# File: unittest.py

"""
The UnitTest class exports several static methods that are compatible
with the JUnit framework used for Java.
"""

# Code to ensure that imported modules can come from the current directory

import os
import sys
sys.path.insert(0, os.getcwd())

# Constants 

RADIUS = 1.0E-15
UNSPECIFIED = [ "Unspecified" ]

class UnitTest(object):

    @classmethod
    def assertTrue(cls, msg, exp=UNSPECIFIED):
        """
        Checks that the boolean condition is True.
        """
        if exp is UNSPECIFIED:
            exp = msg
            msg = "Failure: " + str(exp) + " != True"
        if exp != True:
            cls.errorCount += 1
            print(msg)

    @classmethod
    def assertFalse(cls, msg, exp=UNSPECIFIED):
        """
        Checks that the boolean condition is False.
        """
        if exp is UNSPECIFIED:
            exp = msg
            msg = "Failure: " + str(exp) + " != False"
        if exp != False:
            cls.errorCount += 1
            print(msg)

    @classmethod
    def assertEquals(cls, msg, exp1, exp2=UNSPECIFIED):
        """
        Tests that two values are equal.
        """
        if exp2 is UNSPECIFIED:
            exp2 = exp1
            exp1 = msg
            msg = "Failure: " + str(exp1) + " != " + str(exp2)
        if exp1 is None or exp2 is None:
            cls.assertTrue(msg, exp1 is exp2)
        elif type(exp1) is float or type(exp2) is float:
            r = max(abs(exp1), abs(exp2)) * RADIUS
            cls.assertTrue(msg, abs(d1 - d2) <= r)
        else:
            cls.assertTrue(msg, exp1 == exp2)

    @classmethod
    def assertNotEquals(cls, msg, exp1, exp2=UNSPECIFIED):
        """
        Tests that two values are not equal.
        """
        if exp2 is UNSPECIFIED:
            exp2 = exp1
            exp1 = msg
            msg = "Failure: " + str(exp1) + " == " + str(exp2)
        if exp1 is None or exp2 is None:
            cls.assertTrue(msg, exp1 is not exp2)
        elif type(exp1) is float or type(exp2) is float:
            r = max(abs(exp1), abs(exp2)) * RADIUS
            cls.assertFalse(msg, abs(d1 - d2) <= r)
        else:
            cls.assertFalse(msg, exp1 == exp2)

    @classmethod
    def assertNone(cls, msg, exp=UNSPECIFIED):
        """
        Checks that the expression is None.
        """
        if exp is UNSPECIFIED:
            exp = msg
            msg = "Failure: " + str(exp) + " is not None"
        cls.assertEquals(msg, exp, None)

    @classmethod
    def assertNotNone(cls, msg, exp=UNSPECIFIED):
        """
        Checks that the expression is not None.
        """
        if exp is UNSPECIFIED:
            exp = msg
            msg = "Failure: " + str(exp) + " is None"
        cls.assertNotEquals(msg, exp, None)

    @classmethod
    def assertSame(cls, msg, exp1, exp2=UNSPECIFIED):
        """
        Tests that two values are identical.
        """
        if exp2 is UNSPECIFIED:
            exp2 = exp1
            exp1 = msg
            msg = "Failure: " + str(exp1) + " is not " + str(exp2)
        if exp1 is None or exp2 is None:
            cls.assertTrue(msg, exp1 is exp2)
        else:
            cls.assertTrue(msg, exp1 is exp2)

    @classmethod
    def assertDifferent(cls, msg, exp1, exp2=UNSPECIFIED):
        """
        Tests that two values are different.
        """
        if exp2 is UNSPECIFIED:
            exp2 = exp1
            exp1 = msg
            msg = "Failure: " + str(exp1) + " is " + str(exp2)
        if exp1 is None or exp2 is None:
            cls.assertTrue(msg, exp1 is not exp2)
        else:
            cls.assertTrue(msg, exp1 is not exp2)

    @classmethod
    def resetErrorCount(cls):
        """
        Resets the current error count to zero.
        """
        cls.errorCount = 0

    @classmethod
    def getErrorCount(cls):
        """
        Returns the current error count.
        """
        return cls.errorCount

# Class variables 

    errorCount = 0

# Self test

if __name__ == "__main__":
    print("unittest.py parses successfully")
