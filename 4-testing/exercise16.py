# In this lecture I learn about basic unit testing in Python.
# # Unit testing involves taking smaller pieces of a large program and checking that the code behaves as expected 
# # under various scenarios. A unit of code can be as simple as a small function or as complex as a large class.

import unittest

# This is an example code that is located under the test_addition.py file.
# The code defines a function that adds two numbers together and a unit test that checks if the function works correctly.

# import unittest

# def add(a, b):
#   return a + b

# class TestAddition(unittest.TestCase):
#   # Define the first unit test
#   def test_add(self):
#     result = add(3, 4)

#     # Define the expected result
#     expected_result = 7
#     self.assertEqual(result, expected_result)

# if __name__ == '__main__':
#   unittest.main()