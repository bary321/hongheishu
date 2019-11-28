# coding:utf-8
from shu import Node as _Node
from honghei_err import *

__author__ = 'bary'


class Node(_Node):
    father = None  # type Node

    def __init__(self, key=0, father=None):
        self.key = key
        self.father = father


def left_single_rotate(node):
    """

    @type node: Node
    """
    father = node.father
    rchild = node.right
    if rchild:
        node.right = rchild.left
        node.father = rchild
        rchild.father = father
        rchild.left = node
        return rchild
    else:
        return None


def right_single_rotate(node):
    """

    @type node: Node
    """
    father = node.father
    lchild = node.left
    if lchild:
        node.left = lchild.right
        node.father = lchild
        lchild.father = father
        lchild.right = node
        return lchild
    else:
        return node


def left_double_rotate(node):
    """

    @type node: Node
    """
    if node.right:
        node.right = right_single_rotate(node.right)
    return left_single_rotate(node)


def right_double_rotate(node):
    """

    @type node: Node
    """
    if node.left:
        node.left = left_single_rotate(node.left)
    return right_double_rotate(node)


class Tree:
    root = None  # type: Node

    def __init__(self):
        pass

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
            self.root.black = True
            return self.root
        father = self.root.find_father(key)
        uncle = None
        insert_node = Node(key, father)

        if father.black:
            if father.key < key:
                father.right = insert_node
                return father.right
            else:
                father.left = insert_node
                return father.left
        if not father:
            return None

        while father is not self.root or not father:
            grandfather = father.father  # type: Node
            is_left = True
            if grandfather.left is father:
                uncle = grandfather.right
            else:
                is_left = False
                uncle = grandfather.left
            if uncle and not uncle.black:
                father.black = True
                uncle.black = True
                grandfather.black = False
                father = grandfather.father
            else:
                if is_left:
                    if father.left is insert_node:
                        father.black = True
                        grandfather.black = False
                        if grandfather.father:
                            grandfather.father = right_single_rotate(grandfather)
                        else:
                            self.root = right_single_rotate(grandfather)
                    else:
                        grandfather.left = left_single_rotate(father)
                        insert_node = father
                        father = insert_node
                        continue

            # father = grandfather

            self.root.black = True  # 根节点一定是黑色的

    def is_none(self):
        if self.root:
            return False
        else:
            return True

    def find(self, key):
        if self.root:
            return self.root.find(key)
        else:
            return None

    def find_min(self):
        if self.root:
            return self.root.find_min()
        else:
            return None

    def find_max(self):
        if self.root:
            return self.root.find_max()
        else:
            return None


# 用来检查红黑树是否满足性质
def xingzhijiancha(tree):
    """

    @type tree: Tree
    """
    # 性质2：根节点是黑的
    if tree.root:
        if tree.root.black != True:
            raise RootNoBlack
        hong_child_black(tree.root)
        check_length(tree)
    else:
        return


# 性质4：如果一个节点是红色的，那它的子节点一定是黑的
def hong_child_black(node):
    """

    @type node: Node
    """
    if not node.black:
        if node.left:
            if not node.left.black:
                print "node:", node.key, "child not black"
                raise HongChild
        if node.right:
            if not node.left.black:
                print "node:", node.key, "child not black"
                raise HongChild
    if node.left:
        hong_child_black(node.left)
    if node.right:
        hong_child_black(node.right)


def check_length(tree):
    """

    @type tree: Tree
    """
    node = tree.root
    _check_length(node)


def _check_length(node):
    """

    @type length: int
    @type node: Node
    """
    left_length = 0
    right_length = 0
    if node.left:
        left_length = _check_length(node.left)
    if node.right:
        right_length = _check_length(node.right)
    if left_length and right_length:
        if left_length != right_length:
            print left_length, "!=", right_length, "key:", node.key
            raise LengthException()
        else:
            return left_length

    if not node.left or not node.black:
        length = get_length(node)
        if left_length:
            if length != left_length:
                print left_length, "!=", length, "key:", node.key
                raise LengthException()
            else:
                return left_length
        if right_length:
            if length != right_length:
                print right_length, "!=", length, "key:", node.key
                raise LengthException()
            else:
                return right_length
        return length


def get_length(node):
    """

    @type node: Node
    """
    length = 0
    if node.black:
        length += 1
    while node.father:
        node = node.father
        if node.black:
            length += 1
    return length


def insert(node, key):
    """

    @type key: int
    @type node: Node
    """
    pass
