import argparse


class TicTacToe(object):
    def __init__(self, grid_size):
        self.board = self.make_board(grid_size)

    def __str__(self):
        # for row in self.board:
        #     print(str(row) + '\n')
        print(self.board)

    def make_board(self, grid_size):
        board = []
        for x in range(grid_size):
            board.append(["O"] * grid_size)
        return board


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("x")
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()
