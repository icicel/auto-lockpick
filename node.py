class Color:
    WHITE = 0
    ORANGE = 1
    PURPLE = 2
    PINK = 3
    CYAN = 4
    BLACK = 5
    RED = 6
    BLUE = 7
    GREEN = 8
    BROWN = 9
    GOLD = 10
    PURE = 11
class NodeType:
    SPACE = -1
    KEY = 0
    DOOR = 1
    DOORNEG = 2
    KEYABS = 3
    DOORBLANK = 4
    DOORX = 5
    DOORNEGX = 6
class Effect:
    FROZEN = 0
    PAINTED = 1
    ERODED = 2



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