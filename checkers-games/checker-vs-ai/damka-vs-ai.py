import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('DAMKA')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    isSeeThinking = False
    d = 3
    choice = input('Whould you like to see the ai thinking? y/n\n').lower()
    if choice == 'y':
        isSeeThinking ==True
    elif choice != 'n':
        print('\''+choice+'\' is invalid input. we chose not to simulate the ai')
    
    try:
        d = int(input('Enter the minimax depth 2(easyest) - 5(hardest)\n'))
        if 1>d or d>6:
            print('\''+d+'\' is invalid input. we chose make depth 3')
            d = 3
    except:
        print( 'we chose make depth 3')


    while run:
        clock.tick(FPS)
        
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), d, WHITE, game, isSeeThinking)
            game.ai_move(new_board)

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
