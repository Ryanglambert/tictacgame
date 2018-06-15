import argparse
import display

from game import TicTacToe


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", help="User plays as the Os", action='store_true')
    parser.add_argument("-x", help="User plays as the Xs", action='store_true')
    args = parser.parse_args()
    player = ''
    if args.o:
       player = 'o'
    elif args.x:
       player = 'x'

    print("Playing with: ", player)
    game = TicTacToe(3, player)
    while True:
        display.displayBoard(game.board)
        col, row = input('Please choose a move: (i.e. \'00\')')
        col, row = int(col), int(row)
        print(col)
        print(row)
        game.update_board((col, row), player)
        # opponent's move


if __name__ == '__main__':
    main()
