from actions.actions import actions, restrictions
from node.Node import Node


class Minimax:
    ia_symbol = ''
    player_symbol = ''
    
    def __init__(self) -> None:
        self.actions = actions()
        self.restrictions = restrictions()
        
    def minimax_decision(self, node: Node) -> Node:
        values = []
        childrens = []
        for act, res in zip(self.actions, self.restrictions):
            if res(node):
                children = act(node, self.ia_symbol)
                v = self.min_value(children)
                values.append(v)
                childrens.append(children)
        max_value = max(values)
        return childrens[values.index(max_value)]

    def max_value(self, node: Node) -> int:
        if self.terminal_function(node):
            return self.utility_function(node)
        values = []
        for act, res in zip(self.actions, self.restrictions):
            if res(node):
                children = act(node, self.ia_symbol)
                v = self.min_value(children)
                values.append(v)
        max_value = max(values)
        return max_value
    
    def min_value(self, node: Node) -> int:
        if self.terminal_function(node):
            return self.utility_function(node)
        values = []
        for act, res in zip(self.actions, self.restrictions):
            if res(node):
                children = act(node,self.player_symbol)
                v = self.max_value(children)
                values.append(v)
        min_value = min(values)
        return min_value
    
    def terminal_function(self, node: Node) -> bool:
        if node.evaluate_winning_symbol(self.ia_symbol) or node.evaluate_winning_symbol(self.player_symbol):
            return True
        elif node.no_more_movements():
            return True
        return False

    def utility_function(self, node: Node) -> int:
        if node.evaluate_winning_symbol(self.player_symbol):
            return -1
        elif node.evaluate_winning_symbol(self.ia_symbol):
            return 1
        return 0
