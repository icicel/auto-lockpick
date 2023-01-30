from node_enums import NodeType, Color, Effect

class Node:
    neighbors: list
    nodeType: NodeType
    amount: int
    color: Color
    effect: Effect
    isCursed: bool

    # Code format: "TTn.CE" (TT = node type, n = amount (optional), C = color, E = effect (optional))
    # To represent a stack of 6 red exact keys, the code would be "K=6.R"
    # To represent a frozen pink blast door, the code would be "DX.pF"
    # To represent -1 pure keys, the code would be "K-1.X"
    def __init__(self, code: str):
        self.neighbors = []
        self.isCursed = False
        if not code:
            self.nodeType = NodeType.SPACE
            self.amount = None
            self.color = Color.NONE
            self.effect = Effect.NONE
            return

        codeArgs = code.split(".")
        XnodeType = codeArgs[0][:2]
        Xamount = codeArgs[0][2:]
        Xcolor = codeArgs[1][:2]
        Xeffect = codeArgs[1][2:]
        self.nodeType = {
            "K+": NodeType.KEY,
            "K-": NodeType.KEYNEG,
            "K=": NodeType.KEYABS,
            "D+": NodeType.DOOR,
            "D-": NodeType.DOORNEG,
            "D0": NodeType.DOORBLANK,
            "DX": NodeType.DOORX,
            "Dx": NodeType.DOORNEGX,
        }[XnodeType]
        if XnodeType not in ["D0", "DX", "Dx"]:
            self.amount = int(Xamount)
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
            "F": Effect.FROZEN,
            "P": Effect.PAINTED,
            "E": Effect.ERODED
        }[Xeffect]