# coding:utf-8

__author__ = 'bary'

import pygraphviz as pyg
from PIL import Image
import time

g = pyg.AGraph()  # 建立图
g.add_node('A')  # 建立点
g.add_edge('A', 'B')  # 建立边
g.add_edge('A', 'C')  # 建立边
g.layout(prog='dot')  # 绘图类型
g.draw('pyg1.png')  # 绘制
i = Image.open('pyg1.png')
i.show()
time.sleep(2)
i.close()
