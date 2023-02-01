from node import *

class ActionType:
    OPEN: 0
    CLEAN: 1
    CURSE: 2
    BLESS: 3
    
# node - affected node
# type - OPEN = open (default), CLEAN = remove effect, CURSE = curse, BLESS = remove curse
class Action:
    node: Node
    type: ActionType
    
    def __init__(self, node: Node, type: ActionType=ActionType.OPEN) -> None:
        self.node = node
        self.type = type
    
    def __str__(self) -> str:
        typeStr = {
            ActionType.OPEN: "Open",
            ActionType.CLEAN: "Clean",
            ActionType.CURSE: "Curse",
            ActionType.BLESS: "Bless"
        }[self.type]
        return f"{typeStr} {self.node.id}"


# keys - amount of keys per color
# pool - list of nodes "available" in this state
class LevelState:
    keys: "dict[Color, int]"
    pool: "list[Node]"
    actions: "tuple[Action]"

    def __init__(self, pool: "list[Node]") -> None:
        self.keys = {color: 0 for color in range(Color.NUM_COLORS)}
        self.pool = pool
        self.actions = ()
    
    def getNextStates(self) -> "list[LevelState]":
        # TODO
        return []
