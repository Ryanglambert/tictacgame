import argparse
import display


class TicTacToe(object):
    def __init__(self, grid_size, starting_player):
        self.board = self.make_board(grid_size)

    def make_board(self, grid_size):
        board = []
        for x in range(grid_size):
            board.append(["O"] * grid_size)
        return board

    def update_board(self, location, x_o):
        x, y = location
        self.board[x][y] = x_o
        display.displayBoard(self.board)


def main():
    #parse stuff here:
    # give parsed stuff to the class
    game = TicTacToe()
    # play the game maybe a while loop
    # during each while use display.py to update what is shown to the user


if __name__ == '__main__':
    main()
