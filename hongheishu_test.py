# coding:utf-8

__author__ = 'bary'

import unittest
from hongheishu import *
from shu import show_tree
import random
import time

random.seed(time.time())


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

    def test_insert(self):
        tree = Tree()
        tree.insert(20)
        tree.insert(11)
        tree.insert(25)
        tree.insert(23)
        tree.insert(30)
        tree.insert(40)
        tree.insert(50)
        if tree.root:
            show_tree(tree.root)
        else:
            self.fail("root is None")
        xingzhijiancha(tree)

    def test_insert2(self):
        tree = Tree()
        tmp = []
        for i in range(10):
            tmp.append(random.randint(10, 100))
        print tmp

        for i in tmp:
            print i
            tree.insert(i)
        print "show"
        if tree.root:
            show_tree(tree.root)
        else:
            self.fail("root is None")
        xingzhijiancha(tree)
        print "xinzhi"

    def test_insert3(self):
        tree = Tree()
        tmp = [71, 96, 73, 27, 64, 82, 79, 26, 73, 78]
        for i in tmp:
            if i == 73:
                print
            tree.insert(i)
        if tree.root:
            show_tree(tree.root)
        else:
            self.fail("root is None")
        xingzhijiancha(tree)


if __name__ == '__main__':
    unittest.main()
