# read user input and modify current board
# show username according to current turn

class Player:

    def __init__(self, name):
        self.name = name

    # read user input
    def user_input(self, board):
        while True:
            val = input("(" + self.name + ")" + "input new position here:")
            new_pos = int(val)
            if new_pos > 0 and new_pos < 10:
                if board.node.p[new_pos-1] == 9:
                    return new_pos
                else:
                    print("occupied")
            else:
                print("invalid input")
