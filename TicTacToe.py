__author__ = 'Yijun Lou'
__copyright__ = "Copyright 2018, The Group Project of IE598"
__credits__ = ["Yijun Lou"]
__license__ = "University of Illinois, Urbana Champaign"
__version__ = "1.0.0"
__maintainer__ = "Yijun Lou"
__email__ = "ylou4@illinois.edu"

class TicTacToe:

    def __init__(self, size, is_ai=False):
        self.rows, self.cols, self.diag, self.anti_diag, self.size = [0] * size, [0] * size, 0, 0, size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.player = 1
        self.piece_counter = 0
        self.is_ai = is_ai

    def reset(self):
        self.rows, self.cols, self.diag, self.anti_diag = [0] * self.size, [0] * self. size, 0, 0
        self.board = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        self.player = 1
        self.piece_counter = 0

    def display_board(self):
        for row in self.board:
            print('|'+'|'.join(row)+'|')

    def move(self, row, col):
        offset = self.player * 2 - 3
        piece = 'X' if offset == -1 else 'O'
        if self.board[row][col] != ' ':
            return -1
        self.board[row][col] = piece
        self.piece_counter += 1
        self.rows[row] += offset
        self.cols[col] += offset
        if row == col:
            self.diag += offset
        if row + col == self.size - 1:
            self.anti_diag += offset
        if self.size in [self.rows[row], self.cols[col], self.diag, self.anti_diag]:
            return 1
        if -self.size in [self.rows[row], self.cols[col], self.diag, self.anti_diag]:
            return 1
        if self.piece_counter == self.size * self.size:
            return 2
        return 0

    def get_ai_move(self):
        if self.diag - 1 == -self.size or self.diag + 1 == self.size:
            for i in range(self.size):
                if self.board[i][i] == " ":
                    return i, i
        if self.anti_diag - 1 == -self.size or self.anti_diag + 1 == self.size:
            for i in range(self.size):
                if self.board[i][self.size-i-1] == " ":
                    return i, self.size-i-1
        row_idx, col_idx = -1, -1
        for i, row in enumerate(self.rows):
            if row + 1 == -self.size:
                for j in range(self.size):
                    if self.board[i][j] == " ":
                        return i, j
            if row - 1 == self.size:
                for j in range(self.size):
                    if self.board[i][j] == " ":
                        row_idx, col_idx = i, j
        else:
            for i, col in enumerate(self.cols):
                if col + 1 == -self.size:
                    for j in range(self.size):
                        if self.board[j][i] == " ":
                            return i, j
                if col - 1 == self.size:
                    for j in range(self.size):
                        if self.board[j][i] == " ":
                            row_idx, col_idx = i, j
            if row_idx > -1:
                return row_idx, col_idx
            else:
                mid = [1,1]
                if self.board[mid[0]][mid[1]] == " ":
                    return mid[0], mid[1]
                corners = [[0,0], [2,2], [0,2], [2,0]]
                for corner in corners:
                    if self.board[corner[0]][corner[1]] == " ":
                        return corner[0], corner[1]
                others = [[0,1], [1,0], [2,1], [1,2]]
                for other in others:
                    if self.board[other[0]][other[1]] == " ":
                        return other[0], other[1]

    def is_game_activated(self, row, col):
        if row >= self.size or col >= self.size or row < 0 or col < 0:
            print("Out of bound")
            return True
        action = self.move(row, col)
        if action == -1:
            print("Invalid move for Player {}".format(self.player))
        else:
            print("Player {0} move to {1},{2}".format(self.player, row, col))
            self.display_board()
            if action == 1 :
                print("Player {0} WIN!\nThanks for playing.".format(self.player))
                return False
            elif action == 2:
                print("Duel game!")
                return False
            else:
                self.player = 2 if self.player == 1 else 1
        return True

    def run(self):
        is_activated = True
        print("Put row and column index please, integers split by space.")
        while is_activated:
            try:
                row, col = map(int, input().split())
                if row == -1 or col == -1:
                    print("Terminated!")
                    return 0
                is_activated = game.is_game_activated(row, col)
                if self.player == 2 and self.is_ai:
                    row_idx, col_idx = self.get_ai_move()
                    is_activated = game.is_game_activated(row_idx, col_idx)
            except:
                print("Invalid input!")
        return 0

if __name__ == "__main__":
    print("Input the board size!")
    size = 0
    while not size:
        try:
            size = int(input())
        except:
            print("The input should be an integer!")
    game = TicTacToe(size)
    game.run()