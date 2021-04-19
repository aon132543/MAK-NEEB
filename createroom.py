import pygame
import os
from pygame.locals import *
from constants import *
from game2 import *
from c2 import*

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
idclient = Network()

# Main Menu
def main_menu():
    menu = True
    selected = "start"
    bg = pygame.image.load("bgmuti.jpg").convert()
    count = 0
    
    
    while menu:
        data = str(idclient.id) + ":"+"len"
        reply = idclient.send(data)
        title = text_format("waiting for players", font, 20, white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # Main Menu UI
        screen.blit(bg, [0, 0])

        if (count % 50 == 0):
            time = text_format("..", font, 70, white)
        if (count % 100 == 0):
            time = text_format(".", font, 70, white)
        if (count % 150 == 0):
            time = text_format("...", font, 70, white)
            
        if int(reply) == 1:
            import mutimain

        # Main Menu Text
        screen.blit(title, (390, 140))
        screen.blit(time, (450, 250))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("MAK NEEB")
        count += 1


# Initialize the Game
main_menu()
pygame.quit()
quit()
