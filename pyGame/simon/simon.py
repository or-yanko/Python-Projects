import pygame
import time
from random import randint
from playsound import playsound


# colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

tic = time.perf_counter()  # Start Time

global is_comp_turn
sequence = []
clicking_list = []
global colors_of_sqr
global top_text
sleep_time = 0.2


def draw(screen):
    global top_text
    global colors_of_sqr
    pygame.font.init()
    myfont = pygame.font.SysFont('didot.ttc', 40)
    i = -5
    screen.blit(pygame.font.SysFont('didot.ttc', 30).render(
        top_text, True, BLACK), (10, 10))
    # draw btn1
    pygame.draw.rect(screen, colors_of_sqr[0], pygame.Rect(50, 150, 100, 100))
    screen.blit(myfont.render("d", True, BLACK), (100 + i, 200 + i))
    # draw btn2
    pygame.draw.rect(screen, colors_of_sqr[1], pygame.Rect(150, 150, 100, 100))
    screen.blit(myfont.render("f", True, BLACK), (200 + i, 200 + i))
    # draw btn3
    pygame.draw.rect(screen, colors_of_sqr[2], pygame.Rect(50, 250, 100, 100))
    screen.blit(myfont.render("c", True, BLACK), (100 + i, 300 + i))
    # draw btn4
    pygame.draw.rect(screen, colors_of_sqr[3], pygame.Rect(150, 250, 100, 100))
    screen.blit(myfont.render("v", True, BLACK), (200 + i, 300 + i))


def make_sound(s):
    if s == 1:
        playsound('./sounds/simonSound1.mp3')
    elif s == 2:
        playsound('./sounds/simonSound2.mp3')
    elif s == 3:
        playsound('./sounds/simonSound3.mp3')
    elif s == 0:
        playsound('./sounds/simonSound4.mp3')


def change_color(s, screen, tim=sleep_time):
    global colors_of_sqr
    past_color = colors_of_sqr[s]
    colors_of_sqr[s] = BLACK
    draw(screen)
    pygame.display.flip()
    time.sleep(tim)
    colors_of_sqr[s] = past_color
    draw(screen)
    pygame.display.flip()


def show_and_sound_sequence(screen):
    global is_comp_turn

    next = randint(0, 3)
    sequence.append(int(next))

    for s in sequence:
        change_color(s, screen)
        make_sound(s)
    is_comp_turn = False


def check_is_good_call(i, cl):
    return sequence[i] == cl[i]


def main():
    global colors_of_sqr
    global top_text

    colors_of_sqr = [RED, YELLOW, GREEN, BLUE]
    top_text = ''
    global is_comp_turn
    is_comp_turn = True

    # constants
    WINDOW_WIDTH = 300
    WINDOW_HEIGHT = 400

    # init screen
    pygame.init()
    size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("simon")

    clickX = 0
    clickY = 0

    screen.fill(WHITE)  # fill in white
    pygame.display.flip()
    finish = False
    flag = True
    i = 0
    clicking_list = []

    while not finish:
        screen.fill(WHITE)  # fill in white (default)

        toc = time.perf_counter()  # End Time
        if int(toc - tic) < 6:
            top_text = 'starting in :' + str(5 - int(toc - tic))
        else:
            # * title
            if is_comp_turn == True:
                top_text = 'listen and watch'
                show_and_sound_sequence(screen)
                i = 0
                clicking_list = []

            else:
                top_text = 'click or type'
                if i == len(sequence):
                    is_comp_turn = True

                else:
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
                                clicking_list.append(0)
                                change_color(0, screen, 0.05)
                                make_sound(0)
                                flag = check_is_good_call(i, clicking_list)
                                i += 1
                            if event.key == pygame.K_f:
                                change_color(1, screen, 0.05)
                                make_sound(1)
                                clicking_list.append(1)
                                flag = check_is_good_call(i, clicking_list)
                                i += 1
                            if event.key == pygame.K_c:
                                change_color(2, screen, 0.05)
                                make_sound(2)
                                clicking_list.append(2)
                                flag = check_is_good_call(i, clicking_list)
                                i += 1
                            if event.key == pygame.K_v:
                                change_color(3, screen, 0.05)
                                make_sound(3)
                                clicking_list.append(3)
                                flag = check_is_good_call(i, clicking_list)
                                i += 1

        draw(screen)
        pygame.display.flip()
        if flag == False:
            time.sleep(2)
            break

    pygame.quit()
    quit()


main()
