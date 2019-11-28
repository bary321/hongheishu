# coding:utf-8

__author__ = 'bary'

import unittest
from shu import *
import random
import time

random.seed(time.time())


def rand_num():
    return random.randint(10, 100)


class MyTestCase(unittest.TestCase):
    def test_shu_find(self):
        tree = Node(10)
        self.assertEqual(tree.find(10).key, 10)
        self.assertEqual(tree.find_min().key, 10)
        self.assertEqual(tree.find_max().key, 10)

    def test_shu_insert(self):
        tree = Node(31)
        tree = insert(tree, 21)
        tree = insert(tree, 23)
        tree = insert(tree, 34)
        self.assertEqual(tree.find_min().key, 21)
        self.assertEqual(tree.find_max().key, 34)

    def test_shu_insert_2(self):
        max_num = rand_num()
        min_num = rand_num()
        delete_num = min_num
        tree = Node(min_num)
        # for i in range(rand_num()):
        for i in range(rand_num()):
            tmp = rand_num()
            if tmp > max_num:
                max_num = tmp
            if min_num == 0:
                min_num = tmp
            if tmp < min_num:
                min_num = tmp
            if rand_num() < 20:
                delete_num = tmp
            tree = insert(tree, tmp)
        show_tree(tree)
        self.assertEqual(min_num, tree.find_min().key)
        self.assertEqual(max_num, tree.find_max().key)
        tree = delete(tree, max_num)
        show_tree(tree)
        self.assertNotEquals(max_num, tree.find_max().key)
        tree = delete(tree, delete_num)
        self.assertIsNone(tree.find(delete_num))

    def test_shu_delete(self):
        tree = Node(9)
        tree = insert(tree, 11)
        tree = insert(tree, 12)
        tree = insert(tree, 13)
        tree = insert(tree, 14)
        tree = insert(tree, 15)
        tree = insert(tree, 10)
        show_tree(tree)
        tree = delete(tree, 11)
        show_tree(tree)


if __name__ == '__main__':
    unittest.main()
