# Exercise 17

from string_utils import reverse_string, capitalize_string, is_capitalized
import unittest 


class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string(""), "")

    def test_capitalize_string(self):
        self.assertEqual(capitalize_string("hello"), "Hello")
        self.assertEqual(capitalize_string("python"), "Python")
        self.assertEqual(capitalize_string("HELLO"), "Hello")

    def test_is_capitalized(self):
        self.assertTrue(is_capitalized("Hello"))
        self.assertFalse(is_capitalized("hello"))
        self.assertTrue(is_capitalized("Python"))
        self.assertFalse(is_capitalized("python"))

if __name__ == '__main__':
    unittest.main()
# This code defines a set of unit tests for string utility functions.
# It uses the unittest framework to test the functions reverse_string, capitalize_string, and is_capitalized.
# Each test method checks various scenarios to ensure the functions behave as expected.