from turtle import color
import pygame
import os

from regex import D

# colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# pics
YELLOW_DISC_IMG = pygame.image.load(os.path.join("pics", "yellow_disc.png"))
RED_DISC_IMG = pygame.image.load(os.path.join("pics", "red_disc.png"))
BOARD_IMG = pygame.image.load(os.path.join("pics", "board.png"))
RED_DISC_IMG = pygame.transform.scale(RED_DISC_IMG, (65, 65))
YELLOW_DISC_IMG = pygame.transform.scale(YELLOW_DISC_IMG, (65, 65))


class circule():
    def __init__(self, x=0, y=0, color='w') -> None:
        self.x, self.y = x, y
        self.color = color

    def draw(self, screen):
        if self.color == 'y':
            screen.blit(YELLOW_DISC_IMG, (self.x, self.y))
        elif self.color == 'r':
            screen.blit(RED_DISC_IMG, (self.x, self.y))


board = []
for a in range(0, 7):
    l = []
    for b in range(0, 6):
        l.append(circule(25+a*87, 125+87*b))
    board.append(l)
# constants
WINDOW_WIDTH = 638
WINDOW_HEIGHT = 638


def draw(screen):
    pygame.font.init()
    # draw some things...
    screen.blit(BOARD_IMG, (0, 100))
    for a in board:
        for b in a:
            b.draw(screen)


# init screen
pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("connect 4")
screen.fill(WHITE)  # fill in white
pygame.display.flip()
finish = False

while not finish:
    screen.fill(WHITE)  # fill in white (default)
    for event in pygame.event.get():
        # if quit
        if event.type == pygame.QUIT:
            finish = True
        # if mouse was clicked
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # left click
                x, y = pygame.mouse.get_pos()
                print(x, y)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                print('d clicked')
    draw(screen)
    pygame.display.flip()

pygame.quit()
quit()
