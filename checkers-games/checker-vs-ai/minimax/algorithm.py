from copy import deepcopy
import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)


def minimax(position,depth,max_player,game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    if max_player:
        max_eval = float ('-inf')
        bestMove = None
        for move in get_all_moves(position,WHITE,game)


def simulate_move(piece,move, board,game,skip ):
    board.move(piece , move[0],move[1])
    if skip:
        board.remove(skip)
    return board


def get_all_moves(board,color,game):
    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_all_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            new_board = simulate_move(piece,move,temp_board,game,skip )
            moves.append(new_board)
    return moves