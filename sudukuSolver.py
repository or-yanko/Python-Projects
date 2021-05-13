###press space to solve the soduku
###press f to fill the suduku with my numbers
###press c to clear the suduku
###press b to remove the red numbers
###press with the mouse on point and enter the numbers, if its stack it means your input is wrong
import pygame
import time

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

def copyB1ToB2(b1, b2):
    for i in range(0, 9):
        for j in range(0, 9):
            b2[i][j] = b1[i][j]

def drawError(screen, width, hight):
    pygame.font.init()
    myfont = pygame.font.SysFont('didot.ttc', 200)
    name = myfont.render("can't being solved!", True, GREEN)
    screen.blit(name, (width/2 - 280, hight/2 - 130))

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

def draw1(bo, orig, screen):
    pygame.font.init()
    myfont = pygame.font.SysFont('didot.ttc', 40)

    #draw btns
    ix = 15
    iy = 0
    text = myfont.render("Solve", True, BLACK)
    screen.blit(text, (630 + ix+45 , 50 + iy))

    text = myfont.render("Fill", True, BLACK)
    screen.blit(text, (630 + ix+50, 190 + iy))

    text = myfont.render("Clear All", True, BLACK)
    screen.blit(text, (630 + ix+5, 330 + iy))

    text = myfont.render("Clear Red", True, BLACK)
    screen.blit(text, (630 + ix, 470 + iy))

    #draw game
    myfont = pygame.font.SysFont('didot.ttc', 100)

    pygame.draw.line(screen, BLACK, [640, 630], [0, 630], 8)
    pygame.draw.line(screen, BLACK, [630, 640], [630, 0], 8)

    for i in range(9):
        for j in range(9):
            # draw lines
            if i % 3 == 0:
                pygame.draw.line(screen, BLACK, [i * 70, 0], [i * 70, 630], 8)
                pygame.draw.line(screen, BLACK, [0, i * 70], [630, i * 70], 8)
            else:
                pygame.draw.line(screen, BLACK, [i * 70, 0], [i * 70, 630], 4)
                pygame.draw.line(screen, BLACK, [0, i * 70], [630, i * 70], 4)

            #draw numbers
            kx = 17
            ky = 5
            if bo[j][i] != 0:
                text = myfont.render(str(bo[j][i]), True, RED)
                screen.blit(text, (kx + i * 70, ky + j * 70))

            if orig[j][i] != 0:
                text = myfont.render(str(orig[j][i]), True, BLACK)
                screen.blit(text, (kx + i * 70, ky + j * 70))

def main():
    # boards
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    original = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    # constants
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 634

    # init screen
    pygame.init()
    size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Suduku")

    clickX = 0
    clickY = 0

    screen.fill(WHITE)  # fill in white
    pygame.display.flip()

    finish = False
    flag = False

    while not finish:
        screen.fill(WHITE)  # fill in white (default)
        for event in pygame.event.get():
            # if quit
            if event.type == pygame.QUIT:
                finish = True
            #if mouse was clicked
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left click
                    x, y = pygame.mouse.get_pos()
                    if 0 < x and x < 630 and 0 < x and x < 630:
                        clickX, clickY = x, y
                        clickX = clickX // 70
                        clickY = clickY // 70
                    elif y > 50 and y < 150:#solve
                        try:
                            if solve(board) == false:
                                drawError(screen, WINDOW_WIDTH, WINDOW_HEIGHT)
                                flag = True

                        except:
                            pass
                    elif y > 190 and y < 290:#fill
                        board = [
                            [7, 8, 0, 4, 0, 0, 1, 2, 0],
                            [6, 0, 0, 0, 7, 5, 0, 0, 9],
                            [0, 0, 0, 6, 0, 1, 0, 7, 8],
                            [0, 0, 7, 0, 4, 0, 2, 6, 0],
                            [0, 0, 1, 0, 5, 0, 9, 3, 0],
                            [9, 0, 4, 0, 6, 0, 0, 0, 5],
                            [0, 7, 0, 3, 0, 0, 0, 1, 2],
                            [1, 2, 0, 0, 0, 7, 4, 0, 0],
                            [0, 4, 9, 2, 0, 6, 0, 0, 7]
                        ]
                        original = [
                            [7, 8, 0, 4, 0, 0, 1, 2, 0],
                            [6, 0, 0, 0, 7, 5, 0, 0, 9],
                            [0, 0, 0, 6, 0, 1, 0, 7, 8],
                            [0, 0, 7, 0, 4, 0, 2, 6, 0],
                            [0, 0, 1, 0, 5, 0, 9, 3, 0],
                            [9, 0, 4, 0, 6, 0, 0, 0, 5],
                            [0, 7, 0, 3, 0, 0, 0, 1, 2],
                            [1, 2, 0, 0, 0, 7, 4, 0, 0],
                            [0, 4, 9, 2, 0, 6, 0, 0, 7]
                        ]
                    elif y > 330 and y < 430:#clear all
                        board = [
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0]
                        ]
                        original = [
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0]
                        ]
                    elif y > 470 and y < 570:#clear red
                        copyB1ToB2(original, board)
            #if button is click
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:#clear red
                    copyB1ToB2(original, board)
                elif event.key == pygame.K_f:#fill
                    board = [
                        [7, 8, 0, 4, 0, 0, 1, 2, 0],
                        [6, 0, 0, 0, 7, 5, 0, 0, 9],
                        [0, 0, 0, 6, 0, 1, 0, 7, 8],
                        [0, 0, 7, 0, 4, 0, 2, 6, 0],
                        [0, 0, 1, 0, 5, 0, 9, 3, 0],
                        [9, 0, 4, 0, 6, 0, 0, 0, 5],
                        [0, 7, 0, 3, 0, 0, 0, 1, 2],
                        [1, 2, 0, 0, 0, 7, 4, 0, 0],
                        [0, 4, 9, 2, 0, 6, 0, 0, 7]
                    ]
                    original = [
                        [7, 8, 0, 4, 0, 0, 1, 2, 0],
                        [6, 0, 0, 0, 7, 5, 0, 0, 9],
                        [0, 0, 0, 6, 0, 1, 0, 7, 8],
                        [0, 0, 7, 0, 4, 0, 2, 6, 0],
                        [0, 0, 1, 0, 5, 0, 9, 3, 0],
                        [9, 0, 4, 0, 6, 0, 0, 0, 5],
                        [0, 7, 0, 3, 0, 0, 0, 1, 2],
                        [1, 2, 0, 0, 0, 7, 4, 0, 0],
                        [0, 4, 9, 2, 0, 6, 0, 0, 7]
                    ]
                elif event.key == pygame.K_c:#clear
                    board = [
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0]
                    ]
                    original = [
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0]
                    ]
                elif event.key == pygame.K_SPACE:#solve
                    try:
                        if solve(board) == false:
                            drawError(screen, WINDOW_WIDTH, WINDOW_HEIGHT)
                            flag = True
                    except:
                        pass
                elif event.key == pygame.K_1:#if 1 clicked
                    board[clickY][clickX] = 1
                    original[clickY][clickX] = 1
                elif event.key == pygame.K_2:#if 2 clicked
                    board[clickY][clickX] = 2
                    original[clickY][clickX] = 2
                elif event.key == pygame.K_3:#if 3 clicked
                    board[clickY][clickX] = 3
                    original[clickY][clickX] = 3
                elif event.key == pygame.K_4:#if 4 clicked
                    board[clickY][clickX] = 4
                    original[clickY][clickX] = 4
                elif event.key == pygame.K_5:#if 5 clicked
                    board[clickY][clickX] = 5
                    original[clickY][clickX] = 5
                elif event.key == pygame.K_6:#if 6 clicked
                    board[clickY][clickX] = 6
                    original[clickY][clickX] = 6
                elif event.key == pygame.K_7:#if 7 clicked
                    board[clickY][clickX] = 7
                    original[clickY][clickX] = 7
                elif event.key == pygame.K_8:#if 8 clicked
                    board[clickY][clickX] = 8
                    original[clickY][clickX] = 8
                elif event.key == pygame.K_9:#if 9 clicked
                    board[clickY][clickX] = 9
                    original[clickY][clickX] = 9
                elif event.key == pygame.K_0:#if 0 clicked
                    board[clickY][clickX] = 0
                    original[clickY][clickX] = 0



        draw1(board, original, screen)
        pygame.display.flip()
        if flag == True:
            time.sleep(2)
            flag = False

    pygame.quit()
    quit()

main()
