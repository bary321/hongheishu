# coding:utf-8
from shu import Node as _Node

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


def check_length():
    pass

def insert(node, key):
    """

    @type key: int
    @type node: Node
    """
    pass
