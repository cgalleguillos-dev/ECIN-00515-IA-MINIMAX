from ast import Try
import numpy as np
from actions.constants import INSTRUCTIONS, SYMBOL_EMPTY, SYMBOL_O, SYMBOL_X
from actions.utilities import translate
from actions.validations import validate_options, validate_symbol
from minimax.Minimax import Minimax
from node.Node import Node

class Game:
    def __init__(self) -> None:
        self.board = np.chararray([3, 3])
        self.board[:, :] = SYMBOL_EMPTY
        self.inital_node = Node(self.board)
        self.minimax = Minimax()
        self.run()
    
    def set_player_symbol(self, symbol: bytes, key: str) -> None:
        validate_symbol(symbol)
        if key == 'ia':
            self.minimax.ia_symbol = symbol
        elif key == 'pl':    
            self.minimax.player_symbol = symbol
    
    def choose_player_symbol(self) -> None:
        option = validate_options()
        if option == '1':
            self.set_player_symbol(SYMBOL_X, 'pl')
            self.set_player_symbol(SYMBOL_O, 'ia')
        else:
            self.set_player_symbol(SYMBOL_O, 'pl')
            self.set_player_symbol(SYMBOL_X, 'ia')

    def show_player_symbol(self):
        print(f'IA: {translate(self.minimax.ia_symbol)}')
        print(f'JUGADOR: {translate(self.minimax.player_symbol)}')

    def player_turn(self, current: Node):
        print('TURNO DEL JUGADOR')
        while True:
            try:
                positions1, positions2 = input(INSTRUCTIONS)
                if positions1 == '9'and  positions2 == '9':
                    return False
                positions1, positions2 = int(positions1), int(positions2)
                coord = (positions1, positions2)
                if current.insert_symbol(self.minimax.player_symbol,coord):
                    current.show_board()
                    return True
                print('La posicion ingresada ya fue elegida, intenta nuevamente\n')
            except ValueError:
                print('ERROR! Revisa nuevamente los datos ingresados\n')
            except Exception as e:
                print(e)

    def ia_turn(self, current: Node) -> Node:
        print('TURNO DE LA IA')
        return self.minimax.minimax_decision(current)
    
    def show_winner(self, key: int) -> None:
        if key == 1:
            print('El ganador es la IA')
        elif key == -1:
            print('El ganador es el JUGADOR')
        else:
            print('EMPATE')
    
    def run(self):
        print('Tablero inicial: ')
        self.inital_node.show_board()
        self.choose_player_symbol()
        self.show_player_symbol()
        current = self.inital_node
        ia_playing = False
        while True:
            if not ia_playing:
                if not self.player_turn(current):
                    print('EL JUGADOR HA FINALIZADO EL JUEGO')
                    break
                ia_playing = True
            else:
                current = self.ia_turn(current)
                current.show_board()
                ia_playing = False
            if self.minimax.terminal_function(current):
                print('JUEGO TERMINADO')
                current.show_board()
                self.show_winner(self.minimax.utility_function(current))
                break
            