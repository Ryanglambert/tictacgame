class TicTacToe(object):
    def __init__(self, grid_size, starting_player):
        self.grid_size = grid_size
        self.board = self.make_board(grid_size)
        self.last_moving_player = starting_player

    def make_board(self, grid_size):
        board = []
        for x in range(grid_size):
            board.append([" "] * grid_size)
        return board

    def update_board(self, location, x_o):
        x, y = location
        self.board[x][y] = x_o
        winner = self.check_winner()
        if winner:
            print('winner is: {}'.format(winner))

    def check_winner(self):
        "This method was written by Niso... not Ryan :-D"
        for i in range(3):
            if self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2] and self.board[i][0] != ' ':
                    return self.board[i][0]

        for j in range(3):
            if self.board[0][j] == self.board[1][j] and self.board[1][j] == self.board[2][j] and self.board[j][0] != ' ':
                    return self.board[0][j]

        # check for diags
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
               return self.board[0][0]

        # check for diags
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[2][0] != ' ':
               return self.board[0][2]
        return False
        

    def valid_move(self, loc):
        col, row = loc
        if col > self.grid_size or row > self.grid_size:
            print("You can't do that! Try again!")
        # should print to user when location is used
        pass

