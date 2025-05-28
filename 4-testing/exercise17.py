# In this lecture I learn about the TestCase class and how to use it to create unit tests in Python.
# The TestCase class is a built-in class in the unittest module that provides a framework for writing and running unit tests.
# It allows you to define test methods that check the behavior of your code and report any failures or errors.

# EXERCISE 17: Unit Testing with Strings
# Time to practice with strings! You will:

# Write test cases to validate specific behaviors.
# Use assertion methods to verify expected outcomes.
# First, let's start by creating a new string_utils.py file.

# Next, define the following functions:

# def reverse_string(s):
#   return s[::-1]

# def capitalize_string(s):
#   return s.capitalize()

# def is_capitalized(s):
#   return s[0].isupper()

# Now, let's write some unit tests. Create another Python file named test_string_utils.py.

# Then, import the three functions we defined in string_utils.py:

# Define a test class TestStringUtils that inherits from unittest.TestCase.
# Write test methods inside TestStringUtils to validate each imported function.
# Use assertion methods to test each function, including .assertEqual() and .assertTrue().

# Note: Make sure to use the if __name__ == '__main__' statement that uses unittest.main().

# Finally, run the unit tests with python3 test_string_utils.py. For the s string parameter, maybe try your name or favorite snack!

# from string_utils import reverse_string, capitalize_string, is_capitalized
# import unittest 


# class TestStringUtils(unittest.TestCase):
#     def test_reverse_string(self):
#         self.assertEqual(reverse_string("hello"), "olleh")
#         self.assertEqual(reverse_string("Python"), "nohtyP")
#         self.assertEqual(reverse_string(""), "")

#     def test_capitalize_string(self):
#         self.assertEqual(capitalize_string("hello"), "Hello")
#         self.assertEqual(capitalize_string("python"), "Python")
#         self.assertEqual(capitalize_string("HELLO"), "Hello")

#     def test_is_capitalized(self):
#         self.assertTrue(is_capitalized("Hello"))
#         self.assertFalse(is_capitalized("hello"))
#         self.assertTrue(is_capitalized("Python"))
#         self.assertFalse(is_capitalized("python"))

# if __name__ == '__main__':
#     unittest.main()