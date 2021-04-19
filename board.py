import pygame
from constants import *
from piece import *

class Board:
    def __init__(self):
        self.board = []
        self.create_board()
        self.red_left = 5
        self.black_left = 5

    def draw_squares(self, win):
        win.fill(CL1)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, CL2, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row < 1:
                    self.board[row].append(Piece(row, col, BLACK))
                elif row > ROWS-2:
                    self.board[row].append(Piece(row, col, RED))
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

    def get_piece(self, row, col):
        return self.board[row][col]

    def get_valid_moves(self, piece):
        moves = {}
        row = piece.row
        col = piece.col
        forward = +piece.col
        side = +piece.row
        if piece.color == RED:
            moves.update(self._traverse_1(row-1,-1,-1,piece.color,forward))
            moves.update(self._traverse_1(row+1,ROWS,1,piece.color,forward))
            moves.update(self._traverse_2(col+1,COLS,1,piece.color,side))
            moves.update(self._traverse_2(col-1,-1,-1,piece.color,side))
        if piece.color == BLACK:
            moves.update(self._traverse_1(row+1,ROWS,1,piece.color,forward))
            moves.update(self._traverse_1(row-1,-1,-1,piece.color,forward))
            moves.update(self._traverse_2(col+1,COLS,1,piece.color,side))
            moves.update(self._traverse_2(col-1,-1,-1,piece.color,side))
        return moves

    def _traverse_1(self, start, stop, step, color, forward):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if forward >= ROWS:
                break
            current = self.board[r][forward]
            if current == 0:
                moves[(r,forward)] = last
            elif current.color == color:
                return moves
            else:
                return moves
        return moves

    def _traverse_2(self, start, stop, step, color, side):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if side >= COLS:
                break
            current = self.board[side][r]
            if current == 0:
                moves[(side,r)] = last
            elif current.color == color:
                return moves
            else:
                return moves
        return moves

    def winner(self):
        if self.black_left <= 0:
            return 'The winner is RED'
        elif self.red_left <= 0:
            return 'The winner is BLACK'
        return None

    def _rule(self, row, col):
        if (self.board[0][col] != 0 and self.board[1][col] != 0 and self.board[2][col] != 0 and self.board[3][col] != 0 and self.board[4][col] != 0):
            if (self.board[0][col].color == self.board[3][col].color and self.board[1][col].color !=self.board[3][col].color and self.board[2][col].color != self.board[3][col].color and self.board[4][col].color != self.board[3][col].color):
                self.board[1][col] = 0
                self.board[2][col] = 0
                self.board[4][col] = 0
                if self.board[row][col].color == RED:
                    self.black_left -= 3
                else:
                    self.red_left -= 3
            if (self.board[0][col].color != self.board[1][col].color and self.board[2][col].color !=self.board[1][col].color and self.board[3][col].color != self.board[1][col].color and self.board[4][col].color == self.board[1][col].color):
                self.board[0][col] = 0
                self.board[2][col] = 0
                self.board[3][col] = 0
                if self.board[row][col].color == RED:
                    self.black_left -= 3
                else:
                    self.red_left -= 3

        if (self.board[row][0] != 0 and self.board[row][1] != 0 and self.board[row][2] != 0 and self.board[row][3] != 0 and self.board[row][4] != 0):
            if (self.board[row][0].color == self.board[row][3].color and self.board[row][1].color !=self.board[row][3].color and self.board[row][2].color != self.board[row][3].color and self.board[row][4].color != self.board[row][3].color):
                self.board[row][1] = 0
                self.board[row][2] = 0
                self.board[row][4] = 0
                if self.board[row][col].color == RED:
                    self.black_left -= 3
                else:
                    self.red_left -= 3
            if (self.board[row][0].color != self.board[row][1].color and self.board[row][2].color !=self.board[row][1].color and self.board[row][3].color != self.board[row][1].color and self.board[row][4].color == self.board[row][1].color):
                self.board[row][0] = 0
                self.board[row][2] = 0
                self.board[row][3] = 0
                if self.board[row][col].color == RED:
                    self.black_left -= 3
                else:
                    self.red_left -= 3

        if(col-1 >= 0 and col+1 < COLS):
            if(self.board[row][col+1] != 0 and self.board[row][col-1] != 0):
                if(self.board[row][col+1].color != self.board[row][col].color  and self.board[row][col-1].color  != self.board[row][col].color):
                    self.board[row][col+1] = 0
                    self.board[row][col-1] = 0
                    if self.board[row][col].color == RED:
                        self.black_left -= 2
                    else:
                        self.red_left -= 2

        if (col+1 >= 0 and col+2 < COLS):
            if (self.board[row][col+1] != 0 and self.board[row][col+2] != 0):
                if (self.board[row][col+1].color != self.board[row][col].color and self.board[row][col+2].color == self.board[row][col].color):
                    self.board[row][col+1] = 0
                    if self.board[row][col].color == RED:
                        self.black_left -= 1
                    else:
                        self.red_left -= 1

        if (col-2 >= 0 and col-1 < COLS):
            if (self.board[row][col-1] != 0 and self.board[row][col-2] != 0):
                if (self.board[row][col-1].color != self.board[row][col].color and self.board[row][col-2].color == self.board[row][col].color):
                    self.board[row][col-1] = 0
                    if self.board[row][col].color == RED:
                        self.black_left -= 1
                    else:
                        self.red_left -= 1

        if (row-1 >= 0 and row+1 < ROWS):
            if (self.board[row+1][col] != 0 and self.board[row-1][col] != 0):
                if (self.board[row+1][col].color != self.board[row][col].color and self.board[row-1][col].color !=self.board[row][col].color):
                    self.board[row+1][col] = 0
                    self.board[row-1][col] = 0
                    if self.board[row][col].color == RED:
                        self.black_left -= 2
                    else:
                        self.red_left -= 2

        if (row+1 >= 0 and row+2 < ROWS):
            if (self.board[row+1][col] != 0 and self.board[row+2][col] != 0):
                if (self.board[row+1][col].color != self.board[row][col].color and self.board[row+2][col].color == self.board[row][col].color):
                    self.board[row+1][col] = 0
                    if self.board[row][col].color == RED:
                        self.black_left -= 1
                    else:
                        self.red_left -= 1

        if (row-2 >= 0 and row-1 < ROWS):
            if (self.board[row-1][col] != 0 and self.board[row-2][col] != 0):
                if (self.board[row-1][col].color != self.board[row][col].color and self.board[row-2][col].color == self.board[row][col].color):
                    self.board[row-1][col] = 0
                    if self.board[row][col].color == RED:
                        self.black_left -= 1
                    else:
                        self.red_left -= 1

        if (col+1 >= 0 and col+4 < COLS):
            if (self.board[row][col+1] != 0 and self.board[row][col+2] != 0 and self.board[row][col+3] != 0 and self.board[row][col+4] != 0):
                if (self.board[row][col+1].color != self.board[row][col].color and self.board[row][col+2].color !=self.board[row][col].color and self.board[row][col+3].color !=self.board[row][col].color and self.board[row][col+4].color ==self.board[row][col].color):
                    self.board[row][col+1] = 0
                    self.board[row][col+2] = 0
                    self.board[row][col+3] = 0
                    if self.board[row][col].color == RED:
                        self.black_left -= 3
                    else:
                        self.red_left -= 3

        if (col-1 >= 0 and col-4 < COLS):
            if (self.board[row][col-1] != 0 and self.board[row][col-2] != 0 and self.board[row][col-3] != 0 and self.board[row][col-4] != 0):
                if (self.board[row][col-1].color != self.board[row][col].color and self.board[row][col-2].color !=self.board[row][col].color and self.board[row][col-3].color !=self.board[row][col].color and self.board[row][col-4].color ==self.board[row][col].color):
                    self.board[row][col-1] = 0
                    self.board[row][col-2] = 0
                    self.board[row][col-3] = 0
                    if self.board[row][col].color == RED:
                        self.black_left -= 3
                    else:
                        self.red_left -= 3

        if (col+1 >= 0 and col+3 < COLS):
            if (self.board[row][col+1] != 0 and self.board[row][col+2] != 0 and self.board[row][col+3] != 0):
                if (self.board[row][col+1].color != self.board[row][col].color and self.board[row][col+2].color !=self.board[row][col].color and self.board[row][col+3].color ==self.board[row][col].color):
                    self.board[row][col+1] = 0
                    self.board[row][col+2] = 0
                    if self.board[row][col].color == RED:
                        self.black_left -= 2
                    else:
                        self.red_left -= 2

        if (col-1 >= 0 and col-3 < COLS):
            if (self.board[row][col-1] != 0 and self.board[row][col-2] != 0 and self.board[row][col-3] != 0):
                if (self.board[row][col-1].color != self.board[row][col].color and self.board[row][col-2].color !=self.board[row][col].color and self.board[row][col-3].color ==self.board[row][col].color):
                    self.board[row][col-1] = 0
                    self.board[row][col-2] = 0
                    if self.board[row][col].color == RED:
                        self.black_left -= 2
                    else:
                        self.red_left -= 2

        if (row+1 >= 0 and row+4 < COLS):
            if (self.board[row+1][col] != 0 and self.board[row+2][col] != 0 and self.board[row+3][col] != 0 and self.board[row+4][col] != 0):
                if (self.board[row+1][col].color != self.board[row][col].color and self.board[row+2][col].color != self.board[row][col].color and self.board[row+3][col].color != self.board[row][col].color and self.board[row+4][col].color == self.board[row][col].color):
                    self.board[row+1][col] = 0
                    self.board[row+2][col] = 0
                    self.board[row+3][col] = 0
                    if self.board[row][col].color == RED:
                        self.black_left -= 3
                    else:
                        self.red_left -= 3

        if (row-1 >= 0 and row-4 < COLS):
            if (self.board[row-1][col] != 0 and self.board[row-2][col] != 0 and self.board[row-3][col] != 0 and self.board[row-4][col] != 0):
                if (self.board[row-1][col].color != self.board[row][col].color and self.board[row-2][col].color !=self.board[row][col].color and self.board[row-3][col].color != self.board[row][col].color and self.board[row-4][col].color == self.board[row][col].color):
                    self.board[row-1][col] = 0
                    self.board[row-2][col] = 0
                    self.board[row-3][col] = 0
                    if self.board[row][col].color == RED:
                        self.black_left -= 3
                    else:
                        self.red_left -= 3

        if (row+1 >= 0 and row+4 < COLS):
            if (self.board[row+1][col] != 0 and self.board[row+2][col] != 0 and self.board[row+3][col] != 0):
                if (self.board[row+1][col].color != self.board[row][col].color and self.board[row+2][col].color != self.board[row][col].color and self.board[row+3][col].color == self.board[row][col].color):
                    self.board[row+1][col] = 0
                    self.board[row+2][col] = 0
                    if self.board[row][col].color == RED:
                        self.black_left -= 2
                    else:
                        self.red_left -= 2

        if (row-1 >= 0 and row-3 < COLS):
            if (self.board[row-1][col] != 0 and self.board[row-2][col] != 0 and self.board[row-3][col] != 0):
                if (self.board[row-1][col].color != self.board[row][col].color and self.board[row-2][col].color !=self.board[row][col].color and self.board[row-3][col].color == self.board[row][col].color ):
                    self.board[row-1][col] = 0
                    self.board[row-2][col] = 0
                    if self.board[row][col].color == RED:
                        self.black_left -= 2
                    else:
                        self.red_left -= 2

        if (self.board[4][0] != 0 and self.board[4][1] != 0 and self.board[4][2] != 0 and self.board[4][3] != 0 and self.board[4][4] != 0):
            if (self.board[3][0] != 0 and self.board[3][1] != 0 and self.board[3][2] != 0 and self.board[3][3] != 0 and self.board[4][4] != 0):
                for i in range(5):
                    if self.board[4][i].color == RED:
                        self.red_left -= 5
                    else:
                        self.black_left -= 5

        if (self.board[0][0] != 0 and self.board[0][1] != 0 and self.board[0][2] != 0 and self.board[0][3] != 0 and self.board[0][4] != 0):
            if (self.board[1][0] != 0 and self.board[1][1] != 0 and self.board[1][2] != 0 and self.board[1][3] != 0 and self.board[1][4] != 0):
                for i in range(5):
                    if self.board[1][i].color == RED:
                        self.black_left -= 5
                    else:
                        self.red_left -= 5

        if (row-1 >= 0 and row+2 < COLS):
            if (self.board[row-1][col] != 0 and self.board[row+1][col] != 0 and self.board[row+2][col] != 0):
                if (self.board[row-1][col].color != self.board[row][col].color and self.board[row+1][col].color ==self.board[row][col].color and self.board[row+2][col].color != self.board[row][col].color ):
                    self.board[row-1][col] = 0
                    self.board[row+2][col] = 0
                    if self.board[row][col].color == RED:
                        self.black_left -= 2
                    else:
                        self.red_left -= 2

        if (row-2 >= 0 and row+1 < COLS):
            if (self.board[row-2][col] != 0 and self.board[row-1][col] != 0 and self.board[row+1][col] != 0):
                if (self.board[row-2][col].color != self.board[row][col].color and self.board[row-1][col].color ==self.board[row][col].color and self.board[row+1][col].color != self.board[row][col].color ):
                    self.board[row+1][col] = 0
                    self.board[row-2][col] = 0
                    if self.board[row][col].color == RED:
                        self.black_left -= 2
                    else:
                        self.red_left -= 2

        if (col-2 >= 0 and col+1 < COLS):
            if (self.board[row][col-2] != 0 and self.board[row][col-1] != 0 and self.board[row][col+1] != 0):
                if (self.board[row][col-2].color != self.board[row][col].color and self.board[row][col-1].color ==self.board[row][col].color and self.board[row][col+1].color != self.board[row][col].color):
                    self.board[row][col+1] = 0
                    self.board[row][col-2] = 0
                    if self.board[row][col].color == RED:
                        self.black_left -= 2
                    else:
                        self.red_left -= 2

        if (col-1 >= 0 and col+2 < COLS):
            if (self.board[row][col-1] != 0 and self.board[row][col+1] != 0 and self.board[row][col+2] != 0):
                if (self.board[row][col-1].color != self.board[row][col].color and self.board[row][col+1].color ==self.board[row][col].color and self.board[row][col+2].color != self.board[row][col].color):
                    self.board[row][col-1] = 0
                    self.board[row][col+2] = 0
                    if self.board[row][col].color == RED:
                        self.black_left -= 2
                    else:
                        self.red_left -= 2

        if (col-2 >= 0 and col+2 < COLS):
            if (self.board[row][col-2] != 0 and self.board[row][col-1] != 0 and self.board[row][col+1] != 0 and self.board[row][col+2] != 0):
                if (self.board[row][col-2].color != self.board[row][col].color and self.board[row][col-1].color ==self.board[row][col].color and self.board[row][col+1].color == self.board[row][col].color and self.board[row][col+2].color != self.board[row][col].color):
                    self.board[row][col-2] = 0
                    self.board[row][col+2] = 0
                    if self.board[row][col].color == RED:
                        self.black_left -= 2
                    else:
                        self.red_left -= 2

        if (row-2 >= 0 and row+2 < COLS):
            if (self.board[row+1][col] != 0 and self.board[row-1][col] != 0 and self.board[row+1][col] != 0 and self.board[row+2][col] != 0):
                if (self.board[row-2][col].color != self.board[row][col].color and self.board[row-1][col].color ==self.board[row][col].color and self.board[row+1][col].color == self.board[row][col].color and self.board[row+2][col].color != self.board[row][col].color):
                    self.board[row-2][col] = 0
                    self.board[row+2][col] = 0
                    if self.board[row][col].color == RED:
                        self.black_left -= 2
                    else:
                        self.red_left -= 2