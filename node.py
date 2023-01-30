from node_enums import NodeType, Color, Effect

class Node:
    neighbors: list
    nodeType: NodeType
    amount: int
    color: Color
    effect: Effect
    isCursed: bool

    def __init__(self):
        self.neighbors = []
        self.nodeType = None
        self.amount = None
        self.color = None
        self.effect = None
        self.isCursed = False

    def __init__(self, code):
        pass