import argparse
import display
from game import TicTacToe


def main():
    # parse stuff here:
    # give parsed stuff to the class
    game = TicTacToe()
    x_move = True
    while True:
        user_selection = raw_input()
        game.update_board()
    # play the game maybe a while loop
    # during each while use display.py to update what is shown to the user
        x_move = not True


if __name__ == '__main__':
    main()
