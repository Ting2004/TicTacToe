# generate tree and find targeted node
from statistics import mean

import numpy as np
from Node import Node
from Board import Board


class Tree:

    def __init__(self, root):
        self.nodes = [root]

    # traverse and generate
    def generate(self, node):

        for x in range(9):
            new_p = Node(node.p.copy(), node.turn)
            if node.p[x] == 9:
                new_p.p[x] = node.turn
                new_p.turn = 1 - new_p.turn
                node.add_child(new_p)
                self.nodes.append(new_p)

        for c in node.children:
            self.generate(c)

    def generate_a(self, node):
        b = Board(node)
        if b.check_who_wins() is None:
            for x in range(9):
                new_p = Node(node.p.copy(), node.turn)
                if node.p[x] == 9:
                    new_p.p[x] = node.turn
                    new_p.turn = 1 - new_p.turn
                    node.add_child(new_p)
                    self.nodes.append(new_p)

            for c in node.children:
                self.generate_a(c)

    def cal_chance(self, node):
        if node.children:
            for child in node.children:
                self.cal_chance(child)
            node.chance = self.get_mean_chance(node)
        else:
            b = Board(node)
            node.chance = b.check_who_wins()
            # print(b.check_who_wins())

    def find_node(self, num):
        for n in self.nodes:
            if n.counter == num:
                return n

    def get_mean_chance(self, node):
        chance = 0
        for child in node.children:
            chance += child.chance
        return chance / len(node.children)

    # find and return best child
    def find_best(self, node):
        for n in self.nodes:
            if (n.p == node.p).all() and n.turn != node.turn:
                children = n.get_children()
                break

        if node.turn == 0:
            x = -1
            index = -1
            for i in range(len(children)):
                child = children[i]
                if child.chance > x:
                    x = child.chance
                    index = i
        else:
            x = 9
            index = -1
            for i in range(len(children)):
                child = children[i]
                if child.chance < x:
                    x = child.chance
                    index = i
        return children[index]
