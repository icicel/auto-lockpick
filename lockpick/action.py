from level.node import Node

class ActionType:
    OPEN = 0
    MASTEROPEN = 1
    CLEAN = 2
    CURSE = 3
    BLESS = 4
    
# node - affected node
# type - OPEN = open (default), MASTEROPEN = open with gold key, CLEAN = remove effect, CURSE = curse, BLESS = remove curse
class Action:
    node: Node
    type: ActionType
    
    def __init__(self, node: Node, type: ActionType) -> None:
        self.node = node
        self.type = type
    
    def __str__(self) -> str:
        if self.node.isKey():
            typeStr = "Collect"
        elif self.node.isDoor():
            typeStr = {
                ActionType.OPEN: "Open",
                ActionType.MASTEROPEN: "Master-open",
                ActionType.CLEAN: "Clean",
                ActionType.CURSE: "Curse",
                ActionType.BLESS: "Bless"
            }[self.type]
        return f"{typeStr} {self.node.id} {self.node.asCode()}"
