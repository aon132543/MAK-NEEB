import pygame
from constants import *
from game2 import *
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('MAK NEEB')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game2(WIN)
    if int(game.net.id) == 1:
        game.turn = BLACK

    while run:
        x = game.sendrequest()
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                if int(x) == 1:
                    game.select(row, col)
            else :  
                move = game.getrequest()
                if move != "None":
                    move = move.split(",")
                    piece = game.board.board[int(move[0])][int(move[1])]
                    if piece != 0 :
                        game.board.move(piece,int(move[2]),int(move[3]))
                        game.board._rule(int(move[2]),int(move[3]))
                        game.clear_server()
                        game.turn_now()
                    

        game.update()
    pygame.quit()
main()