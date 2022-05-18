import numpy as np
from node.Node import Node

from actions.constants import SYMBOL_EMPTY


def restrictions() -> list:
    return [
        lambda n: n.get_symbol((0,0)) == SYMBOL_EMPTY,
        lambda n: n.get_symbol((0,1)) == SYMBOL_EMPTY,
        lambda n: n.get_symbol((0,2)) == SYMBOL_EMPTY,
        lambda n: n.get_symbol((1,0)) == SYMBOL_EMPTY,
        lambda n: n.get_symbol((1,1)) == SYMBOL_EMPTY,
        lambda n: n.get_symbol((1,2)) == SYMBOL_EMPTY,
        lambda n: n.get_symbol((2,0)) == SYMBOL_EMPTY,
        lambda n: n.get_symbol((2,1)) == SYMBOL_EMPTY,
        lambda n: n.get_symbol((2,2)) == SYMBOL_EMPTY
    ]

def actions() -> list:
    return [
        lambda n, symbol: Node(np.copy(n.board), symbol, (0,0)),
        lambda n, symbol: Node(np.copy(n.board), symbol, (0,1)),
        lambda n, symbol: Node(np.copy(n.board), symbol, (0,2)),
        lambda n, symbol: Node(np.copy(n.board), symbol, (1,0)),
        lambda n, symbol: Node(np.copy(n.board), symbol, (1,1)),
        lambda n, symbol: Node(np.copy(n.board), symbol, (1,2)),
        lambda n, symbol: Node(np.copy(n.board), symbol, (2,0)),
        lambda n, symbol: Node(np.copy(n.board), symbol, (2,1)),
        lambda n, symbol: Node(np.copy(n.board), symbol, (2,2))
    ]