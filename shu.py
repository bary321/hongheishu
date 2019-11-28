# coding:utf-8
import pygraphviz as pyg
from PIL import Image

__author__ = 'bary'


class Node:
    key = None  # type: int
    left = None  # type: Node
    right = None  # type: Node
    black = False  # type: bool

    def __init__(self, key=0):
        self.key = key

    def find(self, key):
        """

        @type key: int
        """
        if self.key == key:
            return self
        elif self.key < key:
            if self.right:
                return self.right.find(key)
            else:
                return None
        else:
            if self.left:
                return self.left.find(key)
            else:
                return None

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self

    def find_father(self, key):
        if self.key == key:
            return None
        elif self.key < key:
            if self.right:
                return self.right.find(key)
            else:
                return self
        else:
            if self.left:
                return self.left.find(key)
            else:
                return self


def insert(node, key):
    """

    @param node: Node
    @type key: int
    """
    if node.key == key:
        pass
    elif node.key < key:
        if node.right:
            node.right = insert(node.right, key)
        else:
            node.right = Node(key)
    else:
        if node.left:
            node.left = insert(node.left, key)
        else:
            node.left = Node(key)
    return node


def pop_min(node):
    """

    @type node: Node
    """
    if node.left:
        tmp = pop_min(node.left)
        node.left = tmp[0]
        return node, tmp[1]
    else:
        if node.right:
            return node.right, node.key
        else:
            return None, node.key


def delete(node, key):
    """

    @type node: Node
    """
    if node.key == key:
        if node.left and node.right:
            tmp = pop_min(node.right)
            node.right = tmp[0]
            node.key = tmp[1]
            return node
        elif not node.left and not node.right:
            return None
        else:
            if node.left:
                return node.left
            else:
                return node.right
    elif node.key < key:
        if node.right:
            node.right = delete(node.right, key)
            return node
        else:
            return node
    else:
        if node.left:
            node.left = delete(node.left, key)
            return node
        else:
            return node


def show_tree(tree):
    """

    @type tree: Node
    """
    png = "shu.png"
    g = pyg.AGraph()
    _show_tree(tree, g)
    g.layout(prog='dot')  # 绘图类型
    g.draw(png)  # 绘制

    # i = Image.open(png)
    # i.show()


def _show_tree(tree, graph):
    """

    @type graph: pyg.AGraph
    @type tree: Node
    """
    add_left = False
    add_right = False
    if tree.left:
        _show_tree(tree.left, graph)
        add_left = True
    if not tree.black:
        graph.add_node(tree.key, color='red')
    else:
        graph.add_node(tree.key)
    if add_left:
        graph.add_edge(tree.key, tree.left.key)
    if tree.right:
        _show_tree(tree.right, graph)
        add_right = True
    if add_right:
        graph.add_edge(tree.key, tree.right.key)

# if __name__ == "__main__":
#     tree = Node(1)
#     print tree.key
