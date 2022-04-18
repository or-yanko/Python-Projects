# imports
import pygame


# colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


def draw(screen):
    pygame.font.init()
    # draw some things...
    pass


# constants
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 400

# init screen
pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("title")
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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                print('d clicked')
    draw(screen)
    pygame.display.flip()

pygame.quit()
quit()
