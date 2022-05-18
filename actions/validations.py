def validate_symbol(symbol: bytes) -> None:
    if not type(symbol) is bytes:
        #raise ValueError("The symbol must be a bytes string")
        raise Exception("ERROR! El simbolo debe ser de tipo bytes\n")
    
def validate_positions(positions: tuple) -> None:
        if not positions[0] + positions[1] <= 4 or positions[0] < 0 or positions[1] < 0:
            #raise ValueError("The positions must be between 0 and 2")
            raise Exception("ERROR! Las posiciones deben ser entre 0 y 2\n")
        
def validate_options() -> str:
    while True:
        option = input('Que simbolo quieres usar:\n[1] X [2] O: ')
        if option == '1' or option == '2':
            return option
        print('Debes ingresar una opcion valida')

def winner_conditions() -> list:
    return [
        lambda key, node: node.board[0][0] == key and node.board[0][1] == key and node.board[0][2] == key,
        lambda key, node: node.board[1][0] == key and node.board[1][1] == key and node.board[1][2] == key,
        lambda key, node: node.board[2][0] == key and node.board[2][1] == key and node.board[2][2] == key,
        lambda key, node: node.board[0][0] == key and node.board[1][0] == key and node.board[2][0] == key,
        lambda key, node: node.board[0][1] == key and node.board[1][1] == key and node.board[2][1] == key,
        lambda key, node: node.board[0][2] == key and node.board[1][2] == key and node.board[2][2] == key,
        lambda key, node: node.board[0][0] == key and node.board[1][1] == key and node.board[2][2] == key,
        lambda key, node: node.board[0][2] == key and node.board[1][1] == key and node.board[2][0] == key
    ]
