import numpy as np
from statistics import mean


def check_who_wins(node):
    positions = node.p.reshape(3, 3)
    c1 = np.ones(3).reshape(3, 1)
    rows = np.dot(positions, c1)
    transpos = positions.T
    cols = np.dot(transpos, c1)
    if ((3 in rows) or (3 in cols)):
        return 1
    elif ((0 in rows) or (0 in cols)):
        return 0

    # diagonals
    c2 = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    mi_diagnonal = np.vdot(positions, c2)
    if (np.diagonal(positions).sum() == 3 or mi_diagnonal == 3):
        return 1
    elif (np.diagonal(positions).sum() == 0 or mi_diagnonal == 0):
        return 0

    if not (9 in positions):
        return 2

    return 9


class Node:
    def __init__(self, positions, turn):
        self.p = positions.reshape(9, 1)
        self.t = turn
        self.children = []
        self.chances = []

    def get_children(self):
        return self.children

    def print_children(self):
        for d in self.ds:
            print(d)
            print("------------")

    def get_all_chances(self):
        self.chances = []
        for c in self.children:
            self.chances.extend(c.chances)


class Tree:
    def __init__(self, root):
        self.root = root
        self.nodes = []

    def generate(self, node):
        new_p = node.p.copy()
        for x in range(9):
            if (node.p[x] == 9).all():
                new_p[x] = node.t
                node.children.append(Node(new_p, 1 - node.t))
                new_p = node.p.copy()
        if (len(node.get_children()) > 0):
            for c in node.children:
                self.nodes.append(c)
                self.generate(c)

    # return
    def traverse(self, node):
        children = node.get_children()
        for c in children:
            print(c.p)
            self.traverse(c)

        # 业务代码
        print(node)

    def cal_chance(self, node):
        result = check_who_wins(node)
        if result == 0:
            # print("0 wins")
            return 0
        elif (result == 1):
            # print("1 wins")
            return 1
        elif (result == 2):
            # print("draw")
            return 0.5
        else:
            for c in node.children:
                # print("current positions:")
                # print(c.p.reshape(3,3))
                # print("chance of winning:")
                c.chances.append(self.cal_chance(c))
            node.get_all_chances()

    def cal_final_chance(self, node):
        if (node.t == 1):
            return (mean(node.chances))
        else:
            return (1 - mean(node.chances))

    def initialize(self):
        n = Node(self.root, 1)
        t = Tree(n)
        t.generate(n)


def best_move(node):
    max = -1
    max_index = 999
    for n in whole_tree.nodes:
        if (node.p == n.p).all():
            node = n
            print(node.p)
    for i in range(len(node.chances)):
        if node.chances[i] > max:
            max = node.chances[i]
            max_index = i
    return node.children[max_index].p.reshape(3, 3)


class Result:
    draw = 2
    computer_wins = 1
    player_wins = 0


def play(turn, positions):
    if (turn == 0):
        while (True):
            val = input("(" + players[turn] + ")" + "input new position here:")
            new_pos = int(val)
            if (new_pos > 0 and new_pos < 10):
                x = (new_pos - 1) // 3
                y = (new_pos - 1) % 3
                if (positions[x, y] == 9):
                    positions[x, y] = turn

                    # !!!!!!!!!!!!
                    print(positions)
                    return positions
                else:
                    print("occupied")
            else:
                print("invalid input")
    else:
        node = Node(positions, turn)
        print(best_move(node))
        return best_move(node)


def check_win(positions):
    c1 = np.ones(3).reshape(3, 1)
    rows = np.dot(positions, c1)
    transpos = positions.T
    cols = np.dot(transpos, c1)
    if ((3 in rows) or (0 in rows) or (3 in cols) or (0 in cols)):
        return turn

    # diagonals
    c2 = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    mi_diagnonal = np.vdot(positions, c2)
    if (np.diagonal(positions).sum() == 3 or np.diagonal(
            positions).sum() == 0 or mi_diagnonal == 3 or mi_diagnonal == 0):
        return turn

    if not (9 in positions):
        return 2

    return False


def display_result(result):
    if (result == 2):
        print("draw")
    else:
        print(players[result] + " wins. Game ends.")


def show_checkboard(pos):
    signs = "XO"
    for x in range(len(pos)):
        for y in range(len(pos[0])):
            if (pos[x][y] == 9):
                print("_ ", end='')
            elif (pos[x][y] == 0):
                print("O ", end='')
            else:
                print("X ", end='')
        print("")


p = np.array([[9, 9, 9],
              [9, 9, 9],
              [9, 9, 9]])
whole_tree = Tree(p)
whole_tree.initialize()
print("initialization completed")

whole_tree.traverse(p)

# starts with first player
# the first player uses 'O' sign
players = ["player", "computer"]
positions = np.array([[9 for i in range(3)] for j in range(3)])
turn = 1

while True:
    break
    turn = 1 - turn
    positions = np.array(play(turn, positions)).reshape(3, 3)
    print(positions)
    show_checkboard(positions)
    result = check_win(positions)
    if (result != False):
        display_result(result)
        break
