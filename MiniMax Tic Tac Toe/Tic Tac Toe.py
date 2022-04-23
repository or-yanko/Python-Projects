import random
import pygame
import time

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400
# init screen
pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}
player = 'O'
bot = 'X'
errorTxt = ""

xoringTxt = 23479
botwins = 0
playerwins = 0

try:
    txt = str(open("myfile.txt", "r+") .read())
    lst = txt.split(" ")
    botwins = int(lst[0]) ^ xoringTxt
    playerwins = int(lst[1]) ^ xoringTxt
except:
  pass



screen = pygame.display.set_mode(size)

def writeWinsToFilw():
    t = str(str(botwins^xoringTxt)+" "+str(playerwins^xoringTxt))
    open("myfile.txt", "w+").write(t)


def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False


def insertLetter(letter, position):
    global board
    global botwins
    global playerwins
    global errorTxt
    if spaceIsFree(position):
        errorTxt = ""
        board[position] = letter
        if (checkDraw()):
            errorTxt = "Draw..."
        if checkForWin():
            if letter == 'X':
                errorTxt = "Bot Wins ;-)"
                botwins += 1
            else:
                errorTxt = "Player Wins ;-)"
                playerwins += 1

    else:
        errorTxt = "invalid input !!!!!!"


def checkForWin():
    #check rows
    for i in range(1, 10, 3):
        if (board[i] == board[i+1] and board[i] == board[i+2] and board[i] != ' '):
            pygame.draw.line(screen, GREEN, [0, 50+((i-1) // 3 * 100)], [300, 50+(i // 3 * 100)], 8)
            return True
    #check cols
    for i in range(1, 3, 1):
        if (board[i] == board[i+3] and board[i] == board[i+6] and board[i] != ' '):
            pygame.draw.line(screen, GREEN, [50+((i-1) % 3 * 100), 0], [50+((i-1) % 3 * 100), 300], 8)

            return True
    #check alachsons
    if (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        pygame.draw.line(screen, GREEN, [0, 0], [300, 300], 8)
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        pygame.draw.line(screen, GREEN, [0, 300], [300, 0], 8)
        return True

    return False


def checkWhichMarkWon(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True

def compMove():
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    insertLetter(bot, bestMove)
    return


def minimax(board, depth, isMaximizing):
    if (checkWhichMarkWon(bot)):
        return 1
    elif (checkWhichMarkWon(player)):
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):
        bestScore = -800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


def clearBoard():
    global board
    board = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}

def isGameFinished(board):
    if errorTxt == "Draw..." or errorTxt == "Bot Wins ;-)" or errorTxt == "Player Wins ;-)":
        return True
    return False

def drawBoard(board, screen, errorMsg):
    pygame.font.init()
    myfont = pygame.font.SysFont('didot.ttc', 20)

    #draw btns
    ix = 15
    iy = 0
    text = myfont.render(errorMsg, True, RED)
    screen.blit(text, (300 + ix+45, 50 + iy))

    global botwins
    global playerwins
    text = myfont.render("Bot:" + str(botwins), True, BLACK)
    screen.blit(text, (300 + ix+45, 100 + iy))
    text = myfont.render("Player:" + str(playerwins), True, BLACK)
    screen.blit(text, (300 + ix+45, 150 + iy))


    myfont = pygame.font.SysFont('didot.ttc', 40)
    text = myfont.render("restart", True, BLACK)
    screen.blit(text, (300 + ix+50, 200 + iy))

    #draw game
    myfont = pygame.font.SysFont('didot.ttc', 100)


    for i in range(0, 4, 1):
        #draw lines
        pygame.draw.line(screen, BLACK, [i * 100, 0], [i * 100, 300], 8)
        pygame.draw.line(screen, BLACK, [0, i * 100], [300, i * 100], 8)


    # draw numbers
    color = RED
    xmrg = 20
    ymrg = 20
    for i in range(1, 10):
        if board[i] == "X":
            color = BLACK
        elif board[i] == "O":
            color = RED
        x = ((i-1) % 3) * 100 + xmrg
        y = ((i-1) // 3) * 100 + ymrg
        text = myfont.render(str(board[i]), True, color)
        screen.blit(text, (x, y))


def main():


    global screen
    pygame.display.set_caption("Tic Tac Toe MiniMax")

    clickX = 0
    clickY = 0
    screen.fill(WHITE)  # fill in white
    pygame.display.flip()

    finish = False
    turn = ""
    n = random.randrange(0, 100)
    if n % 2 == 0:
        turn = "X"
    else:
        turn = "O"

    while not finish:
        if isGameFinished(board) == True:
            time.sleep(3)
            global errorTxt
            errorTxt = ""
            clearBoard()
            writeWinsToFilw()

        screen.fill(WHITE)  # fill in white (default)
        if turn == "X":#comp
            compMove()
            turn = "O"

        elif turn == "O":#human
            for event in pygame.event.get():
                # if quit
                if event.type == pygame.QUIT:
                    finish = True
                #if mouse was clicked
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # left click
                        x, y = pygame.mouse.get_pos()
                        if (0 < x and x < 300 and 0 < x and x < 300):
                            i = ((x + 100) // 100) + ((y // 100) * 3)
                            insertLetter(player, i)
                            if errorTxt != "invalid input !!!!!!":
                                turn = "X"

                        else:
                            #btn
                            pass


        drawBoard(board, screen, errorTxt)
        pygame.display.flip()
    pygame.quit()
    quit()



main()