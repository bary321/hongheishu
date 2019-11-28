# coding:utf-8

__author__ = 'bary'

import unittest
from hongheishu import *
from shu import show_tree


class MyTestCase(unittest.TestCase):
    def test_rotate(self):
        tree = Node(20)
        tree.left = Node(11, tree)
        tree.right = Node(25, tree)
        tree.right.left = Node(23, tree.right)
        tree.right.right = Node(30, tree.right)
        show_tree(tree)
        tree = left_single_rotate(tree)
        show_tree(tree)
        tree = right_single_rotate(tree)
        show_tree(tree)


if __name__ == '__main__':
    unittest.main()
