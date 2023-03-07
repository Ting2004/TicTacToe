# run here
import pickle

import numpy as np

from Board import Board
from Node import Node
from Player import Player
from Tree import Tree

turn = 0
players = ["computer", "player"]
init = np.array([9, 9, 9, 9, 9, 9, 9, 9, 9])
root = Node(init, turn)


def create_tree():
    tree = Tree(root)
    tree.generate_a(root)
    print("initialization completed")
    tree.cal_chance(root)
    print("initialization completed")

    file = open("d:\\tree.txt", 'wb')
    pickle.dump(tree, file)
    file.close()
    print("stored")

def load_tree():
    tree = pickle.load(open("d:\\tree.txt", 'rb'))
    return tree

#create_tree()
tree = load_tree()

x = tree.find_node(2499686)

board = Board(root)
playerA = Player("player")
while True:
    if turn == 1:
        board = board.player_play(playerA.user_input(board))
        board.display()
        print("")
    else:
        new_node = tree.find_best(board.node)
        board = board.computer_play(new_node)
        board.display()

    turn = 1 - turn
    result = board.check_who_wins()
    if result is not None:
        if result == 1 or result == 0:
            print(players[1-turn]+" wins")
        else:
            print("draw")
        print("game ends")
        break

