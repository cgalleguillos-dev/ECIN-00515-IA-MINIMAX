from actions.constants import SYMBOL_EMPTY
from actions.validations import *
from actions.utilities import translate


class Node:        
    def __init__(self, board, symbol: bytes = SYMBOL_EMPTY, positions: tuple = (0,0)) -> None:
        self.board = board
        if not symbol == SYMBOL_EMPTY:
            validate_symbol(symbol)
            self.insert_symbol(symbol, positions)

    def insert_symbol(self, symbol: bytes, positions: tuple) -> bool:
        validate_positions(positions)
        if self.get_symbol(positions) == SYMBOL_EMPTY:
            self.board[positions[0], positions[1]] = symbol
            return True
        return False
        
    def no_more_movements(self):
        return not SYMBOL_EMPTY in self.board

    def show_board(self):
        for r in self.board:
            print('| ', end='')
            for c in r:
                print(f'{translate(c)} ', end='')
            print('|')
        print()

    def is_empty(self):
        not_o = False if 0 in self.board.find(b'o') else True
        not_x = False if 0 in self.board.find(b'x') else True
        return not_o and not_x
    
    def evaluate_winning_symbol(self, key: bytes) -> bool:
        winner_evaluation = winner_conditions()
        for ev in winner_evaluation:
            if ev(key, self):
                return True
        return False
    
    def get_symbol(self, positions: tuple):
        return self.board[positions[0]][positions[1]]