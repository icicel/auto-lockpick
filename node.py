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
    # To represent a stack of 6 red exact keys, the code would be "K=6.R"
    # To represent a frozen pink blast door, the code would be "DX.pF"
    # To represent -1 pure keys, the code would be "K-.X"
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

        codeArgs = code.split(".")
        XnodeType = codeArgs[0][:2]
        Xamount = codeArgs[0][2:]
        Xcolor = codeArgs[1][0]
        Xeffect = codeArgs[1][1:]
        self.nodeType = {
            "K+": NodeType.KEY,
            "K-": NodeType.KEYNEG,
            "K=": NodeType.KEYABS,
            "K!": NodeType.KEYFLIP,
            "D+": NodeType.DOOR,
            "D-": NodeType.DOORNEG,
            "D0": NodeType.DOORBLANK,
            "DX": NodeType.DOORX,
            "Dx": NodeType.DOORNEGX,
        }[XnodeType]
        if XnodeType not in ["K!", "D0", "DX", "Dx"]:
            if Xamount:
                self.amount = int(Xamount)
            else:
                self.amount = 1
        else:
            self.amount = None
        self.color = {
            "W": Color.WHITE,
            "O": Color.ORANGE,
            "P": Color.PURPLE,
            "p": Color.PINK,
            "C": Color.CYAN,
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