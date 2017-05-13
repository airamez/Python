"""
Unit testing is a software development process in which the smallest testable parts of an application, called units,
are individually and independently scrutinized for proper operation. 
Unit testing can be done manually but is often automated.

This is a introduction to unit testing and basically we will execute the function we want to test passing 
some parameters and compare the results with values we know are the right ones. So anytime we change the code
we can just run the unit tests and check if they all pass.

There are several assertion can we can use to validate the tests and the result of those assertion will indicate if the
test pass or fail. True means PASS and False means FAIL

List of assertion:
    assertEqual(a, b)	 
    assertNotEqual(a, b)	 
    assertTrue(x) ---------------> This one could replace all the others	 
    assertFalse(x)	 
    assertIs(a, b)
    assertIsNot(a, b)
    assertIsNone(x)
    assertIsNotNone(x)
    assertIn(a, b)
    assertNotIn(a, b)
    assertIsInstance(a, b)
    assertNotIsInstance(a, b)

WARNING: There are more advanced topics in Unit Testing that we will review later.
"""
import unittest


def factorial(n: int):
    """
    Calculate the factional of a number
    :param n: n
    :return: factorial
    """
    fat = 1
    while n >= 2:
        fat *= n
        n -= 1
    return fat


class MyUnitTesting (unittest.TestCase):
    """
    Factorial Unit Testing
    """

    def test_01_fat_0(self):
        self.assertEqual(1, factorial(0), "Zero Factorial")

    def test_02_fat_1(self):
        self.assertEqual(1, factorial(1), "One Factorial")

    def test_03_fat_2(self):
        self.assertEqual(2, factorial(2))

    def test_04_fat_3(self):
        self.assertEqual(6, factorial(3))

    def test_05_fat_4(self):
        self.assertEqual(24, factorial(4))

    def test_06_fat_7(self):
        self.assertEqual(5040, factorial(7))

    def test_07_fat_12(self):
        self.assertEqual(479001600, factorial(12))

    def test_09_fat_50(self):
        self.assertEqual(30414093201713378043612608166064768844377641568960512000000000000, factorial(50))

    def test_10_fat_2_and_3(self):
        self.assertNotEqual(factorial(2), factorial(3))

    def test_11_fat_2_and_3(self):
        self.assertTrue(factorial(4) < factorial(5))

# This is the statement that executes the Unit tests
if __name__ == '__main__':
    unittest.main()
