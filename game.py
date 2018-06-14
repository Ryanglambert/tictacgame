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

    def check_winner(self):
        pass

    def valid_move(self, loc):
        # should print to user when location is used
        pass

