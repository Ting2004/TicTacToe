# store current board and check if wins
import numpy as np


class Board:
    def __init__(self, node):
        self.node = node

    # display
    def display(self):
        signs = "XO"
        p = self.node.p.reshape(3, 3)
        for x in range(3):
            for y in range(2):
                if p[x][y] == 9:
                    print("   |", end='')
                elif p[x][y] == 0:
                    print(" O |", end='')
                else:
                    print(" X |", end='')
            if p[x][2] == 9:
                print("   ", end='')
            elif p[x][2] == 0:
                print(" O ", end='')
            else:
                print(" X ", end='')
            print("")


    # check if available and modify
    def player_play(self, new_pos):
        self.node.p[new_pos-1] = self.node.turn
        print(self.node.counter)
        return self


    def computer_play(self, node):
        self.node = node
        print(self.node.counter)
        return self

    # check who wins
    def check_who_wins(self):
        positions = self.node.p.reshape(3, 3)
        c1 = np.ones(3).reshape(3, 1)
        rows = np.dot(positions, c1)
        transpose = positions.T
        cols = np.dot(transpose, c1)
        if (3 in rows) or (3 in cols):
            return 1
        elif (0 in rows) or (0 in cols):
            return 0

        # diagonals
        c2 = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
        mi_diagonal = np.vdot(positions, c2)
        if np.diagonal(positions).sum() == 3 or mi_diagonal == 3:
            return 1
        elif np.diagonal(positions).sum() == 0 or mi_diagonal == 0:
            return 0
        if not (9 in positions):
            return 0.5
        return None