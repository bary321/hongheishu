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

    def test_get_length(self):
        tree = Node(20)
        tree.left = Node(11, tree)
        tree.right = Node(25, tree)
        tree.right.left = Node(23, tree.right)
        tree.right.right = Node(30, tree.right)
        t = Tree()
        t.root = tree

        tree.black = True
        tree.left.black = True
        tree.right.black = True

        show_tree(tree)
        self.assertEqual(get_length(tree.left), get_length(tree.right.left))
        tree.right.right.black = True
        self.assertRaises(LengthException, check_length, t)
        tree.right.black = False
        show_tree(tree)
        self.assertRaises(HongChild, hong_child_black, tree)


if __name__ == '__main__':
    unittest.main()
