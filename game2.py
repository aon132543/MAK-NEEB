import pygame
from constants import *
from board import *
from c1 import *
import traceback
    
class Game2:
    def __init__(self, win):
        self._init()
        self.win = win

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}
        self.net = Network()

    def reset(self):
        self._init()

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def winner(self):
        return self.board.winner()

    def select(self, row, col):

        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        return False

    def _move(self, row, col):
        print("WELCOME TO _MOVE")
        traceback.print_stack()
        piece = self.board.get_piece(row, col)

        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.send_data(self.selected.row, self.selected.col, row, col)
            self.board.move(self.selected, row, col)
            self.board._rule(row, col)
            # self.change_turn()
            # self.valid_moves = {}
            self.turn_now()
            print("TURN:" + str(self.turn))
        else:
            return False
        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE,(col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 25)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = BLACK
        else:
            self.turn = RED

    def send_data(self, piece_rol, piece_col, row, col):
        data = str(self.net.id) + ":" + "move" + ":" + str(piece_rol) + "," + str(piece_col) + "," + str(row) + "," + str(col)
        reply = self.net.send(data)
        return reply

    def sendrequest(self):
        data = str(self.net.id) + ":" + "request"
        reply = self.net.send(data)
        return reply

    def getrequest(self):
        data = str(self.net.id) + ":" + "get"
        reply = self.net.send(data)
        # print("GET : ",reply)
        return reply

    def turn_now(self):
        self.valid_moves = {}
        print("เข้า")
        data = str(self.net.id) + ":" + "turnnow"
        reply = self.net.send(data)
        if reply == "0":
            self.turn = RED
        else:
            self.turn = BLACK

    def change_turn_totext(self):
        if self.turn == RED:
            return '0'
        else:
            return '1'

    def clear_server(self):
        data = str(self.net.id) + ":" + "clear"
        reply = self.net.send(data)

    def get_id_now(self):
        data = str(self.net.id) + ":" + "getid"
        reply = self.net.send(data)
        return reply

    def MoveServer(self):
        data = str(self.net.id) + ":" + "move"
        reply = self.net.send(data)
        return reply