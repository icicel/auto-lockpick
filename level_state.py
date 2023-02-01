from level import Level
from node import *
from action import Action

# keys - amount of keys per color
# pool - list of nodes "available" in this state
class LevelState:
    level: Level
    keys: "dict[Color, int]"
    pool: "list[Node]"
    actions: "tuple[Action]"

    def __init__(self, level: Level) -> None:
        self.keys = {color: 0 for color in range(Color.NUM_COLORS)}
        self.pool = level.gameObjects[level.startNode].neighbors
        self.actions = ()
    
    def getNextStates(self) -> "list[LevelState]":
        # TODO
        return []
    
    def isSolved(self) -> bool:
        for node in self.pool:
            if node.id == self.level.endNode:
                return True
        return False
