import pygame
from all.constants import *
from all.game import *
from minimax.algorithm2 import minimax,getcount

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
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        
        if game.turn == BLACK:
            value, new_board = minimax(game.get_board(),2, BLACK, game,-10000,10000)
            game.ai_move(new_board)
            getcount()

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    pygame.quit()
main()