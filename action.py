from level.node import *

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
