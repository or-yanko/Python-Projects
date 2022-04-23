from copy import deepcopy
import pygame
from sympy import evaluate

RED = (255, 0, 0)
WHITE = (255, 255, 255)


def minimax(position,depth,max_player,game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    if max_player:
        max_eval = float ('-inf')
        best_move = None
        for move in get_all_moves(position,WHITE,game):
            evaluate = minimax(move,depth-1,False,game)[0]
            max_eval = max(evaluate,max_eval)
            if max_eval == evaluate:
                best_move = move
        return max_eval, best_move
    else:
        min_eval = float ('inf')
        best_move = None
        for move in get_all_moves(position,RED,game):
            evaluate = minimax(move,depth-1,True,game)[0]
            min_eval = min(evaluate,min_eval)
            if min_eval == evaluate:
                best_move = move
        return min_eval, best_move



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
            temp_piece = temp_board.get_piece(piece.row,piece.col)
            new_board = simulate_move(temp_piece,move,temp_board,game,skip )
            moves.append(new_board)
    return moves