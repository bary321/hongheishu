# coding:utf-8
from shu import Node as _Node
from honghei_err import *
from shu import show_tree

__author__ = 'bary'

__doc__ = """
    根据 https://www.jianshu.com/p/e136ec79235c 
    编程实现红黑树
    
    mail: 784378814@qq.com
"""


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
        return node


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
        # 根节点为空，直接插入
        # 情景1
        if not self.root:
            self.root = Node(key)
            self.root.black = True
            return
        father = self.root.find_father(key)
        insert_node = Node(key, father)
        insert_node.father = father

        # 当key已经存在时，father为空
        if not father:
            return
        if father.key < key:
            father.right = insert_node
        else:
            father.left = insert_node

        # 如果插入节点的父节点为黑，直接插入
        # 情景3
        if father.black:
            return

        # 父节点是红色的
        # 情景4
        while father is not self.root and father and not father.black:  # 在4.1情景下，第二次循坏时，father如果是黑的，也退出。可以和上面情景3合并
            show_tree(self.root)
            grandfather = father.father  # type: Node
            is_left = True
            # 找到叔叔节点
            if grandfather.left is father:
                uncle = grandfather.right
            else:
                is_left = False
                uncle = grandfather.left

            if uncle and not uncle.black:
                # 叔叔不为空并且是红的
                # 情景4.1
                father.black = True
                uncle.black = True
                grandfather.black = False
                insert_node = grandfather
                father = grandfather.father
            else:
                # 叔叔为空或者是黑的
                if is_left:
                    # 父节点在左边
                    # 情景4.2
                    if father.left is insert_node:
                        # 插入节点在左边
                        # 情景4.2.1
                        father.black = True
                        grandfather.black = False
                        # 在太爷那替换grandfather
                        grandgrandfather = grandfather.father
                        if grandgrandfather:
                            if grandfather is grandgrandfather.left:
                                grandgrandfather.left = right_single_rotate(grandfather)
                            else:
                                grandgrandfather.right = right_single_rotate(grandfather)
                        else:
                            self.root = right_single_rotate(grandfather)
                        break
                    else:
                        # 插入节点在右边
                        # 情景4.2.2
                        grandfather.left = left_single_rotate(father)
                        tmp = father
                        father = insert_node
                        insert_node = tmp
                        continue
                else:
                    # 父节点在右边
                    # 情景4.3
                    if father.right is insert_node:
                        # 插入节点在右边
                        # 情景4.3.1
                        father.black = True
                        grandfather.black = False
                        # 在太爷那替换grandfather
                        grandgrandfather = grandfather.father
                        if grandgrandfather:
                            if grandfather is grandgrandfather.left:
                                grandgrandfather.left = left_single_rotate(grandfather)
                            else:
                                grandgrandfather.right = left_single_rotate(grandfather)
                        else:
                            self.root = left_single_rotate(grandfather)
                        break
                    else:
                        # 插入节点在左边
                        # 情景4.3.2
                        grandfather.right = right_single_rotate(father)
                        tmp = father
                        father = insert_node
                        insert_node = tmp
                        continue

            # father = grandfather
        # 确保根节点满足性质2
        self.root.black = True  # 根节点一定是黑色的
        return

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

    if node.left and node.right:
        return left_length
    else:
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
    while node:
        if node.black:
            length += 1
        node = node.father
    return length


def insert(node, key):
    """

    @type key: int
    @type node: Node
    """
    pass
