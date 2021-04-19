import pygame
import os
from pygame.locals import *
from constants import *
from game import *

# Game Initialization
pygame.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width = 640
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
    return newText

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Game Fonts
font = "Ratox-Regular.ttf"

# Game Framerate
clock = pygame.time.Clock()
FPS = 30

# Main Menu
def main_menu():
    menu = True
    selected = "start"
    bg = pygame.image.load("bg.jpg").convert()
    count = 0

    while menu:
        for event in pygame.event.get():

            text_start = text_format("START", font, 25, white)
            text_Muti = text_format("MUTI-PLAYER", font, 25, white)
            text_ai = text_format("PLAY-AI", font, 25, white)
            text_quit = text_format("QUIT", font, 25, white)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                if pos[0] in range(437, 536) and pos[1] in range(270, 300):
                    text_start = text_start = text_format("START", font, 25, black)
                if pos[0] in range(374, 611) and pos[1] in range(310, 380):
                    text_Muti = text_format("MUTI-PLAYER", font, 25, black)

                if pos[0] in range(374, 611) and pos[1] in range(390, 420):
                    text_ai = text_format("PLAY-AI", font, 25, black)

                if pos[0] in range(374, 611) and pos[1] in range(430, 500):
                    text_quit = text_format("QUIT", font, 25, black)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] in range(437, 536) and pos[1] in range(270, 300):
                    from main import main

                if pos[0] in range(374, 611) and pos[1] in range(310, 380):
                    from createroom import main_menu

                if pos[0] in range(374, 611) and pos[1] in range(390, 420):
                    text_ai = text_format("PLAY-AI", font, 25, black)
                    from aimenu import main

                if pos[0] in range(374, 611) and pos[1] in range(430, 500):
                    pygame.quit()
                    quit()

        # Main Menu UI
        screen.blit(bg, [0, 0])

        title = text_format("MENU", font, 45, white)

        # Main Menu Text
        screen.blit(title, (425, 140))
        screen.blit(text_start, (450, 270))
        screen.blit(text_Muti, (412, 330))
        screen.blit(text_ai, (442, 390))
        screen.blit(text_quit, (458, 450))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("MAK NEEB")

# Initialize the Game
main_menu()
pygame.quit()
quit()