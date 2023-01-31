from node_enums import NodeType, Color, Effect

class Node:
    neighbors: "list[Node]"
    nodeType: NodeType
    amount: int
    color: Color
    effect: Effect
    isCursed: bool
    id: str

    # Code format: "TN.CE" (T = node type, N = amount (optional), C = color, E = effect (optional))
    # To represent a red key, the code would be "K.R"
    # To represent a frozen pink blast door, the code would be "DX.pF"
    # To represent -1 brown exact keys, the code would be "K=-1.Y"
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
        for i, c in enumerate(left):
            if c.isdigit():
                XnodeType = left[:i]
                Xamount = left[i:]
                break
        else:
            XnodeType = left
            Xamount = ""
        Xcolor = right[0]
        Xeffect = right[1:]

        self.nodeType = {
            "K": NodeType.KEY,
            "K-": NodeType.KEY,
            "K=": NodeType.KEYABS,
            "K!": NodeType.KEYFLIP,
            "D": NodeType.DOOR,
            "D-": NodeType.DOORNEG,
            "DO": NodeType.DOORBLANK,
            "DX": NodeType.DOORX,
            "D-X": NodeType.DOORNEGX
        }[XnodeType]
        self.amount = {
            "K": int(Xamount) if Xamount else 1,
            "K-": int(Xamount),
            "K=": int(Xamount) if Xamount else 1,
            "K!": None,
            "D": int(Xamount) if Xamount else 1,
            "D-": int(Xamount),
            "DO": None,
            "DX": None,
            "D-X": None
        }[XnodeType]
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
        }[Xcolor]
        self.effect = {
            "": Effect.NONE,
            "F": Effect.FROZEN,
            "P": Effect.PAINTED,
            "E": Effect.ERODED
        }[Xeffect]
    
    def __str__(self) -> str:
        return f"Node({self.nodeType}, {self.amount}, {self.color}, {self.effect}, {self.isCursed})"

    def addNeighbor(self, node) -> None:
        if node not in self.neighbors:
            self.neighbors.append(node)