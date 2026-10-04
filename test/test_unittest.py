import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import leetcode


class TestLeetcode(unittest.TestCase):

    def test_two_sum(self):
        self.assertEqual(leetcode.two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(leetcode.two_sum([3, 3], 6), [0, 1])
        self.assertEqual(leetcode.two_sum([-3, 4, 3, 90], 0), [0, 2])
        self.assertEqual(leetcode.two_sum([1, 2, 3], 100), [])

    def test_two_sum_sorted(self):
        self.assertEqual(leetcode.two_sum_sorted([1, 2, 3, 4, 5, 6], 0, 7), [[1, 6], [2, 5], [3, 4]])
        self.assertEqual(leetcode.two_sum_sorted([1, 1, 2, 2, 3, 3], 0, 4), [[1, 3], [2, 2]])
        self.assertEqual(leetcode.two_sum_sorted([1, 2, 3, 4], 1, 5), [[2, 3]])
        self.assertEqual(leetcode.two_sum_sorted([1, 2], 0, 10), [])

    def test_three_sum(self):
        self.assertEqual(leetcode.three_sum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
        self.assertEqual(leetcode.three_sum([0, 0, 0, 0]), [[0, 0, 0]])
        self.assertEqual(leetcode.three_sum([0, 1, 1]), [])
        self.assertEqual(leetcode.three_sum([1, 2]), [])
        self.assertEqual(leetcode.three_sum([1, 2, 3, 4, 5], 9), [[1, 3, 5], [2, 3, 4]])

    def test_validate_nums(self):
        with self.assertRaises(ValueError):
            leetcode.three_sum("123")
        with self.assertRaises(ValueError):
            leetcode.two_sum([1, "a", 3], 4)


if __name__ == '__main__':
    unittest.main()
