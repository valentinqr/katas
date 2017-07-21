import unittest

from chops import iterative_chop, recursive_chop, builtin_chop


class TestChops(unittest.TestCase):

    def test_iterative_chop(self):
        self.assertEqual(-1, iterative_chop(3, []))
        self.assertEqual(-1, iterative_chop(3, [1]))
        self.assertEqual(0, iterative_chop(1, [1]))
        self.assertEqual(0, iterative_chop(1, [1, 3, 5]))
        self.assertEqual(1, iterative_chop(3, [1, 3, 5]))
        self.assertEqual(2, iterative_chop(5, [1, 3, 5]))
        self.assertEqual(-1, iterative_chop(0, [1, 3, 5]))
        self.assertEqual(-1, iterative_chop(2, [1, 3, 5]))
        self.assertEqual(-1, iterative_chop(4, [1, 3, 5]))
        self.assertEqual(-1, iterative_chop(6, [1, 3, 5]))
        self.assertEqual(0, iterative_chop(1, [1, 3, 5, 7]))
        self.assertEqual(1, iterative_chop(3, [1, 3, 5, 7]))
        self.assertEqual(2, iterative_chop(5, [1, 3, 5, 7]))
        self.assertEqual(3, iterative_chop(7, [1, 3, 5, 7]))
        self.assertEqual(-1, iterative_chop(0, [1, 3, 5, 7]))
        self.assertEqual(-1, iterative_chop(2, [1, 3, 5, 7]))
        self.assertEqual(-1, iterative_chop(4, [1, 3, 5, 7]))
        self.assertEqual(-1, iterative_chop(6, [1, 3, 5, 7]))
        self.assertEqual(-1, iterative_chop(8, [1, 3, 5, 7]))

    def test_builtin_chop(self):
        self.assertEqual(-1, builtin_chop(3, []))
        self.assertEqual(-1, builtin_chop(3, [1]))
        self.assertEqual(0, builtin_chop(1, [1]))
        self.assertEqual(0, builtin_chop(1, [1, 3, 5]))
        self.assertEqual(1, builtin_chop(3, [1, 3, 5]))
        self.assertEqual(2, builtin_chop(5, [1, 3, 5]))
        self.assertEqual(-1, builtin_chop(0, [1, 3, 5]))
        self.assertEqual(-1, builtin_chop(2, [1, 3, 5]))
        self.assertEqual(-1, builtin_chop(4, [1, 3, 5]))
        self.assertEqual(-1, builtin_chop(6, [1, 3, 5]))
        self.assertEqual(0, builtin_chop(1, [1, 3, 5, 7]))
        self.assertEqual(1, builtin_chop(3, [1, 3, 5, 7]))
        self.assertEqual(2, builtin_chop(5, [1, 3, 5, 7]))
        self.assertEqual(3, builtin_chop(7, [1, 3, 5, 7]))
        self.assertEqual(-1, builtin_chop(0, [1, 3, 5, 7]))
        self.assertEqual(-1, builtin_chop(2, [1, 3, 5, 7]))
        self.assertEqual(-1, builtin_chop(4, [1, 3, 5, 7]))
        self.assertEqual(-1, builtin_chop(6, [1, 3, 5, 7]))
        self.assertEqual(-1, builtin_chop(8, [1, 3, 5, 7]))

    def test_recursive_chop(self):
        self.assertEqual(-1, recursive_chop(3, []))
        self.assertEqual(-1, recursive_chop(3, [1]))
        self.assertEqual(0, recursive_chop(1, [1]))
        self.assertEqual(0, recursive_chop(1, [1, 3, 5]))
        self.assertEqual(1, recursive_chop(3, [1, 3, 5]))
        self.assertEqual(2, recursive_chop(5, [1, 3, 5]))
        self.assertEqual(-1, recursive_chop(0, [1, 3, 5]))
        self.assertEqual(-1, recursive_chop(2, [1, 3, 5]))
        self.assertEqual(-1, recursive_chop(4, [1, 3, 5]))
        self.assertEqual(-1, recursive_chop(6, [1, 3, 5]))
        self.assertEqual(0, recursive_chop(1, [1, 3, 5, 7]))
        self.assertEqual(1, recursive_chop(3, [1, 3, 5, 7]))
        self.assertEqual(2, recursive_chop(5, [1, 3, 5, 7]))
        self.assertEqual(3, recursive_chop(7, [1, 3, 5, 7]))
        self.assertEqual(-1, recursive_chop(0, [1, 3, 5, 7]))
        self.assertEqual(-1, recursive_chop(2, [1, 3, 5, 7]))
        self.assertEqual(-1, recursive_chop(4, [1, 3, 5, 7]))
        self.assertEqual(-1, recursive_chop(6, [1, 3, 5, 7]))
        self.assertEqual(-1, recursive_chop(8, [1, 3, 5, 7]))
