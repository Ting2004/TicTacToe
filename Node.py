# store every situation as array(1,9) and children nodes
from statistics import mean


class Node:

    counter = 0

    def __init__(self, p, turn):
        self.turn = turn
        self.p = p
        self.children = []
        self.chance = -1
        self.counter = Node.counter
        Node.counter += 1


    def switch_turn(self):
        self.turn = 1-self.turn

    def create(self):
        return


    # retrieve positions
    def get_positions(self):
        return self.p

    # retrieve children
    def get_children(self):
        return self.children

    def add_child(self, node):
        self.children.append(node)

