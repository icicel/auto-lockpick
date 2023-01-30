from node_enums import NodeType, Color, Effect

class Node:
    neighbors: "list[Node]"
    nodeType: NodeType
    amount: int
    color: Color
    effect: Effect
    isCursed: bool
    id: str

    # Code format: "TTn.CE" (TT = node type, n = amount (optional), C = color, E = effect (optional))
    # To represent a red key, the code would be "K.R"
    # To represent a frozen pink blast door, the code would be "DX.pF"
    # To represent -6 pure exact keys, the code would be "K=-1.X"
    def __init__(self, code: str) -> None:
        self.neighbors = []
        self.isCursed = False
        self.id = None
        if not code:
            self.nodeType = NodeType.SPACE
            self.amount = None
            self.color = Color.NONE
            self.effect = Effect.NONE
            return

        left, right = code.split(".")
        if left[:2] == "K=":
            self.nodeType = NodeType.KEYABS
            self.amount = int(left[2:]) if len(left) > 2 else 1
        elif left[:2] == "K!":
            self.nodeType = NodeType.KEYFLIP
            self.amount = None
        elif left[0] == "K":
            self.nodeType = NodeType.KEY
            self.amount = int(left[1:]) if len(left) > 1 else 1
        elif left[:3] == "D-X":
            self.nodeType = NodeType.DOORNEGX
            self.amount = None
        elif left[:2] == "D-":
            self.nodeType = NodeType.DOORNEG
            self.amount = int(left[1:])
        elif left[:2] == "D0":
            self.nodeType = NodeType.DOORBLANK
            self.amount = None
        elif left[:2] == "DX":
            self.nodeType = NodeType.DOORX
            self.amount = None
        elif left[0] == "D":
            self.nodeType = NodeType.DOOR
            self.amount = int(left[1:]) if len(left) > 1 else 1
        self.color = {
            "w": Color.WHITE,
            "o": Color.ORANGE,
            "l": Color.PURPLE,
            "p": Color.PINK,
            "c": Color.CYAN,
            "b": Color.BLACK,
            "R": Color.RED,
            "B": Color.BLUE,
            "G": Color.GREEN,
            "Y": Color.BROWN,
            "M": Color.GOLD,
            "X": Color.PURE
        }[right[0]]
        self.effect = {
            "": Effect.NONE,
            "F": Effect.FROZEN,
            "P": Effect.PAINTED,
            "E": Effect.ERODED
        }[right[1:]]
    
    def __str__(self) -> str:
        return f"Node({self.nodeType}, {self.amount}, {self.color}, {self.effect}, {self.isCursed})"

    def addNeighbor(self, node) -> None:
        if node not in self.neighbors:
            self.neighbors.append(node)