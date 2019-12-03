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
        for i in range(100):
            tmp.append(random.randint(10, 1000))
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
            tree.insert(i)
            show_tree(tree.root)
        xingzhijiancha(tree)
        self.assertEqual(bst_order(tree), True)

    def test_insert4(self):
        tree = Tree()
        tmp = [384, 631, 100, 15, 715, 80, 456, 305, 836, 893, 278, 696, 663, 834, 947, 663, 353, 762, 694, 703, 258,
               916, 405, 380, 324, 637, 780, 289, 811, 496, 123, 122, 660, 224, 629, 109, 314, 571, 246, 164, 424, 403,
               943, 562, 771, 98, 975, 151, 792, 602, 700, 295, 367, 486, 480, 148, 956, 318, 523, 417, 805, 652, 367,
               467, 195, 726, 755, 10, 777, 862, 278, 450, 978, 451, 851, 688, 684, 317, 523, 104, 846, 505, 89, 966,
               941, 893, 595, 862, 57, 248, 980, 875, 165, 925, 654, 817, 138, 927, 343, 861]
        for i in tmp:
            print i, tmp.index(i)
            if i == 834:
                print
            tree.insert(i)
            show_tree(tree.root)

            check_father(tree)
            self.assertEqual(bst_order(tree), True)
            xingzhijiancha(tree)

    def test_insert5(self):
        for i in range(100):
            tree = Tree()
            tmp = []
            for i in range(100):
                tmp.append(random.randint(10, 10000))
            print tmp

            for i in tmp:
                # print i
                tree.insert(i)
            print "show"
            if tree.root:
                show_tree(tree.root)
            else:
                self.fail("root is None")
            check_father(tree)
            self.assertEqual(bst_order(tree), True)
            xingzhijiancha(tree)
            print "xinzhi"

    def test_delete0(self):
        tree = Tree()
        tree.insert(49)
        show_tree(tree.root)
        tree.delete(49)
        self.assertIsNone(tree.root)

    def test_delete1(self):
        tree = Tree()
        tree.insert(49)
        tree.insert(52)
        tree.insert(54)
        show_tree(tree.root, "bf.png")
        tree.delete(49)
        show_tree(tree.root, "af.png")
        self.assertEqual(tree.root.key, 52)
        self.assertIsNone(tree.root.left)
        self.assertEqual(tree.root.right.key, 54)
        self.assertEqual(tree.root.black, True)
        self.assertEqual(tree.root.right.black, False)

    def test_delete2_1_1(self):
        tree = Tree()
        tmp = [384, 631, 100, 15, 715, 80, 456, 305, 836, 893, 278, 696, 663, 834, 947, 663, 353, 762, 694, 703, 258,
               916, 405, 380, 324, 637, 780, 289, 811, 496, 123, 122, 660, 224, 629, 109, 314, 571, 246, 164, 424, 403,
               943, 562, 771, 98, 975, 151, 792, 602, 700, 295, 367, 486, 480, 148, 956, 318, 523, 417, 805, 652, 367,
               467, 195, 726, 755, 10, 777, 862, 278, 450, 978, 451, 851, 688, 684, 317, 523, 104, 846, 505, 89, 966,
               941, 893, 595, 862, 57, 248, 980, 875, 165, 925, 654, 817, 138, 927, 343, 861]
        for i in tmp:
            tree.insert(i)
        show_tree(tree.root)

        tmp.reverse()
        for i in tmp:
            print i
            if i == 947:
                import pdb

                # pdb.set_trace()
                pass
            tree.delete(i)
            if tree.root:
                show_tree(tree.root)
                check_father(tree)
                self.assertEqual(bst_order(tree), True)
                xingzhijiancha(tree)
        self.assertIsNone(tree.root)

    def test_delete(self):
        for i in range(1000):
            print i
            tmp = []
            for i in range(100):
                tmp.append(random.randint(10, 10000))
            print tmp
            tree = Tree()
            for i in tmp:
                tree.insert(i)
            # show_tree(tree.root)

            tmp.reverse()
            for i in tmp:
                tree.delete(i)
                if tree.root:
                    # show_tree(tree.root)
                    check_father(tree)
                    self.assertEqual(bst_order(tree), True)
                    xingzhijiancha(tree)
            self.assertIsNone(tree.root)

    def test_delete2_1_3(self):
        tree = Tree()
        tmp = [4241, 2051, 4323, 7412, 2602, 7607, 4654, 8124, 6324, 3076, 2919, 4210, 1583, 2442, 5058, 5890, 2674, 2027, 2844, 4915, 5616, 2600, 9698, 5751, 358, 4682, 4023, 4958, 9782, 1031, 5003, 8967, 7488, 4965, 4864, 8722, 7636, 1639, 1149, 782, 1566, 1919, 8489, 6095, 8613, 4828, 3385, 6836, 5633, 2091, 2663, 5462, 7937, 4445, 7242, 5084, 4587, 3347, 3076, 7002, 9681, 9657, 6337, 8693, 9603, 9378, 7448, 502, 4926, 9926, 3774, 7997, 6099, 5602, 1460, 3295, 4863, 4195, 1677, 32, 432, 9288, 5485, 2910, 7763, 5954, 9108, 8326, 6234, 376, 8502, 449, 2851, 479, 5787, 1823, 8845, 7393, 4610, 6148]
        for i in tmp:
            tree.insert(i)
        show_tree(tree.root)

        tmp.reverse()
        for i in tmp:
            print i
            if i == 358:
                import pdb

                # pdb.set_trace()
                pass
            tree.delete(i)
            if tree.root:
                show_tree(tree.root)
                check_father(tree)
                self.assertEqual(bst_order(tree), True)
                xingzhijiancha(tree)
        self.assertIsNone(tree.root)

if __name__ == '__main__':
    unittest.main()
